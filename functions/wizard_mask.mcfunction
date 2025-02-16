data modify storage ui mask insert 0 value {Slot: 9b, id: "minecraft:stick", "components": {"custom_model_data": 75, lore:["{\"color\":\"gray\",\"italic\":false,\"text\":\"All the projectiles you shoot inflict glowing\"}"],custom_name:"{\"color\":\"#5b6ee1\",\"italic\":false,\"text\":\"Spectral shot\"}", "minecraft:custom_data": {ui_item: {empty: 1b}}}}

data modify storage ui mask insert 0 value {Slot: 10b, id: "minecraft:stick", "components": {"custom_model_data": 76, lore:["{\"color\":\"gray\",\"italic\":false,\"text\":\"you have 9 hearts\"}"],custom_name:"{\"color\":\"#5b6ee1\",\"italic\":false,\"text\":\"Health\"}", "minecraft:custom_data": {ui_item: {empty: 1b}}}}

data modify storage ui mask insert 0 value {Slot: 11b, id: "minecraft:stick", "components": {"custom_model_data": 77, lore:["{\"color\":\"gray\",\"italic\":false,\"text\":\"none\"}"],custom_name:"{\"color\":\"#5b6ee1\",\"italic\":false,\"text\":\"pearl\"}", "minecraft:custom_data": {ui_item: {empty: 1b}}}}



execute if entity @p[tag=fly] run data modify storage ui mask insert 0 value {Slot: 18b, id: "minecraft:stick", "components": {"custom_model_data": 78, lore:["{\"color\":\"gray\",\"italic\":false,\"text\":\"none\"}"],custom_name:"{\"color\":\"#5b6ee1\",\"italic\":false,\"text\":\"fly\"}", "minecraft:custom_data": {ui_item: {cmd: "function ui:menu/wizard/slot_select/open {predicate:78}"}}}}

execute if entity @p[tag=slow_fall] run data modify storage ui mask insert 0 value {Slot: 19b, id: "minecraft:stick", "components": {"custom_model_data": 79, lore:["{\"color\":\"gray\",\"italic\":false,\"text\":\"none\"}"],custom_name:"{\"color\":\"#5b6ee1\",\"italic\":false,\"text\":\"slow_fall\"}", "minecraft:custom_data": {ui_item: {cmd: "function ui:menu/wizard/slot_select/open {predicate:79}"}}}}

execute if entity @p[tag=wither] run data modify storage ui mask insert 0 value {Slot: 20b, id: "minecraft:stick", "components": {"custom_model_data": 80, lore:["{\"color\":\"gray\",\"italic\":false,\"text\":\"none\"}"],custom_name:"{\"color\":\"#5b6ee1\",\"italic\":false,\"text\":\"wither\"}", "minecraft:custom_data": {ui_item: {cmd: "function ui:menu/wizard/slot_select/open {predicate:80}"}}}}

execute if entity @p[tag=lightning] run data modify storage ui mask insert 0 value {Slot: 21b, id: "minecraft:stick", "components": {"custom_model_data": 81, lore:["{\"color\":\"gray\",\"italic\":false,\"text\":\"none\"}"],custom_name:"{\"color\":\"#5b6ee1\",\"italic\":false,\"text\":\"lightning\"}", "minecraft:custom_data": {ui_item: {cmd: "function ui:menu/wizard/slot_select/open {predicate:81}"}}}}

execute if entity @p[tag=fireball] run data modify storage ui mask insert 0 value {Slot: 22b, id: "minecraft:stick", "components": {"custom_model_data": 71, lore:["{\"color\":\"gray\",\"italic\":false,\"text\":\"none\"}"],custom_name:"{\"color\":\"#5b6ee1\",\"italic\":false,\"text\":\"fireball\"}", "minecraft:custom_data": {ui_item: {cmd: "function ui:menu/wizard/slot_select/open {predicate:71}"}}}}

execute if entity @p[tag=glow] run data modify storage ui mask insert 0 value {Slot: 23b, id: "minecraft:stick", "components": {"custom_model_data": 72, lore:["{\"color\":\"gray\",\"italic\":false,\"text\":\"none\"}"],custom_name:"{\"color\":\"#5b6ee1\",\"italic\":false,\"text\":\"glow\"}", "minecraft:custom_data": {ui_item: {cmd: "function ui:menu/wizard/slot_select/open {predicate:72}"}}}}

execute if entity @p[tag=ice] run data modify storage ui mask insert 0 value {Slot: 24b, id: "minecraft:stick", "components": {"custom_model_data": 73, lore:["{\"color\":\"gray\",\"italic\":false,\"text\":\"none\"}"],custom_name:"{\"color\":\"#5b6ee1\",\"italic\":false,\"text\":\"ice\"}", "minecraft:custom_data": {ui_item: {cmd: "function ui:menu/wizard/slot_select/open {predicate:73}"}}}}

execute if entity @p[tag=push] run data modify storage ui mask insert 0 value {Slot: 25b, id: "minecraft:stick", "components": {"custom_model_data": 74, lore:["{\"color\":\"gray\",\"italic\":false,\"text\":\"none\"}"],custom_name:"{\"color\":\"#5b6ee1\",\"italic\":false,\"text\":\"push\"}", "minecraft:custom_data": {ui_item: {cmd: "function ui:menu/wizard/slot_select/open {predicate:74}"}}}}



execute if score @p primary matches 81 run data modify storage ui mask insert 0 value {Slot: 5b, id: "minecraft:stick", "components": {"custom_model_data": 81, lore:["{\"color\":\"gray\",\"italic\":false,\"text\":\"none\"}"],custom_name:"{\"color\":\"#5b6ee1\",\"italic\":false,\"text\":\"lightning\"}", "minecraft:custom_data": {ui_item: {empty: 1b}}}}

execute if score @p secondary matches 81 run data modify storage ui mask insert 0 value {Slot: 7b, id: "minecraft:stick", "components": {"custom_model_data": 81, lore:["{\"color\":\"gray\",\"italic\":false,\"text\":\"none\"}"],custom_name:"{\"color\":\"#7b6ee1\",\"italic\":false,\"text\":\"lightning\"}", "minecraft:custom_data": {ui_item: {empty: 1b}}}}