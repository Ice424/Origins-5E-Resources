execute if entity @p[tag=ddamgemobs] run data modify storage ui mask insert 0 value {Slot: 18b, id: "minecraft:stick", "components": {"custom_model_data": 72, lore:["{\"color\":\"gray\",\"italic\":false,\"text\":\"you deal double damage to hostile mobs\"}"],custom_name:"{\"color\":\"#ac3232\",\"italic\":false,\"text\":\"Damage to mobs\"}", "minecraft:custom_data": {ui_item: {empty: 1b}}}}

execute if entity @p[tag=!ddamgemobs] run data modify storage ui mask insert 0 value {Slot: 18b, id: "minecraft:iron_nugget", "components": {"custom_model_data": 72, custom_name:"{\"color\":\"gray\",\"italic\":false,\"text\":\"Damage to mobs\"}", "minecraft:custom_data": {ui_item: {empty: 1b}}}}

execute if entity @p[tag=hotvillage] run data modify storage ui mask insert 0 value {Slot: 19b, id: "minecraft:stick", "components": {"custom_model_data": 73, lore:["{\"color\":\"gray\",\"italic\":false,\"text\":\"you have permanent hero of the village\"}"],custom_name:"{\"color\":\"#ac3232\",\"italic\":false,\"text\":\"Hero of the village\"}", "minecraft:custom_data": {ui_item: {empty: 1b}}}}

execute if entity @p[tag=!hotvillage] run data modify storage ui mask insert 0 value {Slot: 19b, id: "minecraft:iron_nugget", "components": {"custom_model_data": 73, custom_name:"{\"color\":\"gray\",\"italic\":false,\"text\":\"Hero of the village\"}", "minecraft:custom_data": {ui_item: {empty: 1b}}}}

execute if entity @p[tag=reach] run data modify storage ui mask insert 0 value {Slot: 20b, id: "minecraft:stick", "components": {"custom_model_data": 74, lore:["{\"color\":\"gray\",\"italic\":false,\"text\":\"you get 6 block reach\"}"],custom_name:"{\"color\":\"#ac3232\",\"italic\":false,\"text\":\"Increased reach\"}", "minecraft:custom_data": {ui_item: {empty: 1b}}}}

execute if entity @p[tag=!reach] run data modify storage ui mask insert 0 value {Slot: 20b, id: "minecraft:iron_nugget", "components": {"custom_model_data": 74, custom_name:"{\"color\":\"gray\",\"italic\":false,\"text\":\"Increased reach\"}", "minecraft:custom_data": {ui_item: {empty: 1b}}}}

execute if entity @p[tag=saturation] run data modify storage ui mask insert 0 value {Slot: 21b, id: "minecraft:stick", "components": {"custom_model_data": 75, lore:["{\"color\":\"gray\",\"italic\":false,\"text\":\"you have permanent saturation\"}"],custom_name:"{\"color\":\"#ac3232\",\"italic\":false,\"text\":\"Saturation\"}", "minecraft:custom_data": {ui_item: {empty: 1b}}}}

execute if entity @p[tag=!saturation] run data modify storage ui mask insert 0 value {Slot: 21b, id: "minecraft:iron_nugget", "components": {"custom_model_data": 75, custom_name:"{\"color\":\"gray\",\"italic\":false,\"text\":\"Saturation\"}", "minecraft:custom_data": {ui_item: {empty: 1b}}}}

execute if entity @p[tag=speed_upgrade] run data modify storage ui mask insert 0 value {Slot: 22b, id: "minecraft:stick", "components": {"custom_model_data": 76, lore:["{\"color\":\"gray\",\"italic\":false,\"text\":\"you have permanent speed 2\"}"],custom_name:"{\"color\":\"#ac3232\",\"italic\":false,\"text\":\"Speed\"}", "minecraft:custom_data": {ui_item: {empty: 1b}}}}

