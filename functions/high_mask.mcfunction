execute if entity @p[tag=grow] run data modify storage ui mask insert 0 value {Slot: 9b, id: "minecraft:stick", "components": {"custom_model_data": 39, lore:["{\"color\":\"gray\",\"italic\":false,\"text\":\"You grow a block taller\"}"],custom_name:"{\"color\":\"dark_purple\",\"italic\":false,\"text\":\"Grow\"}", "minecraft:custom_data": {ui_item: {empty: 1b}}}}

execute if entity @p[tag=!grow] run data modify storage ui mask insert 0 value {Slot: 9b, id: "minecraft:iron_nugget", "components": {"custom_model_data": 39, custom_name:"{\"color\":\"gray\",\"italic\":false,\"text\":\"Grow\"}", "minecraft:custom_data": {ui_item: {empty: 1b}}}}

execute if entity @p[tag=inventory] run data modify storage ui mask insert 0 value {Slot: 10b, id: "minecraft:stick", "components": {"custom_model_data": 40, lore:["{\"color\":\"gray\",\"italic\":false,\"text\":\"you have 5 extra inventory slots they stay with you on death\"}"],custom_name:"{\"color\":\"dark_purple\",\"italic\":false,\"text\":\"Inventory\"}", "minecraft:custom_data": {ui_item: {cmd: "function ui:menu/high/slot_select/open {predicate:40}"}}}}

execute if entity @p[tag=!inventory] run data modify storage ui mask insert 0 value {Slot: 10b, id: "minecraft:iron_nugget", "components": {"custom_model_data": 40, custom_name:"{\"color\":\"gray\",\"italic\":false,\"text\":\"Inventory\"}", "minecraft:custom_data": {ui_item: {empty: 1b}}}}

execute if entity @p[tag=falling] run data modify storage ui mask insert 0 value {Slot: 11b, id: "minecraft:stick", "components": {"custom_model_data": 41, lore:["{\"color\":\"gray\",\"italic\":false,\"text\":\"none\"}"],custom_name:"{\"color\":\"dark_purple\",\"italic\":false,\"text\":\"falling\"}", "minecraft:custom_data": {ui_item: {empty: 1b}}}}

execute if entity @p[tag=!falling] run data modify storage ui mask insert 0 value {Slot: 11b, id: "minecraft:iron_nugget", "components": {"custom_model_data": 41, custom_name:"{\"color\":\"gray\",\"italic\":false,\"text\":\"falling\"}", "minecraft:custom_data": {ui_item: {empty: 1b}}}}

execute if entity @p[tag=fall_damage] run data modify storage ui mask insert 0 value {Slot: 12b, id: "minecraft:stick", "components": {"custom_model_data": 42, lore:["{\"color\":\"gray\",\"italic\":false,\"text\":\"none\"}"],custom_name:"{\"color\":\"dark_purple\",\"italic\":false,\"text\":\"fall_damage\"}", "minecraft:custom_data": {ui_item: {empty: 1b}}}}

execute if entity @p[tag=!fall_damage] run data modify storage ui mask insert 0 value {Slot: 12b, id: "minecraft:iron_nugget", "components": {"custom_model_data": 42, custom_name:"{\"color\":\"gray\",\"italic\":false,\"text\":\"fall_damage\"}", "minecraft:custom_data": {ui_item: {empty: 1b}}}}

execute if entity @p[tag=jump] run data modify storage ui mask insert 0 value {Slot: 13b, id: "minecraft:stick", "components": {"custom_model_data": 43, lore:["{\"color\":\"gray\",\"italic\":false,\"text\":\"by crouching you can jump high\"}"],custom_name:"{\"color\":\"dark_purple\",\"italic\":false,\"text\":\"Jump\"}", "minecraft:custom_data": {ui_item: {empty: 1b}}}}

execute if entity @p[tag=!jump] run data modify storage ui mask insert 0 value {Slot: 13b, id: "minecraft:iron_nugget", "components": {"custom_model_data": 43, custom_name:"{\"color\":\"gray\",\"italic\":false,\"text\":\"Jump\"}", "minecraft:custom_data": {ui_item: {empty: 1b}}}}

