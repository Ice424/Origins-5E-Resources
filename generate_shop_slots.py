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

    template = "execute if entity @p[tag=!{id}] run summon armor_stand ~ {predicate} ~ {{Tags: [randomizer], NoGravity: 1b}}"
    low_template = "execute if entity @p[{line}] run summon armor_stand ~ {predicate} ~ {{Tags: [randomizer], NoGravity: 1b}}"
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
    #print(low_powers)

    
    for group, items in low_powers.items():
        ids = [item['id'] for item in items]
        predicates = [item['predicate'] for item in items]

        # Line 1: All negated, predicate of the first item
        all_negated = [f"tag=!{id_}" for id_ in ids]
        #print(", ".join(all_negated) + f" {predicates[0]}")
        out.append(low_template.format(line=", ".join(all_negated), predicate=predicates[0]))
        # Lines 2 to N-1: One positive tag, others negated
        for i in range(len(ids) - 1):
            tags = []
            for j, id_ in enumerate(ids):
                if j == i:
                    tags.append(f"tag={id_}")
                else:
                    tags.append(f"tag=!{id_}")
            #print(", ".join(tags) + f" {predicates[i + 1]}")
            out.append(low_template.format(line=", ".join(tags), predicate=predicates[i+1]))
        #print()  # blank line between groups
            
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
