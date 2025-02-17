execute if entity @p[tag= !grow] run summon armor_stand ~ 82 ~ {Tags: [randomizer], NoGravity: 1b}
execute if entity @p[tag= !inventory] run summon armor_stand ~ 83 ~ {Tags: [randomizer], NoGravity: 1b}
execute if entity @p[tag= !falling] run summon armor_stand ~ 84 ~ {Tags: [randomizer], NoGravity: 1b}
execute if entity @p[tag= !fall_damage] run summon armor_stand ~ 85 ~ {Tags: [randomizer], NoGravity: 1b}
execute if entity @p[tag= !jump] run summon armor_stand ~ 86 ~ {Tags: [randomizer], NoGravity: 1b}
execute if entity @p[tag= !permeation] run summon armor_stand ~ 87 ~ {Tags: [randomizer], NoGravity: 1b}
execute if entity @p[tag= !scan] run summon armor_stand ~ 88 ~ {Tags: [randomizer], NoGravity: 1b}
execute if entity @p[tag= !general] run summon armor_stand ~ 89 ~ {Tags: [randomizer], NoGravity: 1b}
execute if entity @p[tag= !shrink] run summon armor_stand ~ 90 ~ {Tags: [randomizer], NoGravity: 1b}
execute if entity @p[tag= !tame] run summon armor_stand ~ 91 ~ {Tags: [randomizer], NoGravity: 1b}
$execute store result score @p $(slot) run data get entity @ e[tag = randomizer, sort = random, limit = 1] Pos[1]
kill @e[tag= randomizer]