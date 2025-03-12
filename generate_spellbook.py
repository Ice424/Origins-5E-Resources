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

    passive_power_template = 'execute if entity @p[tag={id}] run data modify storage ui mask insert 0 value {{Slot: {slot}b, id:"minecraft:stick", "components": {{"custom_model_data": {predicate}, lore:["{{\\"color\\":\\"gray\\",\\"italic\\":false,\\"text\\":\\"{description}\\"}}"],custom_name:"{{\\"color\\":\\"{color}\\",\\"italic\\":false,\\"text\\":\\"{name}\\"}}", "minecraft:custom_data": {{ui_item: {{empty: 1b}}}}}}}}'

    equipped_power_template = """execute if entity @p[tag={id}] run data modify storage ui mask insert 0 value {{Slot: {slot}b, id:"minecraft:stick", "components": {{"custom_model_data": {predicate}, lore:["{{\\"color\\":\\"gray\\",\\"italic\\":false,\\"text\\":\\"{description}\\"}}"],custom_name:"{{\\"color\\":\\"{color}\\",\\"italic\\":false,\\"text\\":\\"{name}\\"}}", "minecraft:custom_data": {{ui_item:{{cmd:"function ui:menu/{type}/slot_select/open {{predicate:{predicate}}}"}}}}}}}}"""

    greyscale_powers_template = 'execute if entity @p[tag=!{id}] run data modify storage ui mask insert 0 value {{Slot: {slot}b, id:"minecraft:iron_nugget", "components": {{"custom_model_data": {predicate}, custom_name:"{{\\"color\\":\\"gray\\",\\"italic\\":false, \\"text\\":\\"{name}\\"}}", "minecraft:custom_data": {{ui_item: {{empty: 1b}}}}}}}}'

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
                        out.append(passive_power_template.format(predicate=power["predicate"], id=power["id"], slot = low_slot, type=types,     description=power["description"],   name=power["name"], color=color).replace(f"execute if entity @p[tag={power["id"]}] run  ", ""))
                        low_slot += 1
                    else:
                        out.append(passive_power_template.format(predicate=power["predicate"], id=power["id"], slot = high_special_slot, type=types,    description=power["description"],   name=power["name"], color=color))
                        out.append(greyscale_powers_template.format(predicate=power["predicate"], id=power["id"], slot = high_special_slot,     type=types, description=power["description"], name=power["name"]))
                        high_special_slot += 1


        out.append("\n\n\n" + "\n\n".join(display))
        os.makedirs(os.path.join(DATA, classes, "spellbook"), exist_ok=True)
        file = open(os.path.join(DATA, classes, "spellbook", "mask.mcfunction"), "w")
        file.write("""data modify storage ui mask set value [{Slot:0b,id:"minecraft:barrier","components":{"custom_name": "{\\"text\\":\\"Back\\",\\"color\\":\\"red\\",\\"italic\\": false}","minecraft:custom_model_data": 4, "minecraft:custom_data":{ui_item:{cmd:"function ui:menu/main/root/open"}}}}] \n\n""")
        file.write("\n\n".join(out))
        file.close()



    def GetPowers(types):
        out = []
        slot = 9
        for power in powers[types]:
            if power["predicate"] <= 1000:
                if power["key_activated"] == True:
                    out.append(equipped_power_template.format(predicate=power["predicate"], id=power["id"], slot = slot, type=types,    description=power["description"], name=power["name"], color="dark_gray" if types == "low" else "dark_purple"))


                else:
                    out.append(passive_power_template.format(predicate=power["predicate"], id=power["id"], slot = slot, type=types, description=power   ["description"], name=power["name"], color="dark_gray" if types == "low" else "dark_purple"))

                out.append(greyscale_powers_template.format(predicate=power["predicate"], id=power["id"], slot = slot, type=types, description=power    ["description"], name=power["name"]))
                slot += 1

        out.append("\n\n\n"+ "\n\n".join(display))
        os.makedirs(os.path.join(DATA, types, "spellbook"), exist_ok=True)
        file = open(os.path.join(DATA, types, "spellbook", "mask.mcfunction"), "w")
        file.write("""data modify storage ui mask set value [{Slot:0b,id:"minecraft:barrier","components":{"custom_name": "{\\"text\\":\\"Back\\", \\"color\\": \\"red\\", \\"italic\\": false}","minecraft:custom_model_data": 4, "minecraft:custom_data":{ui_item:{cmd:"function ui:menu/main/root/open"}}}}] \n\n""")
        file.write("\n\n".join(out))
        file.close()


    GetPowers("low")
    GetPowers("high")


