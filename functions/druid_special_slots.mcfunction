execute if entity @p[tag= !animal_control] run summon armor_stand ~ 28 ~ {Tags: [randomizer], NoGravity: 1b}
execute if entity @p[tag= !bone_meal] run summon armor_stand ~ 29 ~ {Tags: [randomizer], NoGravity: 1b}
execute if entity @p[tag= !freeze] run summon armor_stand ~ 30 ~ {Tags: [randomizer], NoGravity: 1b}
execute if entity @p[tag= !skulk] run summon armor_stand ~ 31 ~ {Tags: [randomizer], NoGravity: 1b}
execute if entity @p[tag= !speed] run summon armor_stand ~ 32 ~ {Tags: [randomizer], NoGravity: 1b}
$execute store result score @p $(slot) run data get entity @e[tag = randomizer, sort = random, limit = 1] Pos[1]
kill @e[tag= randomizer]