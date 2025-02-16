data modify storage ui mask insert 0 value {Slot: 9b, id: "minecraft:stick", "components": {"custom_model_data": 49, lore:["{\"color\":\"gray\",\"italic\":false,\"text\":\"none\"}"],custom_name:"{\"color\":\"#121212\",\"italic\":false,\"text\":\"agro\"}", "minecraft:custom_data": {ui_item: {empty: 1b}}}}

data modify storage ui mask insert 0 value {Slot: 10b, id: "minecraft:stick", "components": {"custom_model_data": 50, lore:["{\"color\":\"gray\",\"italic\":false,\"text\":\"none\"}"],custom_name:"{\"color\":\"#121212\",\"italic\":false,\"text\":\"footsteps\"}", "minecraft:custom_data": {ui_item: {empty: 1b}}}}

data modify storage ui mask insert 0 value {Slot: 11b, id: "minecraft:stick", "components": {"custom_model_data": 51, lore:["{\"color\":\"gray\",\"italic\":false,\"text\":\"none\"}"],custom_name:"{\"color\":\"#121212\",\"italic\":false,\"text\":\"hearts\"}", "minecraft:custom_data": {ui_item: {empty: 1b}}}}

data modify storage ui mask insert 0 value {Slot: 12b, id: "minecraft:stick", "components": {"custom_model_data": 52, lore:["{\"color\":\"gray\",\"italic\":false,\"text\":\"none\"}"],custom_name:"{\"color\":\"#121212\",\"italic\":false,\"text\":\"nametag\"}", "minecraft:custom_data": {ui_item: {empty: 1b}}}}



execute if entity @p[tag=dash] run data modify storage ui mask insert 0 value {Slot: 18b, id: "minecraft:stick", "components": {"custom_model_data": 53, lore:["{\"color\":\"gray\",\"italic\":false,\"text\":\"none\"}"],custom_name:"{\"color\":\"#121212\",\"italic\":false,\"text\":\"dash\"}", "minecraft:custom_data": {ui_item: {cmd: "function ui:menu/rogue/slot_select/open {predicate:53}"}}}}

execute if entity @p[tag=invisibility] run data modify storage ui mask insert 0 value {Slot: 19b, id: "minecraft:stick", "components": {"custom_model_data": 54, lore:["{\"color\":\"gray\",\"italic\":false,\"text\":\"none\"}"],custom_name:"{\"color\":\"#121212\",\"italic\":false,\"text\":\"invisibility\"}", "minecraft:custom_data": {ui_item: {cmd: "function ui:menu/rogue/slot_select/open {predicate:54}"}}}}

execute if entity @p[tag=opportunist] run data modify storage ui mask insert 0 value {Slot: 20b, id: "minecraft:stick", "components": {"custom_model_data": 55, lore:["{\"color\":\"gray\",\"italic\":false,\"text\":\"none\"}"],custom_name:"{\"color\":\"#121212\",\"italic\":false,\"text\":\"opportunist\"}", "minecraft:custom_data": {ui_item: {cmd: "function ui:menu/rogue/slot_select/open {predicate:55}"}}}}

execute if entity @p[tag=teleport] run data modify storage ui mask insert 0 value {Slot: 21b, id: "minecraft:stick", "components": {"custom_model_data": 56, lore:["{\"color\":\"gray\",\"italic\":false,\"text\":\"none\"}"],custom_name:"{\"color\":\"#121212\",\"italic\":false,\"text\":\"teleport\"}", "minecraft:custom_data": {ui_item: {cmd: "function ui:menu/rogue/slot_select/open {predicate:56}"}}}}

execute if entity @p[tag=wall_climb] run data modify storage ui mask insert 0 value {Slot: 22b, id: "minecraft:stick", "components": {"custom_model_data": 57, lore:["{\"color\":\"gray\",\"italic\":false,\"text\":\"none\"}"],custom_name:"{\"color\":\"#121212\",\"italic\":false,\"text\":\"wall_climb\"}", "minecraft:custom_data": {ui_item: {cmd: "function ui:menu/rogue/slot_select/open {predicate:57}"}}}}

execute if entity @p[tag=blindness] run data modify storage ui mask insert 0 value {Slot: 23b, id: "minecraft:stick", "components": {"custom_model_data": 46, lore:["{\"color\":\"gray\",\"italic\":false,\"text\":\"none\"}"],custom_name:"{\"color\":\"#121212\",\"italic\":false,\"text\":\"blindness\"}", "minecraft:custom_data": {ui_item: {cmd: "function ui:menu/rogue/slot_select/open {predicate:46}"}}}}

execute if entity @p[tag=fall_dmg] run data modify storage ui mask insert 0 value {Slot: 24b, id: "minecraft:stick", "components": {"custom_model_data": 47, lore:["{\"color\":\"gray\",\"italic\":false,\"text\":\"none\"}"],custom_name:"{\"color\":\"#121212\",\"italic\":false,\"text\":\"fall_dmg\"}", "minecraft:custom_data": {ui_item: {cmd: "function ui:menu/rogue/slot_select/open {predicate:47}"}}}}

execute if entity @p[tag=stealth_bonus] run data modify storage ui mask insert 0 value {Slot: 25b, id: "minecraft:stick", "components": {"custom_model_data": 48, lore:["{\"color\":\"gray\",\"italic\":false,\"text\":\"none\"}"],custom_name:"{\"color\":\"#121212\",\"italic\":false,\"text\":\"stealth_bonus\"}", "minecraft:custom_data": {ui_item: {cmd: "function ui:menu/rogue/slot_select/open {predicate:48}"}}}}





