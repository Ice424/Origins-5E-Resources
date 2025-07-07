""" generate primary and secondary mcfunctions"""
import json
import os
from pathlib import Path

def generate_equipfiles():

    os.chdir(Path(__file__).parents[1])


    DATA = os.path.abspath(
        "./saves/New World/datapacks/Origins-5E-Data/data/ui/function/menu")

    file = open("./resourcepacks/powers.json", "r")
    powers = json.loads(file.read())
    file.close()

    template = """execute as @a[scores={{ui.id=1..}}] if score @s ui.id = @s ui.id run execute if score @s predicate matches {predicate} run scoreboard players set @s {key} {predicate}
execute as @a[scores={{ui.id=1..}}] if score @s ui.id = @s ui.id run execute if score @s predicate matches {predicate} run power grant @s {path} chill:{key}
    """
    primary = ["execute as @a[scores={ui.id=1..}] if score @s ui.id = @s ui.id run power revoke @s all chill:primary"]
    secondary = ["execute as @a[scores={ui.id=1..}] if score @s ui.id = @s ui.id run power revoke @s all chill:secondary"]


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

    file = open(os.path.join(DATA, "main", "primary.mcfunction"), "w", encoding="UTF-8")
    file.write("\n".join(primary))
    file.close()

    file = open(os.path.join(DATA, "main", "secondary.mcfunction"), "w", encoding="UTF-8")
    file.write("\n".join(secondary))
    file.close()
