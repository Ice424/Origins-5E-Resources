execute if entity @p[tag=death] run data modify storage ui mask insert 0 value {Slot: 18b, id: "minecraft:stick", "components": {"custom_model_data": 49, lore:["{\"color\":\"gray\",\"italic\":false,\"text\":\"you can gain the effects of holding a totem of undying\"}"],custom_name:"{\"color\":\"#fbf236\",\"italic\":false,\"text\":\"Divine protection\"}", "minecraft:custom_data": {ui_item: {empty: 1b}}}}

execute if entity @p[tag=!death] run data modify storage ui mask insert 0 value {Slot: 18b, id: "minecraft:iron_nugget", "components": {"custom_model_data": 49, custom_name:"{\"color\":\"gray\",\"italic\":false,\"text\":\"Divine protection\"}", "minecraft:custom_data": {ui_item: {empty: 1b}}}}

execute if entity @p[tag=luck] run data modify storage ui mask insert 0 value {Slot: 19b, id: "minecraft:stick", "components": {"custom_model_data": 50, lore:["{\"color\":\"gray\",\"italic\":false,\"text\":\"+ 3 to your luck\"}"],custom_name:"{\"color\":\"#fbf236\",\"italic\":false,\"text\":\"luck\"}", "minecraft:custom_data": {ui_item: {empty: 1b}}}}

execute if entity @p[tag=!luck] run data modify storage ui mask insert 0 value {Slot: 19b, id: "minecraft:iron_nugget", "components": {"custom_model_data": 50, custom_name:"{\"color\":\"gray\",\"italic\":false,\"text\":\"luck\"}", "minecraft:custom_data": {ui_item: {empty: 1b}}}}

execute if entity @p[tag=see] run data modify storage ui mask insert 0 value {Slot: 20b, id: "minecraft:stick", "components": {"custom_model_data": 51, lore:["{\"color\":\"gray\",\"italic\":false,\"text\":\"you can see mobs in a 10 block area\"}"],custom_name:"{\"color\":\"#fbf236\",\"italic\":false,\"text\":\"Divine eye\"}", "minecraft:custom_data": {ui_item: {empty: 1b}}}}

execute if entity @p[tag=!see] run data modify storage ui mask insert 0 value {Slot: 20b, id: "minecraft:iron_nugget", "components": {"custom_model_data": 51, custom_name:"{\"color\":\"gray\",\"italic\":false,\"text\":\"Divine eye\"}", "minecraft:custom_data": {ui_item: {empty: 1b}}}}

execute if entity @p[tag=summon] run data modify storage ui mask insert 0 value {Slot: 21b, id: "minecraft:stick", "components": {"custom_model_data": 52, lore:["{\"color\":\"gray\",\"italic\":false,\"text\":\"summon 5 zombies to assist you in battle they are friendly towards druids\"}"],custom_name:"{\"color\":\"#fbf236\",\"italic\":false,\"text\":\"Summon the dead\"}", "minecraft:custom_data": {ui_item: {cmd: "function ui:menu/cleric/slot_select/open {predicate:52}"}}}}

execute if entity @p[tag=!summon] run data modify storage ui mask insert 0 value {Slot: 21b, id: "minecraft:iron_nugget", "components": {"custom_model_data": 52, custom_name:"{\"color\":\"gray\",\"italic\":false,\"text\":\"Summon the dead\"}", "minecraft:custom_data": {ui_item: {empty: 1b}}}}

execute if entity @p[tag=hunger] run data modify storage ui mask insert 0 value {Slot: 22b, id: "minecraft:stick", "components": {"custom_model_data": 53, lore:["{\"color\":\"gray\",\"italic\":false,\"text\":\"none\"}"],custom_name:"{\"color\":\"#fbf236\",\"italic\":false,\"text\":\"hunger\"}", "minecraft:custom_data": {ui_item: {empty: 1b}}}}

execute if entity @p[tag=!hunger] run data modify storage ui mask insert 0 value {Slot: 22b, id: "minecraft:iron_nugget", "components": {"custom_model_data": 53, custom_name:"{\"color\":\"gray\",\"italic\":false,\"text\":\"hunger\"}", "minecraft:custom_data": {ui_item: {empty: 1b}}}}

execute if entity @p[tag=lifesteal] run data modify storage ui mask insert 0 value {Slot: 23b, id: "minecraft:stick", "components": {"custom_model_data": 54, lore:["{\"color\":\"gray\",\"italic\":false,\"text\":\"none\"}"],custom_name:"{\"color\":\"#fbf236\",\"italic\":false,\"text\":\"lifesteal\"}", "minecraft:custom_data": {ui_item: {empty: 1b}}}}

execute if entity @p[tag=!lifesteal] run data modify storage ui mask insert 0 value {Slot: 23b, id: "minecraft:iron_nugget", "components": {"custom_model_data": 54, custom_name:"{\"color\":\"gray\",\"italic\":false,\"text\":\"lifesteal\"}", "minecraft:custom_data": {ui_item: {empty: 1b}}}}

execute if entity @p[tag=teleport] run data modify storage ui mask insert 0 value {Slot: 24b, id: "minecraft:stick", "components": {"custom_model_data": 55, lore:["{\"color\":\"gray\",\"italic\":false,\"text\":\"none\"}"],custom_name:"{\"color\":\"#fbf236\",\"italic\":false,\"text\":\"teleport\"}", "minecraft:custom_data": {ui_item: {empty: 1b}}}}

execute if entity @p[tag=!teleport] run data modify storage ui mask insert 0 value {Slot: 24b, id: "minecraft:iron_nugget", "components": {"custom_model_data": 55, custom_name:"{\"color\":\"gray\",\"italic\":false,\"text\":\"teleport\"}", "minecraft:custom_data": {ui_item: {empty: 1b}}}}

execute if entity @p[tag=heal] run data modify storage ui mask insert 0 value {Slot: 25b, id: "minecraft:stick", "components": {"custom_model_data": 56, lore:["{\"color\":\"gray\",\"italic\":false,\"text\":\"none\"}"],custom_name:"{\"color\":\"#fbf236\",\"italic\":false,\"text\":\"heal\"}", "minecraft:custom_data": {ui_item: {cmd: "function ui:menu/cleric/slot_select/open {predicate:56}"}}}}

execute if entity @p[tag=!heal] run data modify storage ui mask insert 0 value {Slot: 25b, id: "minecraft:iron_nugget", "components": {"custom_model_data": 56, custom_name:"{\"color\":\"gray\",\"italic\":false,\"text\":\"heal\"}", "minecraft:custom_data": {ui_item: {empty: 1b}}}}

data modify storage ui mask insert 0 value {Slot: 9b, id: "minecraft:stick", "components": {"custom_model_data": 57, lore:["{\"color\":\"gray\",\"italic\":false,\"text\":\"you have 9 hearts\"}"],custom_name:"{\"color\":\"#fbf236\",\"italic\":false,\"text\":\"health\"}", "minecraft:custom_data": {ui_item: {empty: 1b}}}}

data modify storage ui mask insert 0 value {Slot: 10b, id: "minecraft:stick", "components": {"custom_model_data": 58, lore:["{\"color\":\"gray\",\"italic\":false,\"text\":\"sneak to heal you and all mobs in a 10 block radius\"}"],custom_name:"{\"color\":\"#fbf236\",\"italic\":false,\"text\":\"Regeneration aura\"}", "minecraft:custom_data": {ui_item: {empty: 1b}}}}




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