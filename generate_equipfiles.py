""" generate primary and secondary mcfunctions"""
import json

file = open("powers.json", "r")
powers = json.loads(file.read())
file.close()

template = """
execute if score @p predicate matches {predicate} run scoreboard players set @p {key} {predicate}
execute if score @p predicate matches {predicate} run power grant @p {path} chill:{key}
"""
primary = ["power revoke @p all chill:primary"]
secondary = ["power revoke @p all chill:secondary"]


def GetPowers(types):
    for power in powers[types]:
        if power["key_activated"] is True:
            
            path = f"chill:high/{power["id"]}/primary"
            primary.append(template.format(predicate=power["predicate"], key="primary", path=path))
            
            path = f"chill:high/{power["id"]}/secondary"
            secondary.append(template.format(predicate=power["predicate"], key="secondary", path=path))


GetPowers("low")
GetPowers("high")

for classes in powers["class"]:
    out = []
    for types in powers["class"][classes]:
        for power in powers["class"][classes][types]:
            if power["key_activated"] is True:
                path = f"chill:class/{classes}/{types}/{power["id"]}/primary"
                primary.append(template.format(predicate=power["predicate"], key="primary", path=path))
                
                path = f"chill:class/{classes}/{types}/{power["id"]}/secondary"
                secondary.append(template.format(predicate=power["predicate"], key="secondary", path=path))

primary.append("function ui:menu/main/open_spellbook")
secondary.append("function ui:menu/main/open_spellbook")

file = open("functions/primary.mcfunction", "w")
file.write("\n".join(primary))
file.close()

file = open("functions/secondary.mcfunction", "w")
file.write("\n".join(secondary))
file.close()
