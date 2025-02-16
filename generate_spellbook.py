import json

file = open("powers.json", "r")
powers = json.loads(file.read())
file.close()

ClassColours = {
    "cleric": "#fbf236",
    "druid": "#99e550",
    "fighter": "#ac3232",
    "rogue": "#121212",
    "tank": "#2c2d51",
    "wizard": "#5b6ee1"
}


template = 'execute if score @p primary matches {predicate} run data modify storage ui mask insert 0 value {{Slot: 5b, id: "minecraft:stick", "components": {{"custom_model_data": {predicate}, lore:["{{\\"color\\":\\"gray\\",\\"italic\\":false,\\"text\\":\\"{description}\\"}}"],custom_name:"{{\\"color\\":\\"{color}\\",\\"italic\\":false,\\"text\\":\\"{name}\\"}}", "minecraft:custom_data": {{ui_item: {{empty: 1b}}}}}}}}'

low_power_template = """data modify storage ui mask insert 0 value {{Slot: {slot}b, id: "minecraft:stick", "components": {{"custom_model_data": {predicate}, lore:["{{\\"color\\":\\"gray\\",\\"italic\\":false,\\"text\\":\\"{description}\\"}}"],custom_name:"{{\\"color\\":\\"{color}\\",\\"italic\\":false,\\"text\\":\\"{name}\\"}}", "minecraft:custom_data": {{ui_item: {{empty: 1b}}}}}}}}"""

all_powers_template = """execute if entity @p[tag={id}] run data modify storage ui mask insert 0 value {{Slot: {slot}b, id: "minecraft:stick", "components": {{"custom_model_data": {predicate}, lore:["{{\\"color\\":\\"gray\\",\\"italic\\":false,\\"text\\":\\"{description}\\"}}"],custom_name:"{{\\"color\\":\\"{color}\\",\\"italic\\":false,\\"text\\":\\"{name}\\"}}", "minecraft:custom_data": {{ui_item: {{cmd: "function ui:menu/{type}/slot_select/open {{predicate:{predicate}}}"}}}}}}}}"""
print(template)

# generate spellbooks

def GetPowers(types):
    out = []
    out2 = []
    all_powers = []
    slot = 18
    for power in powers[types]:
        all_powers.append(all_powers_template.format(id=power["id"], type=types, slot=slot, predicate=power["predicate"], description=power["description"], name=power["name"], color="dark_gray" if types == "low"   else "dark_purple"))
        slot += 1

        if power["key_activated"] == True: 
            out.append(template.format(predicate=power["predicate"], description=power["description"],name=power["name"], color="dark_gray" if types == "low"   else "dark_purple"))
            out2.append(template.format(predicate=power["predicate"], description=power["description"],name=power["name"], color="light_blue" if types == "low"   else "cyan").replace("primary", "secondary").replace("5b", "7b"))

    file = open(f"functions/{types}_mask.mcfunction", "w")
    file.write("\n".join(all_powers))
    file.write("\n\n")
    file.write("\n".join(out))
    file.write("\n\n")
    file.write("\n".join(out2))
    file.close()


GetPowers("low")
GetPowers("high")

for classes in powers["class"]:
    out = []
    out2 = []
    all_powers = []
    low_powers = []

    slot = 18
    low_slot = 9
    for types in powers["class"][classes]:
        for power in powers["class"][classes][types]:
            color = ClassColours[classes]
            print(types)
            if types == "passive":
                low_powers.append(low_power_template.format(id=power["id"], type=classes, slot=low_slot, predicate=power["predicate"], description=power["description"], name=power["name"], color=color))
                low_slot += 1


            else:
                all_powers.append(all_powers_template.format(id=power["id"], type=classes, slot=slot, predicate=power["predicate"], description=power["description"], name=power["name"], color=color))
                slot += 1

            if power["key_activated"] == True:

                
                out.append(template.format(predicate=power["predicate"], description=power["description"], name=power["name"], color=color))
                out2.append(template.format(predicate=power["predicate"], description=power["description"], name=power["name"], color=color).replace("primary", "secondary").replace("5b", "7b"))

        file = open(f"functions/{classes}_mask.mcfunction", "w")
        file.write("\n\n".join(low_powers))
        file.write("\n\n\n\n")
        file.write("\n\n".join(all_powers))
        file.write("\n\n\n\n")
        file.write("\n".join(out))
        file.write("\n\n")
        file.write("\n".join(out2))
        file.close()


