execute if entity @p[tag= !ground_pound] run summon armor_stand ~ 58 ~ {Tags: [randomizer], NoGravity: 1b}
execute if entity @p[tag= !hook] run summon armor_stand ~ 59 ~ {Tags: [randomizer], NoGravity: 1b}
execute if entity @p[tag= !knockback] run summon armor_stand ~ 60 ~ {Tags: [randomizer], NoGravity: 1b}
execute if entity @p[tag= !shield] run summon armor_stand ~ 61 ~ {Tags: [randomizer], NoGravity: 1b}
execute if entity @p[tag= !thorns] run summon armor_stand ~ 62 ~ {Tags: [randomizer], NoGravity: 1b}
$execute store result score @p $(slot) run data get entity @e[tag = randomizer, sort = random, limit = 1] Pos[1]
kill @e[tag= randomizer]