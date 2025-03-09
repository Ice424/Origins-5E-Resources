import json

file = open("powers.json", "r")
powers = json.loads(file.read())
file.close()

template = "execute if entity @p[tag= !{id}] run summon armor_stand ~ {predicate} ~ {{Tags: [randomizer], NoGravity: 1b}}"

def GetPowers(types):
    out = []
    for power in powers[types]:
        out.append(template.format(predicate=power["predicate"], id=power["id"]))

    out.append("""$execute store result score @p $(slot) run data get entity @e[tag = randomizer, sort = random, limit = 1] Pos[1]
kill @e[tag= randomizer]""")
    file = open(f"functions/{types}_slots.mcfunction", "w")
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

            file = open(f"functions/{classes}_{types}_slots.mcfunction", "w")
            file.write("\n".join(out))
            file.close()
