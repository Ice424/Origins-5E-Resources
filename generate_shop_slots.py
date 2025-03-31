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
    low_template = "execute if entity @p[tag={id}] run summon armor_stand ~ {predicate} ~ {{Tags: [randomizer], NoGravity: 1b}}"
    out = []
    for power in powers["high"]:
        out.append(template.format(predicate=power["predicate"], id=power["id"]))
    out.append("""$execute store result score @p $(slot) run data get entity @e[tag = randomizer, sort = random, limit = 1] Pos[1]
kill @e[tag= randomizer]""")
    file = open(os.path.join(DATA,"main", "high_slots.mcfunction"), "w", encoding="UTF-8")
    file.write("\n".join(out))
    file.close()


    out = []
    low_powers = {}
    for power in powers["low"]:
        low_powers[power["name"]] = []
    for power in powers["low"]:
        low_powers[power["name"]].append({"id":power["id"], "predicate": power["predicate"]})

    for low_power in low_powers:
        if low_powers[low_power][0]["id"] != "xp_xp":
            
            out.append(template.format(predicate=low_powers[low_power][0]["predicate"], id=low_powers[low_power][0]["id"]))
            
            for i in range(len(low_powers[low_power])-1):
                out.append(low_template.format(predicate=low_powers[low_power][i]["predicate"]+1, id=low_powers[low_power][i]["id"]))


    out.append("""$execute store result score @p $(slot) run data get entity @e[tag = randomizer, sort = random, limit = 1] Pos[1]
kill @e[tag= randomizer]""")
    file = open(os.path.join(DATA,"main", "low_slots.mcfunction"), "w", encoding="UTF-8")
    file.write("\n".join(out))
    file.close()
    

    for classes in powers["class"]:

        for types in powers["class"][classes]:
            if types != "passive":
                out = []
                for power in powers["class"][classes][types]:
                    out.append(template.format(predicate=power["predicate"], id=power["id"]))

                out.append("""$execute store result score @p $(slot) run data get entity @e[tag = randomizer, sort = random, limit = 1] Pos[1]
kill @e[tag= randomizer]""")
                os.makedirs(os.path.join(DATA, f"{classes}/"), exist_ok=True)
                file = open(os.path.join(DATA, f"{classes}/{types}_slots.mcfunction"), "w")
                file.write("\n".join(out))
                file.close()
generate_shop_slots()