execute if entity @p[tag=!speed_upgrade] run data modify storage ui mask insert 0 value {Slot: 22b, id: "minecraft:iron_nugget", "components": {"custom_model_data": 76, custom_name:"{\"color\":\"gray\",\"italic\":false,\"text\":\"Speed\"}", "minecraft:custom_data": {ui_item: {empty: 1b}}}}

execute if entity @p[tag=arrows] run data modify storage ui mask insert 0 value {Slot: 23b, id: "minecraft:stick", "components": {"custom_model_data": 77, lore:["{\"color\":\"gray\",\"italic\":false,\"text\":\"none\"}"],custom_name:"{\"color\":\"#ac3232\",\"italic\":false,\"text\":\"arrows\"}", "minecraft:custom_data": {ui_item: {cmd: "function ui:menu/fighter/slot_select/open {predicate:77}"}}}}

execute if entity @p[tag=!arrows] run data modify storage ui mask insert 0 value {Slot: 23b, id: "minecraft:iron_nugget", "components": {"custom_model_data": 77, custom_name:"{\"color\":\"gray\",\"italic\":false,\"text\":\"arrows\"}", "minecraft:custom_data": {ui_item: {empty: 1b}}}}

execute if entity @p[tag=overheal] run data modify storage ui mask insert 0 value {Slot: 24b, id: "minecraft:stick", "components": {"custom_model_data": 78, lore:["{\"color\":\"gray\",\"italic\":false,\"text\":\"you heal 20 hearts and gain 5 temporary hearts\"}"],custom_name:"{\"color\":\"#ac3232\",\"italic\":false,\"text\":\"Overheal\"}", "minecraft:custom_data": {ui_item: {cmd: "function ui:menu/fighter/slot_select/open {predicate:78}"}}}}

execute if entity @p[tag=!overheal] run data modify storage ui mask insert 0 value {Slot: 24b, id: "minecraft:iron_nugget", "components": {"custom_model_data": 78, custom_name:"{\"color\":\"gray\",\"italic\":false,\"text\":\"Overheal\"}", "minecraft:custom_data": {ui_item: {empty: 1b}}}}

execute if entity @p[tag=powered] run data modify storage ui mask insert 0 value {Slot: 25b, id: "minecraft:stick", "components": {"custom_model_data": 79, lore:["{\"color\":\"gray\",\"italic\":false,\"text\":\"you gain resistance 2 and strength 2 for a short period\"}"],custom_name:"{\"color\":\"#ac3232\",\"italic\":false,\"text\":\"Powered up\"}", "minecraft:custom_data": {ui_item: {cmd: "function ui:menu/fighter/slot_select/open {predicate:79}"}}}}

execute if entity @p[tag=!powered] run data modify storage ui mask insert 0 value {Slot: 25b, id: "minecraft:iron_nugget", "components": {"custom_model_data": 79, custom_name:"{\"color\":\"gray\",\"italic\":false,\"text\":\"Powered up\"}", "minecraft:custom_data": {ui_item: {empty: 1b}}}}

execute if entity @p[tag=speedboost] run data modify storage ui mask insert 0 value {Slot: 26b, id: "minecraft:stick", "components": {"custom_model_data": 80, lore:["{\"color\":\"gray\",\"italic\":false,\"text\":\"you can gain speed 3 for a short period\"}"],custom_name:"{\"color\":\"#ac3232\",\"italic\":false,\"text\":\"Swiftness\"}", "minecraft:custom_data": {ui_item: {cmd: "function ui:menu/fighter/slot_select/open {predicate:80}"}}}}

execute if entity @p[tag=!speedboost] run data modify storage ui mask insert 0 value {Slot: 26b, id: "minecraft:iron_nugget", "components": {"custom_model_data": 80, custom_name:"{\"color\":\"gray\",\"italic\":false,\"text\":\"Swiftness\"}", "minecraft:custom_data": {ui_item: {empty: 1b}}}}

data modify storage ui mask insert 0 value {Slot: 9b, id: "minecraft:stick", "components": {"custom_model_data": 81, lore:["{\"color\":\"gray\",\"italic\":false,\"text\":\"you have permanent haste 1\"}"],custom_name:"{\"color\":\"#ac3232\",\"italic\":false,\"text\":\"Haste\"}", "minecraft:custom_data": {ui_item: {empty: 1b}}}}