execute if entity @p[tag=permeation] run data modify storage ui mask insert 0 value {Slot: 14b, id: "minecraft:stick", "components": {"custom_model_data": 44, lore:["{\"color\":\"gray\",\"italic\":false,\"text\":\"you can temporarily phase through walls\"}"],custom_name:"{\"color\":\"dark_purple\",\"italic\":false,\"text\":\"phasing\"}", "minecraft:custom_data": {ui_item: {cmd: "function ui:menu/high/slot_select/open {predicate:44}"}}}}

execute if entity @p[tag=!permeation] run data modify storage ui mask insert 0 value {Slot: 14b, id: "minecraft:iron_nugget", "components": {"custom_model_data": 44, custom_name:"{\"color\":\"gray\",\"italic\":false,\"text\":\"phasing\"}", "minecraft:custom_data": {ui_item: {empty: 1b}}}}

execute if entity @p[tag=scan] run data modify storage ui mask insert 0 value {Slot: 15b, id: "minecraft:stick", "components": {"custom_model_data": 45, lore:["{\"color\":\"gray\",\"italic\":false,\"text\":\"reveal all entities in 40 a block radius\"}"],custom_name:"{\"color\":\"dark_purple\",\"italic\":false,\"text\":\"scan\"}", "minecraft:custom_data": {ui_item: {cmd: "function ui:menu/high/slot_select/open {predicate:45}"}}}}

execute if entity @p[tag=!scan] run data modify storage ui mask insert 0 value {Slot: 15b, id: "minecraft:iron_nugget", "components": {"custom_model_data": 45, custom_name:"{\"color\":\"gray\",\"italic\":false,\"text\":\"scan\"}", "minecraft:custom_data": {ui_item: {empty: 1b}}}}

execute if entity @p[tag=general] run data modify storage ui mask insert 0 value {Slot: 16b, id: "minecraft:stick", "components": {"custom_model_data": 46, lore:["{\"color\":\"gray\",\"italic\":false,\"text\":\"none\"}"],custom_name:"{\"color\":\"dark_purple\",\"italic\":false,\"text\":\"general\"}", "minecraft:custom_data": {ui_item: {empty: 1b}}}}

execute if entity @p[tag=!general] run data modify storage ui mask insert 0 value {Slot: 16b, id: "minecraft:iron_nugget", "components": {"custom_model_data": 46, custom_name:"{\"color\":\"gray\",\"italic\":false,\"text\":\"general\"}", "minecraft:custom_data": {ui_item: {empty: 1b}}}}

execute if entity @p[tag=shrink] run data modify storage ui mask insert 0 value {Slot: 17b, id: "minecraft:stick", "components": {"custom_model_data": 47, lore:["{\"color\":\"gray\",\"italic\":false,\"text\":\"You shrink a block\"}"],custom_name:"{\"color\":\"dark_purple\",\"italic\":false,\"text\":\"shrink\"}", "minecraft:custom_data": {ui_item: {empty: 1b}}}}

execute if entity @p[tag=!shrink] run data modify storage ui mask insert 0 value {Slot: 17b, id: "minecraft:iron_nugget", "components": {"custom_model_data": 47, custom_name:"{\"color\":\"gray\",\"italic\":false,\"text\":\"shrink\"}", "minecraft:custom_data": {ui_item: {empty: 1b}}}}

execute if entity @p[tag=tame] run data modify storage ui mask insert 0 value {Slot: 18b, id: "minecraft:stick", "components": {"custom_model_data": 48, lore:["{\"color\":\"gray\",\"italic\":false,\"text\":\"you can tame all tameable mobs in a 4 block radius\"}"],custom_name:"{\"color\":\"dark_purple\",\"italic\":false,\"text\":\"Tame\"}", "minecraft:custom_data": {ui_item: {cmd: "function ui:menu/high/slot_select/open {predicate:48}"}}}}

execute if entity @p[tag=!tame] run data modify storage ui mask insert 0 value {Slot: 18b, id: "minecraft:iron_nugget", "components": {"custom_model_data": 48, custom_name:"{\"color\":\"gray\",\"italic\":false,\"text\":\"Tame\"}", "minecraft:custom_data": {ui_item: {empty: 1b}}}}




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