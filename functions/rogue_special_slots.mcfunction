execute if entity @p[tag= !dash] run summon armor_stand ~ 53 ~ {Tags: [randomizer], NoGravity: 1b}
execute if entity @p[tag= !invisibility] run summon armor_stand ~ 54 ~ {Tags: [randomizer], NoGravity: 1b}
execute if entity @p[tag= !opportunist] run summon armor_stand ~ 55 ~ {Tags: [randomizer], NoGravity: 1b}
execute if entity @p[tag= !teleport] run summon armor_stand ~ 56 ~ {Tags: [randomizer], NoGravity: 1b}
execute if entity @p[tag= !wall_climb] run summon armor_stand ~ 57 ~ {Tags: [randomizer], NoGravity: 1b}
$execute store result score @p $(slot) run data get entity @e[tag = randomizer, sort = random, limit = 1] Pos[1]
kill @e[tag= randomizer]