execute if entity @p[tag= !arrows] run summon armor_stand ~ 20 ~ {Tags: [randomizer], NoGravity: 1b}
execute if entity @p[tag= !poison] run summon armor_stand ~ 21 ~ {Tags: [randomizer], NoGravity: 1b}
execute if entity @p[tag= !underwater] run summon armor_stand ~ 22 ~ {Tags: [randomizer], NoGravity: 1b}
execute if entity @p[tag= !wall_climb] run summon armor_stand ~ 23 ~ {Tags: [randomizer], NoGravity: 1b}
$execute store result score @p $(slot) run data get entity @e[tag = randomizer, sort = random, limit = 1] Pos[1]
kill @e[tag= randomizer]