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
        "rogue": "#403352",
        "tank": "#2c2d51",
        "wizard": "#5b6ee1"
    }

    PREDICATES = {
        "high": 2,
        "low": 3,
        "fighter": 4,
        "cleric": 8,
        "druid": 9,
        "rogue": 10,
        "tank": 11,
        "wizard": 12
        
    }
    
    passive_power_template = """function ui:minecart/if_player_selector {{selector:"tag={id}", cmd:'data modify storage ui mask insert 0 value {{Slot: {slot}b, id:"minecraft:stick", "components": {{"custom_model_data": {predicate}, lore:[\\'{{"color":"gray","italic":false,"text":"{description}"}}\\'],custom_name:\\'{{"color":"{color}","italic":false,"text":"{name}"}}\\', "minecraft:custom_data": {{ui_item: {{empty: 1b}}}}}}}}'}}"""

    equipped_power_template = """function ui:minecart/if_player_selector {{selector:"tag={id}", cmd:'data modify storage ui mask insert 0 value {{Slot: {slot}b, id:"minecraft:stick", "components": {{"custom_model_data": {predicate}, lore:[\\'{{"color":"gray","italic":false,"text":"{description}"}}\\'],custom_name:\\'{{"color":"{color}","italic":false,"text":"{name}"}}\\', "minecraft:custom_data": {{ui_item:{{cmd:"function ui:menu/{type}/slot_select/open {{predicate:{predicate}}}"}}}}}}}}'}}"""

    greyscale_powers_template = """function ui:minecart/if_player_selector {{selector:"tag=!{id}", cmd:'data modify storage ui mask insert 0 value {{Slot: {slot}b, id:"minecraft:iron_nugget", "components": {{"custom_model_data": {predicate}, custom_name:\\'{{"color":"dark_gray","italic":false, "text":"{name}"}}\\', "minecraft:custom_data": {{ui_item: {{empty: 1b}}}}}}}}'}}"""

    equipped_display_template = """function ui:minecart/if_player {{objective:"{key}", score:"{predicate}", cmd:'data modify storage ui mask insert 0 value {{Slot: {slot}b, id:"minecraft:stick", "components": {{"custom_model_data": {predicate}, lore:[\\'{{"color":"gray","italic":false,"text":"{description}"}}\\'],custom_name:\\'{{"color":"{color}","italic":false,"text":"{name}"}}\\', "minecraft:custom_data": {{ui_item:{{empty: 1b}}}}}}}}'}}"""

    # generate spellbooks
    display = []
    for classes in powers["class"]:

        for types in powers["class"][classes]:
            for power in powers["class"][classes][types]:
                color = ClassColours[classes]
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
                        out.append(equipped_power_template.format(predicate=power["predicate"], id=power["id"], slot=high_special_slot,     type=classes, description=power["description"].replace("'", "\\'"),  name=power["name"], color=color))
                        out.append(greyscale_powers_template.format(predicate=power["predicate"], id=power["id"], slot = high_special_slot,     type=classes, description=power["description"].replace("'", "\\'"), name=power["name"]))
                        high_special_slot += 1
                    elif types == "passive":
                        out.append("""data modify storage ui mask insert 0 value {{Slot: {slot}b, id:"minecraft:stick", "components": {{"custom_model_data": {predicate}, lore:['{{"color":"gray","italic":false,"text":"{description}"}}'],custom_name:'{{"color":"{color}","italic":false,"text":"{name}"}}', "minecraft:custom_data": {{ui_item: {{empty: 1b}}}}}}}}""".format(predicate=power["predicate"], slot = low_slot,  description=power["description"].replace("'", "\\'"),  name=power["name"], color=color, id=power["id"]))
                        low_slot += 1
                    else:
                        out.append(passive_power_template.format(predicate=power["predicate"], id=power["id"], slot = high_special_slot, type=types,    description=power["description"].replace("'", "\\'"),   name=power["name"], color=color))
                        out.append(greyscale_powers_template.format(predicate=power["predicate"], id=power["id"], slot = high_special_slot,     type=types, description=power["description"].replace("'", "\\'"), name=power["name"]))
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
            out.append(greyscale_powers_template.format(predicate=power["predicate"], id=power["id"], slot = slot, type="high",    description=power["description"].replace("'", "\\'"), name=power["name"], color="dark_purple"))
            if power["id"] != "grow" and power["id"] != "shrink":
                if power["key_activated"] == True:
                    out.append(equipped_power_template.format(predicate=power["predicate"], id=power["id"], slot = slot, type="high",    description=power["description"].replace("'", "\\'"), name=power["name"], color="dark_purple"))
                else:
                    out.append(passive_power_template.format(predicate=power["predicate"], id=power["id"], slot = slot, type="high", description=power   ["description"], name=power["name"], color="dark_purple"))
            else:
                if power["id"] == "grow": 
                    
                    out.append(f"""function ui:minecart/if_player_selector_score {{if: "if", objective:"size", score:"1", selector:"tag={power["id"]}", cmd:'data modify storage ui mask insert 0 value {{Slot: {slot}b, id:"minecraft:acacia_boat", "components": {{"enchantment_glint_override":true, "custom_model_data": {power["predicate"]}, lore:[\\'{{"color":"gray","italic":false,"text":"{power["description"]} click to toggle"}}\\'],custom_name:\\'{{"color":"{"dark_purple"}","italic":false,"text":"{power["name"]}"}}\\', "minecraft:custom_data": {{ui_item:{{cmd:"function ui:minecart/as_player {{cmd:\\'function ui:menu/main/size_toggle {{predicate:{power["predicate"]}}}\\' }}"}}}}}}}}'}}""")
                    
                    out.append(f"""function ui:minecart/if_player_selector_score {{if: "unless", objective:"size", score:"1", selector:"tag={power["id"]}", cmd:'data modify storage ui mask insert 0 value {{Slot: {slot}b, id:"minecraft:stick", "components": {{"enchantment_glint_override":false, "custom_model_data": {power["predicate"]}, lore:[\\'{{"color":"gray","italic":false,"text":"{power["description"]} click to toggle"}}\\'],custom_name:\\'{{"color":"{"dark_purple"}","italic":false,"text":"{power["name"]}"}}\\', "minecraft:custom_data": {{ui_item:{{cmd:"function ui:minecart/as_player {{cmd:\\'function ui:menu/main/size_toggle {{predicate:{power["predicate"]}}}\\' }}"}}}}}}}}'}}""")
                    
                else:
                    out.append(f"""function ui:minecart/if_player_selector_score {{if: "if", objective:"size", score:"2", selector:"tag={power["id"]}", cmd:'data modify storage ui mask insert 0 value {{Slot: {slot}b, id:"minecraft:acacia_boat", "components": {{"enchantment_glint_override":true, "custom_model_data": {power["predicate"]}, lore:[\\'{{"color":"gray","italic":false,"text":"{power["description"]} click to toggle"}}\\'],custom_name:\\'{{"color":"{"dark_purple"}","italic":false,"text":"{power["name"]}"}}\\', "minecraft:custom_data": {{ui_item:{{cmd:"function ui:minecart/as_player {{cmd:\\'function ui:menu/main/size_toggle {{predicate:{power["predicate"]}}}\\' }}"}}}}}}}}'}}""")
                    
                    out.append(f"""function ui:minecart/if_player_selector_score {{if: "unless", objective:"size", score:"2", selector:"tag={power["id"]}", cmd:'data modify storage ui mask insert 0 value {{Slot: {slot}b, id:"minecraft:stick", "components": {{"enchantment_glint_override":false, "custom_model_data": {power["predicate"]}, lore:[\\'{{"color":"gray","italic":false,"text":"{power["description"]} click to toggle"}}\\'],custom_name:\\'{{"color":"{"dark_purple"}","italic":false,"text":"{power["name"]}"}}\\', "minecraft:custom_data": {{ui_item:{{cmd:"function ui:minecart/as_player {{cmd:\\'function ui:menu/main/size_toggle {{predicate:{power["predicate"]}}}\\' }}"}}}}}}}}'}}""")
            
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
        exclusions = []
        if power != "xp_xp":
            for upgrade in low_powers[power]:
                out.append(passive_power_template.format(predicate=upgrade["predicate"], id=upgrade["id"], slot = slot, type="low", description=upgrade["description"], name=upgrade["name"], color="gray"))
                exclusions.append(upgrade["id"])
        
            out.append(greyscale_powers_template.format(predicate=low_powers[power][0]["predicate"], id=", tag=!".join(exclusions), slot = slot, type="low", description=low_powers[power][0]["description"], name=low_powers[power][0]["name"]))
        slot += 1
    out.append("\n\n\n"+ "\n\n".join(display))
    os.makedirs(os.path.join(DATA, "low", "spellbook"), exist_ok=True)
    file = open(os.path.join(DATA, "low", "spellbook", "mask.mcfunction"), "w", encoding="UTF-8")
    
    file.write("""data modify storage ui mask set value [{Slot:0b,id:"minecraft:barrier","components":{"custom_name": "{\\"text\\":\\"Back\\", \\"color\\": \\"red\\", \\"italic\\": false}","minecraft:custom_model_data": 3, "minecraft:custom_data":{ui_item:{cmd:"function ui:menu/main/root/open"}}}},{Slot:8b,id:"minecraft:barrier","components":{"custom_name": "{\\"text\\":\\"Class Powers\\",\\"color\\":\\"blue\\",\\"italic\\": false}", "minecraft:custom_data":{ui_item:{cmd:"function ui:menu/main/open_spellbook"}}}}, {Slot:1b,id:"minecraft:barrier","components":{"custom_name": "{\\"text\\":\\"General Powers\\",\\"color\\":\\"blue\\",\\"italic\\": false}", "minecraft:custom_data":{ui_item:{cmd:"function ui:menu/high/spellbook/open"}}}}] \n\n""")
    
        
    file.write("\n\n".join(out))
    file.close()
    
    file = open(os.path.join(DATA, "low", "spellbook", "open.mcfunction"), "w", encoding="UTF-8")
    file.write(f"""function ui:menu/low/spellbook/mask
data modify storage ui current set from storage ui mask
execute on passengers run data modify entity @s data.page.mask set value \"function ui:menu/low/spellbook/mask\"""")
    file.close()
    

generate_spellbook()