data modify storage ui mask insert 0 value {Slot: 9b, id: "minecraft:stick", "components": {"custom_model_data": 63, lore:["{\"color\":\"gray\",\"italic\":false,\"text\":\"none\"}"],custom_name:"{\"color\":\"#2c2d51\",\"italic\":false,\"text\":\"resistance\"}", "minecraft:custom_data": {ui_item: {empty: 1b}}}}

data modify storage ui mask insert 0 value {Slot: 10b, id: "minecraft:stick", "components": {"custom_model_data": 64, lore:["{\"color\":\"gray\",\"italic\":false,\"text\":\"none\"}"],custom_name:"{\"color\":\"#2c2d51\",\"italic\":false,\"text\":\"saturation\"}", "minecraft:custom_data": {ui_item: {empty: 1b}}}}



execute if entity @p[tag=block] run data modify storage ui mask insert 0 value {Slot: 18b, id: "minecraft:stick", "components": {"custom_model_data": 65, lore:["{\"color\":\"gray\",\"italic\":false,\"text\":\"none\"}"],custom_name:"{\"color\":\"#2c2d51\",\"italic\":false,\"text\":\"block\"}", "minecraft:custom_data": {ui_item: {cmd: "function ui:menu/tank/slot_select/open {predicate:65}"}}}}

execute if entity @p[tag=damage] run data modify storage ui mask insert 0 value {Slot: 19b, id: "minecraft:stick", "components": {"custom_model_data": 66, lore:["{\"color\":\"gray\",\"italic\":false,\"text\":\"none\"}"],custom_name:"{\"color\":\"#2c2d51\",\"italic\":false,\"text\":\"damage\"}", "minecraft:custom_data": {ui_item: {cmd: "function ui:menu/tank/slot_select/open {predicate:66}"}}}}

execute if entity @p[tag=fire_res] run data modify storage ui mask insert 0 value {Slot: 20b, id: "minecraft:stick", "components": {"custom_model_data": 67, lore:["{\"color\":\"gray\",\"italic\":false,\"text\":\"none\"}"],custom_name:"{\"color\":\"#2c2d51\",\"italic\":false,\"text\":\"fire_res\"}", "minecraft:custom_data": {ui_item: {cmd: "function ui:menu/tank/slot_select/open {predicate:67}"}}}}

execute if entity @p[tag=fire_ring] run data modify storage ui mask insert 0 value {Slot: 21b, id: "minecraft:stick", "components": {"custom_model_data": 68, lore:["{\"color\":\"gray\",\"italic\":false,\"text\":\"none\"}"],custom_name:"{\"color\":\"#2c2d51\",\"italic\":false,\"text\":\"fire_ring\"}", "minecraft:custom_data": {ui_item: {cmd: "function ui:menu/tank/slot_select/open {predicate:68}"}}}}

execute if entity @p[tag=rage] run data modify storage ui mask insert 0 value {Slot: 22b, id: "minecraft:stick", "components": {"custom_model_data": 69, lore:["{\"color\":\"gray\",\"italic\":false,\"text\":\"none\"}"],custom_name:"{\"color\":\"#2c2d51\",\"italic\":false,\"text\":\"rage\"}", "minecraft:custom_data": {ui_item: {cmd: "function ui:menu/tank/slot_select/open {predicate:69}"}}}}

execute if entity @p[tag=stone] run data modify storage ui mask insert 0 value {Slot: 23b, id: "minecraft:stick", "components": {"custom_model_data": 70, lore:["{\"color\":\"gray\",\"italic\":false,\"text\":\"none\"}"],custom_name:"{\"color\":\"#2c2d51\",\"italic\":false,\"text\":\"stone\"}", "minecraft:custom_data": {ui_item: {cmd: "function ui:menu/tank/slot_select/open {predicate:70}"}}}}

execute if entity @p[tag=ground_pound] run data modify storage ui mask insert 0 value {Slot: 24b, id: "minecraft:stick", "components": {"custom_model_data": 58, lore:["{\"color\":\"gray\",\"italic\":false,\"text\":\"none\"}"],custom_name:"{\"color\":\"#2c2d51\",\"italic\":false,\"text\":\"ground_pound\"}", "minecraft:custom_data": {ui_item: {cmd: "function ui:menu/tank/slot_select/open {predicate:58}"}}}}

execute if entity @p[tag=hook] run data modify storage ui mask insert 0 value {Slot: 25b, id: "minecraft:stick", "components": {"custom_model_data": 59, lore:["{\"color\":\"gray\",\"italic\":false,\"text\":\"none\"}"],custom_name:"{\"color\":\"#2c2d51\",\"italic\":false,\"text\":\"hook\"}", "minecraft:custom_data": {ui_item: {cmd: "function ui:menu/tank/slot_select/open {predicate:59}"}}}}

execute if entity @p[tag=knockback] run data modify storage ui mask insert 0 value {Slot: 26b, id: "minecraft:stick", "components": {"custom_model_data": 60, lore:["{\"color\":\"gray\",\"italic\":false,\"text\":\"none\"}"],custom_name:"{\"color\":\"#2c2d51\",\"italic\":false,\"text\":\"knockback\"}", "minecraft:custom_data": {ui_item: {cmd: "function ui:menu/tank/slot_select/open {predicate:60}"}}}}

execute if entity @p[tag=shield] run data modify storage ui mask insert 0 value {Slot: 27b, id: "minecraft:stick", "components": {"custom_model_data": 61, lore:["{\"color\":\"gray\",\"italic\":false,\"text\":\"none\"}"],custom_name:"{\"color\":\"#2c2d51\",\"italic\":false,\"text\":\"shield\"}", "minecraft:custom_data": {ui_item: {cmd: "function ui:menu/tank/slot_select/open {predicate:61}"}}}}

execute if entity @p[tag=thorns] run data modify storage ui mask insert 0 value {Slot: 28b, id: "minecraft:stick", "components": {"custom_model_data": 62, lore:["{\"color\":\"gray\",\"italic\":false,\"text\":\"none\"}"],custom_name:"{\"color\":\"#2c2d51\",\"italic\":false,\"text\":\"thorns\"}", "minecraft:custom_data": {ui_item: {cmd: "function ui:menu/tank/slot_select/open {predicate:62}"}}}}





