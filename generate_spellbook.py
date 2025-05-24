import json
import os
from pathlib import Path

def generate_spellbook():
    os.chdir(Path(__file__).parents[1])

    file = open("resourcepacks/powers.json", "r")
    powers = json.loads(file.read())
    file.close()

    DATA = os.path.abspath(
        "./saves/New World/datapacks/Origins-5E-Data/data/ui/function/menu")

    ClassColours = {
        "cleric": "#fbf236",
        "druid": "#99e550",
        "fighter": "#ac3232",
        "rogue": "#121212",
        "tank": "#2c2d51",
        "wizard": "#5b6ee1"
    }

    PREDICATES = {
        "high": 2,
        "low": 3,
        "fighter": 4,
        "cleric": 4,
        "druid": 4,
        "rogue": 4,
        "tank": 4,
        "wizard": 4
        
    }
    
    passive_power_template = 'execute if entity @p[tag={id}] run data modify storage ui mask insert 0 value {{Slot: {slot}b, id:"minecraft:stick", "components": {{"custom_model_data": {predicate}, lore:["{{\\"color\\":\\"gray\\",\\"italic\\":false,\\"text\\":\\"{description}\\"}}"],custom_name:"{{\\"color\\":\\"{color}\\",\\"italic\\":false,\\"text\\":\\"{name}\\"}}", "minecraft:custom_data": {{ui_item: {{empty: 1b}}}}}}}}'

    equipped_power_template = """execute if entity @p[tag={id}] run data modify storage ui mask insert 0 value {{Slot: {slot}b, id:"minecraft:stick", "components": {{"custom_model_data": {predicate}, lore:["{{\\"color\\":\\"gray\\",\\"italic\\":false,\\"text\\":\\"{description}\\"}}"],custom_name:"{{\\"color\\":\\"{color}\\",\\"italic\\":false,\\"text\\":\\"{name}\\"}}", "minecraft:custom_data": {{ui_item:{{cmd:"function ui:menu/{type}/slot_select/open {{predicate:{predicate}}}"}}}}}}}}"""

    greyscale_powers_template = 'execute if entity @p[tag=!{id}] run data modify storage ui mask insert 0 value {{Slot: {slot}b, id:"minecraft:iron_nugget", "components": {{"custom_model_data": {predicate}, custom_name:"{{\\"color\\":\\"dark_gray\\",\\"italic\\":false, \\"text\\":\\"{name}\\"}}", "minecraft:custom_data": {{ui_item: {{empty: 1b}}}}}}}}'

    equipped_display_template = 'execute if score @p {key} matches {predicate} run data modify storage ui mask insert 0 value {{Slot: {slot}b, id:"minecraft:stick", "components": {{"custom_model_data": {predicate}, lore:["{{\\"color\\":\\"gray\\",\\"italic\\":false,\\"text\\":\\"{description}\\"}}"],custom_name:"{{\\"color\\":\\"{color}\\",\\"italic\\":false,\\"text\\":\\"{name}\\"}}", "minecraft:custom_data": {{ui_item:{{empty: 1b}}}}}}}}'

    # generate spellbooks
    display = []
    for classes in powers["class"]:

        for types in powers["class"][classes]:
            for power in powers["class"][classes][types]:
                color = ClassColours[classes]
                if power["predicate"] <= 1000:

                    if power["key_activated"] is True:

                        display.append(equipped_display_template.format(slot=5, key="primary", name=power["name"], predicate=power["predicate"],    description=power  ["description"], color=color))
                        display.append(equipped_display_template.format(slot=7, key="secondary", name=power["name"], predicate=power["predicate"],  description=power    ["description"], color=color))
    for power in powers["high"]:
            if power["key_activated"] is True:
                display.append(equipped_display_template.format(slot=5, key="primary", name=power["name"], predicate=power["predicate"],    description=power  ["description"], color="dark_gray" if types == "low" else "dark_purple"))
                display.append(equipped_display_template.format(slot=7, key="secondary", name=power["name"], predicate=power["predicate"],    description=power  ["description"], color="dark_gray" if types == "low" else "dark_purple"))


    for classes in powers["class"]:
        out = []
        low_slot = 9
        high_special_slot = 18
        for types in powers["class"][classes]:
            for power in powers["class"][classes][types]:
                color = ClassColours[classes]
                if power["predicate"] <= 1000:
                    if power["key_activated"] is True:
                        out.append(equipped_power_template.format(predicate=power["predicate"], id=power["id"], slot=high_special_slot,     type=classes, description=power["description"],  name=power["name"], color=color))
                        out.append(greyscale_powers_template.format(predicate=power["predicate"], id=power["id"], slot = high_special_slot,     type=classes, description=power["description"], name=power["name"]))
                        high_special_slot += 1
                    elif types == "passive":
                        out.append(passive_power_template.format(predicate=power["predicate"], id=power["id"], slot = low_slot, type=types,     description=power["description"],   name=power["name"], color=color).replace(f"execute if entity @p[tag={power["id"]}] run ", ""))
                        low_slot += 1
                    else:
                        out.append(passive_power_template.format(predicate=power["predicate"], id=power["id"], slot = high_special_slot, type=types,    description=power["description"],   name=power["name"], color=color))
                        out.append(greyscale_powers_template.format(predicate=power["predicate"], id=power["id"], slot = high_special_slot,     type=types, description=power["description"], name=power["name"]))
                        high_special_slot += 1

        
        out.append("\n\n\n" + "\n\n".join(display))
        os.makedirs(os.path.join(DATA, classes, "spellbook"), exist_ok=True)
        file = open(os.path.join(DATA, classes, "spellbook", "mask.mcfunction"), "w", encoding="UTF-8")
        file.write(f"""data modify storage ui mask set value [{{Slot:0b,id:"minecraft:barrier","components":{{"custom_name": "{{\\"text\\":\\"Back\\",\\"color\\":\\"red\\",\\"italic\\": false}}","minecraft:custom_model_data": {PREDICATES[classes]}, "minecraft:custom_data":{{ui_item:{{cmd:"function ui:menu/main/root/open"}}}}}}}}, {{Slot:1b,id:"minecraft:barrier","components":{{"custom_name": "{{\\"text\\":\\"Low Powers\\",\\"color\\":\\"blue\\",\\"italic\\": false}}", "minecraft:custom_data":{{ui_item:{{cmd:"function ui:menu/low/spellbook/open"}}}}}}}},{{Slot:8b,id:"minecraft:barrier","components":{{"custom_name": "{{\\"text\\":\\"General Powers\\",\\"color\\":\\"blue\\",\\"italic\\": false}}", "minecraft:custom_data":{{ui_item:{{cmd:"function ui:menu/high/spellbook/open"}}}}}}}}] \n\n""")
        file.write("\n\n".join(out))
        file.close()
        
        file = open(os.path.join(DATA, classes, "spellbook", "open.mcfunction"), "w", encoding="UTF-8")
        file.write(f"""function ui:menu/{classes}/spellbook/mask
data modify storage ui current set from storage ui mask
execute on passengers run data modify entity @s data.page.mask set value \"function ui:menu/{classes}/spellbook/mask\"""")
        file.close()



    
    out = []
    
    slot = 9
    for power in powers["high"]:
        if power["predicate"] <= 1000:
            if power["key_activated"] == True:
                out.append(equipped_power_template.format(predicate=power["predicate"], id=power["id"], slot = slot, type="high",    description=power["description"], name=power["name"], color="dark_purple"))
            else:
                out.append(passive_power_template.format(predicate=power["predicate"], id=power["id"], slot = slot, type="high", description=power   ["description"], name=power["name"], color="dark_purple"))
            out.append(greyscale_powers_template.format(predicate=power["predicate"], id=power["id"], slot = slot, type="high", description=power    ["description"], name=power["name"]))
            slot += 1
    out.append("\n\n\n"+ "\n\n".join(display))
    os.makedirs(os.path.join(DATA, "high", "spellbook"), exist_ok=True)
    file = open(os.path.join(DATA, "high", "spellbook", "mask.mcfunction"), "w", encoding="UTF-8")
    
    file.write("""data modify storage ui mask set value [{Slot:0b,id:"minecraft:barrier","components":{"custom_name": "{\\"text\\":\\"Back\\", \\"color\\": \\"red\\", \\"italic\\": false}","minecraft:custom_model_data": 2, "minecraft:custom_data":{ui_item:{cmd:"function ui:menu/main/root/open"}}}},{Slot:1b,id:"minecraft:barrier","components":{"custom_name": "{\\"text\\":\\"Class Powers\\",\\"color\\":\\"blue\\",\\"italic\\": false}", "minecraft:custom_data":{ui_item:{cmd:"function ui:menu/main/open_spellbook"}}}}, {Slot:8b,id:"minecraft:barrier","components":{"custom_name": "{\\"text\\":\\"Low Powers\\",\\"color\\":\\"blue\\",\\"italic\\": false}", "minecraft:custom_data":{ui_item:{cmd:"function ui:menu/low/spellbook/open"}}}}] \n\n""")
    
        
    file.write("\n\n".join(out))
    file.close()
    
    file = open(os.path.join(DATA, "high", "spellbook", "open.mcfunction"), "w", encoding="UTF-8")
    file.write(f"""function ui:menu/high/spellbook/mask
data modify storage ui current set from storage ui mask
execute on passengers run data modify entity @s data.page.mask set value \"function ui:menu/high/spellbook/mask\"""")
    file.close()


    out = []
    low_powers = {}
    for power in powers["low"]:
        low_powers[power["name"]] = []
    for power in powers["low"]:
        low_powers[power["name"]].append({"id":power["id"], "predicate": power["predicate"], "name": power["name"], "description": power["description"]})
        
    slot = 9
    for power in low_powers:

        if power != "xp_xp":
            for upgrade in low_powers[power]:
                out.append(passive_power_template.format(predicate=upgrade["predicate"], id=upgrade["id"], slot = slot, type="low", description=upgrade["description"], name=upgrade["name"], color="gray"))
                out.append(greyscale_powers_template.format(predicate=upgrade["predicate"], id=upgrade["id"], slot = slot, type="low", description=upgrade["description"], name=upgrade["name"]))
        slot += 1
    out.append("\n\n\n"+ "\n\n".join(display))
    os.makedirs(os.path.join(DATA, "low", "spellbook"), exist_ok=True)
    file = open(os.path.join(DATA, "low", "spellbook", "mask.mcfunction"), "w", encoding="UTF-8")
    
    file.write("""data modify storage ui mask set value [{Slot:0b,id:"minecraft:barrier","components":{"custom_name": "{\\"text\\":\\"Back\\", \\"color\\": \\"red\\", \\"italic\\": false}","minecraft:custom_model_data": 2, "minecraft:custom_data":{ui_item:{cmd:"function ui:menu/main/root/open"}}}},{Slot:8b,id:"minecraft:barrier","components":{"custom_name": "{\\"text\\":\\"Class Powers\\",\\"color\\":\\"blue\\",\\"italic\\": false}", "minecraft:custom_data":{ui_item:{cmd:"function ui:menu/main/open_spellbook"}}}}, {Slot:1b,id:"minecraft:barrier","components":{"custom_name": "{\\"text\\":\\"General Powers\\",\\"color\\":\\"blue\\",\\"italic\\": false}", "minecraft:custom_data":{ui_item:{cmd:"function ui:menu/high/spellbook/open"}}}}] \n\n""")
    
        
    file.write("\n\n".join(out))
    file.close()
    
    file = open(os.path.join(DATA, "low", "spellbook", "open.mcfunction"), "w", encoding="UTF-8")
    file.write(f"""function ui:menu/low/spellbook/mask
data modify storage ui current set from storage ui mask
execute on passengers run data modify entity @s data.page.mask set value \"function ui:menu/low/spellbook/mask\"""")
    file.close()
    

