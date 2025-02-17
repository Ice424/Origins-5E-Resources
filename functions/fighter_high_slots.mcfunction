execute if entity @p[tag= !ddamgemobs] run summon armor_stand ~ 33 ~ {Tags: [randomizer], NoGravity: 1b}
execute if entity @p[tag= !hotvillage] run summon armor_stand ~ 34 ~ {Tags: [randomizer], NoGravity: 1b}
execute if entity @p[tag= !reach] run summon armor_stand ~ 35 ~ {Tags: [randomizer], NoGravity: 1b}
execute if entity @p[tag= !saturation] run summon armor_stand ~ 36 ~ {Tags: [randomizer], NoGravity: 1b}
execute if entity @p[tag= !speed_upgrade] run summon armor_stand ~ 37 ~ {Tags: [randomizer], NoGravity: 1b}
execute if entity @p[tag= !arrows] run summon armor_stand ~ 38 ~ {Tags: [randomizer], NoGravity: 1b}
execute if entity @p[tag= !overheal] run summon armor_stand ~ 39 ~ {Tags: [randomizer], NoGravity: 1b}
execute if entity @p[tag= !powered] run summon armor_stand ~ 40 ~ {Tags: [randomizer], NoGravity: 1b}
execute if entity @p[tag= !speedboost] run summon armor_stand ~ 41 ~ {Tags: [randomizer], NoGravity: 1b}
$execute store result score @p $(slot) run data get entity @e[tag = randomizer, sort = random, limit = 1] Pos[1]
kill @e[tag= randomizer]