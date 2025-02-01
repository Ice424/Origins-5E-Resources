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

print(template)

def GetPowers(types):
    out = []
    for power in powers[types]:
        if power["key_activated"] == True: 
            out.append(template.format(predicate=power["predicate"], description=power["description"],name=power["name"], color="dark_gray" if types == "low"   else "dark_purple"))
    file = open(f"{types}.mcfunction", "w")
    file.write("\n".join(out))
    file.close()


GetPowers("low")
GetPowers("high")

for classes in powers["class"]:
    out = []
    for types in powers["class"][classes]:
        for power in powers["class"][classes][types]:
            if power["key_activated"] == True:
                print(power)
                color = ClassColours[classes]
                out.append(template.format(predicate=power["predicate"], description=power["description"], name=power["name"], color="gold"))
        file = open(f"{classes}.mcfunction", "w")
        file.write("\n".join(out))
        file.close()

            

