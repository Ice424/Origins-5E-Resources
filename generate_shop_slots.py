import json
import os
from pathlib import Path

def generate_shop_slots():
    os.chdir(Path(__file__).parents[1])
    DATA = os.path.abspath(
        "./saves/New World/datapacks/Origins-5E-Data/data/ui/function/menu")
    file = open("resourcepacks/powers.json", "r")
    powers = json.loads(file.read())
    file.close()

    template = "execute if entity @p[tag= !{id}] run summon armor_stand ~ {predicate} ~ {{Tags: [randomizer], NoGravity: 1b}}"

    def GetPowers(types):
        out = []
        for power in powers[types]:
            out.append(template.format(predicate=power["predicate"], id=power["id"]))

        out.append("""$execute store result score @p $(slot) run data get entity @e[tag = randomizer, sort = random, limit = 1] Pos[1]
kill @e[tag= randomizer]""")
        file = open(os.path.join(DATA,"main", f"{types}_slots.mcfunction"), "w")
        file.write("\n".join(out))
        file.close()


    GetPowers("low")
    GetPowers("high")

    for classes in powers["class"]:

        for types in powers["class"][classes]:
            if types != "passive":
                out = []
                for power in powers["class"][classes][types]:
                    out.append(template.format(predicate=power["predicate"], id=power["id"]))

                out.append("""$execute store result score @p $(slot) run data get entity @e[tag = randomizer, sort = random, limit = 1] Pos[1]
kill @e[tag= randomizer]""")
                file = open(os.path.join(DATA, f"{classes}/{classes}_{types}_slots.mcfunction"), "w")
                file.write("\n".join(out))
                file.close()
