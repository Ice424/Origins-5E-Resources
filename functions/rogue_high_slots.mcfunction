execute if entity @p[tag= !blindness] run summon armor_stand ~ 46 ~ {Tags: [randomizer], NoGravity: 1b}
execute if entity @p[tag= !fall_dmg] run summon armor_stand ~ 47 ~ {Tags: [randomizer], NoGravity: 1b}
execute if entity @p[tag= !stealth_bonus] run summon armor_stand ~ 48 ~ {Tags: [randomizer], NoGravity: 1b}
$execute store result score @p $(slot) run data get entity @e[tag = randomizer, sort = random, limit = 1] Pos[1]
kill @e[tag= randomizer]