import json

file = open("powers.json", "r")
powers = json.loads(file.read())
file.close()



template = """$execute if score @s primary matches {predicate} run data modify storage ui mask insert 0 value {{Slot: $(slot)b, id: "minecraft:stick", "components": {{"custom_model_data": {predicate}, "custom_name": "{{\\"text\\": \\"{name}\\", \\"color\\": \\"{color}\\", \\"italic\\": false}}", "minecraft:custom_data": {{ui_item: {{empty: 1b}}}}}}}}"""



def GetPowers(types):
    for power in powers[types]:
        print(template.format(predicate=power["predicate"], name=power["name"], color="dark_gray" if types == "low" else "dark_purple"))
GetPowers("low")
GetPowers("high")

for classes in powers["class"]:
    for types in powers["class"][classes]:
        for power in powers["class"][classes][types]:
            file = open("data/chill/powers/class/" + classes + "/" + types + ".json", "r")
            file.write(json.dumps(power, indent=4))
            file.close()


            

