execute if entity @p[tag= !fly] run summon armor_stand ~ 78 ~ {Tags: [randomizer], NoGravity: 1b}
execute if entity @p[tag= !slow_fall] run summon armor_stand ~ 79 ~ {Tags: [randomizer], NoGravity: 1b}
execute if entity @p[tag= !wither] run summon armor_stand ~ 80 ~ {Tags: [randomizer], NoGravity: 1b}
execute if entity @p[tag= !lightning] run summon armor_stand ~ 81 ~ {Tags: [randomizer], NoGravity: 1b}
$execute store result score @p $(slot) run data get entity @e[tag = randomizer, sort = random, limit = 1] Pos[1]
kill @e[tag= randomizer]