data modify storage ui mask insert 0 value {Slot: 10b, id: "minecraft:stick", "components": {"custom_model_data": 82, lore:["{\"color\":\"gray\",\"italic\":false,\"text\":\"you gain 4 hearts\"}"],custom_name:"{\"color\":\"#ac3232\",\"italic\":false,\"text\":\"Health increase\"}", "minecraft:custom_data": {ui_item: {empty: 1b}}}}

data modify storage ui mask insert 0 value {Slot: 11b, id: "minecraft:stick", "components": {"custom_model_data": 83, lore:["{\"color\":\"gray\",\"italic\":false,\"text\":\"you have permanent speed 1\"}"],custom_name:"{\"color\":\"#ac3232\",\"italic\":false,\"text\":\"Speed\"}", "minecraft:custom_data": {ui_item: {empty: 1b}}}}

data modify storage ui mask insert 0 value {Slot: 12b, id: "minecraft:stick", "components": {"custom_model_data": 84, lore:["{\"color\":\"gray\",\"italic\":false,\"text\":\"you have permanent strength 1\"}"],custom_name:"{\"color\":\"#ac3232\",\"italic\":false,\"text\":\"Strength\"}", "minecraft:custom_data": {ui_item: {empty: 1b}}}}




execute if score @p primary matches 52 run data modify storage ui mask insert 0 value {Slot: 5b, id: "minecraft:stick", "components": {"custom_model_data": 52, lore:["{\"color\":\"gray\",\"italic\":false,\"text\":\"summon 5 zombies to assist you in battle they are friendly towards druids\"}"],custom_name:"{\"color\":\"#fbf236\",\"italic\":false,\"text\":\"Summon the dead\"}", "minecraft:custom_data": {ui_item: {empty: 1b}}}}

execute if score @p secondary matches 52 run data modify storage ui mask insert 0 value {Slot: 7b, id: "minecraft:stick", "components": {"custom_model_data": 52, lore:["{\"color\":\"gray\",\"italic\":false,\"text\":\"summon 5 zombies to assist you in battle they are friendly towards druids\"}"],custom_name:"{\"color\":\"#fbf236\",\"italic\":false,\"text\":\"Summon the dead\"}", "minecraft:custom_data": {ui_item: {empty: 1b}}}}

execute if score @p primary matches 56 run data modify storage ui mask insert 0 value {Slot: 5b, id: "minecraft:stick", "components": {"custom_model_data": 56, lore:["{\"color\":\"gray\",\"italic\":false,\"text\":\"none\"}"],custom_name:"{\"color\":\"#fbf236\",\"italic\":false,\"text\":\"heal\"}", "minecraft:custom_data": {ui_item: {empty: 1b}}}}

execute if score @p secondary matches 56 run data modify storage ui mask insert 0 value {Slot: 7b, id: "minecraft:stick", "components": {"custom_model_data": 56, lore:["{\"color\":\"gray\",\"italic\":false,\"text\":\"none\"}"],custom_name:"{\"color\":\"#fbf236\",\"italic\":false,\"text\":\"heal\"}", "minecraft:custom_data": {ui_item: {empty: 1b}}}}

execute if score @p primary matches 77 run data modify storage ui mask insert 0 value {Slot: 5b, id: "minecraft:stick", "components": {"custom_model_data": 77, lore:["{\"color\":\"gray\",\"italic\":false,\"text\":\"none\"}"],custom_name:"{\"color\":\"#ac3232\",\"italic\":false,\"text\":\"arrows\"}", "minecraft:custom_data": {ui_item: {empty: 1b}}}}

