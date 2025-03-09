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
slot_select_template = 'execute if score @p predicate matches {predicate} run data modify storage ui mask insert 0 value {{Slot: {slot}b, id: \"minecraft:stick\", \"components\": {{\"custom_model_data\": {predicate}, custom_name:\"{{\\"color\\":\\"{color}\\",\\"italic\\":false,\\"text\\":\\"{name}\\"}}\", \"minecraft:custom_data\": {{ui_item: {{cmd: \"function ui:menu/main/{key}\"}}}}}}}}'


# generate spellbooks
out = []
for classes in powers["class"]:
    
    for types in powers["class"][classes]:
        for power in powers["class"][classes][types]:
            color = ClassColours[classes]
            if power["key_activated"] is True:
                out.append(slot_select_template.format(slot=21, key="primary", predicate=power["predicate"], color=color, name = "Primary"))
                out.append(slot_select_template.format(slot=23, key="secondary", predicate=power["predicate"],  color=color, name = "Secondary"))
    file = open(f"functions/{classes}_slot_select.mcfunction", "w")
    file.write("\n\n".join(out))
    file.close()
    



def GetPowers(types):
    out = []
    slot = 9
    for power in powers[types]:
            if power["key_activated"] == True:
                out.append(slot_select_template.format(slot=21, name = "Primary", key="primary", predicate=power["predicate"], color="dark_gray" if types == "low" else "dark_purple"))
                out.append(slot_select_template.format(slot=23, name = "Secondary", key="secondary", predicate=power["predicate"],  color="dark_gray" if types == "low" else"dark_purple"))
            
    file = open(f"functions/{types}_slot_select.mcfunction", "w")
    file.write("\n\n".join(out))
    file.close()


GetPowers("low")
GetPowers("high")


