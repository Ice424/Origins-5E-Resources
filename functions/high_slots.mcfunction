execute if entity @p[tag= !grow] run summon armor_stand ~ 39 ~ {Tags: [randomizer], NoGravity: 1b}
execute if entity @p[tag= !inventory] run summon armor_stand ~ 40 ~ {Tags: [randomizer], NoGravity: 1b}
execute if entity @p[tag= !falling] run summon armor_stand ~ 41 ~ {Tags: [randomizer], NoGravity: 1b}
execute if entity @p[tag= !fall_damage] run summon armor_stand ~ 42 ~ {Tags: [randomizer], NoGravity: 1b}
execute if entity @p[tag= !jump] run summon armor_stand ~ 43 ~ {Tags: [randomizer], NoGravity: 1b}
execute if entity @p[tag= !permeation] run summon armor_stand ~ 44 ~ {Tags: [randomizer], NoGravity: 1b}
execute if entity @p[tag= !scan] run summon armor_stand ~ 45 ~ {Tags: [randomizer], NoGravity: 1b}
execute if entity @p[tag= !general] run summon armor_stand ~ 46 ~ {Tags: [randomizer], NoGravity: 1b}
execute if entity @p[tag= !shrink] run summon armor_stand ~ 47 ~ {Tags: [randomizer], NoGravity: 1b}
execute if entity @p[tag= !tame] run summon armor_stand ~ 48 ~ {Tags: [randomizer], NoGravity: 1b}
$execute store result score @p $(slot) run data get entity @e[tag = randomizer, sort = random, limit = 1] Pos[1]
kill @e[tag= randomizer]