execute if score @p secondary matches 77 run data modify storage ui mask insert 0 value {Slot: 7b, id: "minecraft:stick", "components": {"custom_model_data": 77, lore:["{\"color\":\"gray\",\"italic\":false,\"text\":\"none\"}"],custom_name:"{\"color\":\"#ac3232\",\"italic\":false,\"text\":\"arrows\"}", "minecraft:custom_data": {ui_item: {empty: 1b}}}}

execute if score @p primary matches 78 run data modify storage ui mask insert 0 value {Slot: 5b, id: "minecraft:stick", "components": {"custom_model_data": 78, lore:["{\"color\":\"gray\",\"italic\":false,\"text\":\"you heal 20 hearts and gain 5 temporary hearts\"}"],custom_name:"{\"color\":\"#ac3232\",\"italic\":false,\"text\":\"Overheal\"}", "minecraft:custom_data": {ui_item: {empty: 1b}}}}

execute if score @p secondary matches 78 run data modify storage ui mask insert 0 value {Slot: 7b, id: "minecraft:stick", "components": {"custom_model_data": 78, lore:["{\"color\":\"gray\",\"italic\":false,\"text\":\"you heal 20 hearts and gain 5 temporary hearts\"}"],custom_name:"{\"color\":\"#ac3232\",\"italic\":false,\"text\":\"Overheal\"}", "minecraft:custom_data": {ui_item: {empty: 1b}}}}

execute if score @p primary matches 79 run data modify storage ui mask insert 0 value {Slot: 5b, id: "minecraft:stick", "components": {"custom_model_data": 79, lore:["{\"color\":\"gray\",\"italic\":false,\"text\":\"you gain resistance 2 and strength 2 for a short period\"}"],custom_name:"{\"color\":\"#ac3232\",\"italic\":false,\"text\":\"Powered up\"}", "minecraft:custom_data": {ui_item: {empty: 1b}}}}

execute if score @p secondary matches 79 run data modify storage ui mask insert 0 value {Slot: 7b, id: "minecraft:stick", "components": {"custom_model_data": 79, lore:["{\"color\":\"gray\",\"italic\":false,\"text\":\"you gain resistance 2 and strength 2 for a short period\"}"],custom_name:"{\"color\":\"#ac3232\",\"italic\":false,\"text\":\"Powered up\"}", "minecraft:custom_data": {ui_item: {empty: 1b}}}}

execute if score @p primary matches 80 run data modify storage ui mask insert 0 value {Slot: 5b, id: "minecraft:stick", "components": {"custom_model_data": 80, lore:["{\"color\":\"gray\",\"italic\":false,\"text\":\"you can gain speed 3 for a short period\"}"],custom_name:"{\"color\":\"#ac3232\",\"italic\":false,\"text\":\"Swiftness\"}", "minecraft:custom_data": {ui_item: {empty: 1b}}}}

execute if score @p secondary matches 80 run data modify storage ui mask insert 0 value {Slot: 7b, id: "minecraft:stick", "components": {"custom_model_data": 80, lore:["{\"color\":\"gray\",\"italic\":false,\"text\":\"you can gain speed 3 for a short period\"}"],custom_name:"{\"color\":\"#ac3232\",\"italic\":false,\"text\":\"Swiftness\"}", "minecraft:custom_data": {ui_item: {empty: 1b}}}}

execute if score @p primary matches 113 run data modify storage ui mask insert 0 value {Slot: 5b, id: "minecraft:stick", "components": {"custom_model_data": 113, lore:["{\"color\":\"gray\",\"italic\":false,\"text\":\"none\"}"],custom_name:"{\"color\":\"#5b6ee1\",\"italic\":false,\"text\":\"lightning\"}", "minecraft:custom_data": {ui_item: {empty: 1b}}}}

execute if score @p secondary matches 113 run data modify storage ui mask insert 0 value {Slot: 7b, id: "minecraft:stick", "components": {"custom_model_data": 113, lore:["{\"color\":\"gray\",\"italic\":false,\"text\":\"none\"}"],custom_name:"{\"color\":\"#5b6ee1\",\"italic\":false,\"text\":\"lightning\"}", "minecraft:custom_data": {ui_item: {empty: 1b}}}}