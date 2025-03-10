import json
import os
from pathlib import Path

os.chdir(Path(__file__).parents[1])

DATA = os.path.abspath(
    "./saves/New World/datapacks/Origins-5E-Data/data/ui/function/menu")

# Load the JSON data from the file
with open("resourcepacks/powers.json", "r") as file:
    powers = json.load(file)

ClassColours = {
    "cleric": "#fbf236",
    "druid": "#99e550",
    "fighter": "#ac3232",
    "rogue": "#121212",
    "tank": "#2c2d51",
    "wizard": "#5b6ee1"
}

power_display_template = 'execute if score @p {key} matches {predicate} run data modify storage ui mask insert 0 value {{Slot: {slot}b, id: "minecraft:stick", "components": {{"custom_model_data": {predicate}, lore:["{{\\"color\\":\\"gray\\",\\"italic\\":false,\\"text\\":\\"{description}\\"}}"],custom_name:"{{\\"color\\":\\"{color}\\",\\"italic\\":false,\\"text\\":\\"{name}\\"}}", "minecraft:custom_data": {{ui_item: {{empty: 1b}}}}}}}}'

def GetPowers(types):
    for power in powers[types]:
        if types == "low":
            low.append(power_display_template.format(key="slot_1", predicate=power["predicate"], name=power["name"], description=power["description"], slot=10, color="dark_gray"))
        elif types == "high":
            high.append(power_display_template.format(key="slot_2", predicate=power["predicate"], name=power["name"], description=power["description"], slot=12, color="dark_purple"))
    
low = []
high = []
class_high = []
special = []
GetPowers("low")
GetPowers("high")



for classes in powers["class"]:
    for types in powers["class"][classes]:
            for power in powers["class"][classes][types]:
                color = ClassColours[classes]
                if types != "passive":
                    if types == "high":
                        class_high.append(power_display_template.format(key="slot_3", predicate=power["predicate"], name=power["name"], description=power["description"], slot=14, color=color))
                    else:
                        special.append(power_display_template.format(key="slot_4", predicate=power["predicate"], name=power["name"], description=power["description"], slot=16, color=color))



file = open(os.path.join(DATA, "main", "shop", "mask.mcfunction"), "w")
file.write("""data modify storage ui mask set value [{Slot:0b,id:"minecraft:barrier","components":{"custom_name": "{\\"text\\": \\"Back\\", \\"color\\": \\"red\\", \\"italic\\": false}","minecraft:custom_data":{ui_item:{cmd:"function ui:menu/main/root/open"}}}}]""")
file.write("\n\n")
file.write("""data modify storage ui mask insert 0 value {Slot: 22b, id: "minecraft:stick", "components": {"custom_model_data": 5, custom_name:"{\\"color\\":\\"dark_gray\\",\\"italic\\":false,\\"text\\":\\"Refresh\\"}", "minecraft:custom_data": {ui_item: {cmd: "function ui:menu/main/reset_slots"}}}}""")
file.write("\n\n")

file.write("\n\n".join(low))
file.write("\n\n")
file.write("\n\n".join(high))
file.write("\n\n")
file.write("\n\n".join(class_high))
file.write("\n\n")
file.write("\n\n".join(special))
file.close()
