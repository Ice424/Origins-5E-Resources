execute if entity @p[tag= !block] run summon armor_stand ~ 65 ~ {Tags: [randomizer], NoGravity: 1b}
execute if entity @p[tag= !damage] run summon armor_stand ~ 66 ~ {Tags: [randomizer], NoGravity: 1b}
execute if entity @p[tag= !fire_res] run summon armor_stand ~ 67 ~ {Tags: [randomizer], NoGravity: 1b}
execute if entity @p[tag= !fire_ring] run summon armor_stand ~ 68 ~ {Tags: [randomizer], NoGravity: 1b}
execute if entity @p[tag= !rage] run summon armor_stand ~ 69 ~ {Tags: [randomizer], NoGravity: 1b}
execute if entity @p[tag= !stone] run summon armor_stand ~ 70 ~ {Tags: [randomizer], NoGravity: 1b}
$execute store result score @p $(slot) run data get entity @e[tag = randomizer, sort = random, limit = 1] Pos[1]
kill @e[tag= randomizer]