execute if entity @p[tag= !hunger] run summon armor_stand ~ 10 ~ {Tags: [randomizer], NoGravity: 1b}
execute if entity @p[tag= !lifesteal] run summon armor_stand ~ 11 ~ {Tags: [randomizer], NoGravity: 1b}
execute if entity @p[tag= !teleport] run summon armor_stand ~ 12 ~ {Tags: [randomizer], NoGravity: 1b}
execute if entity @p[tag= !heal] run summon armor_stand ~ 13 ~ {Tags: [randomizer], NoGravity: 1b}
$execute store result score @p $(slot) run data get entity @e[tag = randomizer, sort = random, limit = 1] Pos[1]
kill @e[tag= randomizer]