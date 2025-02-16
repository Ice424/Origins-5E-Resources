data modify storage ui mask insert 0 value {Slot: 9b, id: "minecraft:stick", "components": {"custom_model_data": 24, lore:["{\"color\":\"gray\",\"italic\":false,\"text\":\"none\"}"],custom_name:"{\"color\":\"#99e550\",\"italic\":false,\"text\":\"animal\"}", "minecraft:custom_data": {ui_item: {empty: 1b}}}}

data modify storage ui mask insert 0 value {Slot: 10b, id: "minecraft:stick", "components": {"custom_model_data": 25, lore:["{\"color\":\"gray\",\"italic\":false,\"text\":\"none\"}"],custom_name:"{\"color\":\"#99e550\",\"italic\":false,\"text\":\"heal\"}", "minecraft:custom_data": {ui_item: {empty: 1b}}}}

data modify storage ui mask insert 0 value {Slot: 11b, id: "minecraft:stick", "components": {"custom_model_data": 26, lore:["{\"color\":\"gray\",\"italic\":false,\"text\":\"none\"}"],custom_name:"{\"color\":\"#99e550\",\"italic\":false,\"text\":\"health\"}", "minecraft:custom_data": {ui_item: {empty: 1b}}}}

data modify storage ui mask insert 0 value {Slot: 12b, id: "minecraft:stick", "components": {"custom_model_data": 27, lore:["{\"color\":\"gray\",\"italic\":false,\"text\":\"none\"}"],custom_name:"{\"color\":\"#99e550\",\"italic\":false,\"text\":\"vegetarian\"}", "minecraft:custom_data": {ui_item: {empty: 1b}}}}



execute if entity @p[tag=animal_control] run data modify storage ui mask insert 0 value {Slot: 18b, id: "minecraft:stick", "components": {"custom_model_data": 28, lore:["{\"color\":\"gray\",\"italic\":false,\"text\":\"none\"}"],custom_name:"{\"color\":\"#99e550\",\"italic\":false,\"text\":\"animal_control\"}", "minecraft:custom_data": {ui_item: {cmd: "function ui:menu/druid/slot_select/open {predicate:28}"}}}}

execute if entity @p[tag=bone_meal] run data modify storage ui mask insert 0 value {Slot: 19b, id: "minecraft:stick", "components": {"custom_model_data": 29, lore:["{\"color\":\"gray\",\"italic\":false,\"text\":\"none\"}"],custom_name:"{\"color\":\"#99e550\",\"italic\":false,\"text\":\"bone_meal\"}", "minecraft:custom_data": {ui_item: {cmd: "function ui:menu/druid/slot_select/open {predicate:29}"}}}}

execute if entity @p[tag=freeze] run data modify storage ui mask insert 0 value {Slot: 20b, id: "minecraft:stick", "components": {"custom_model_data": 30, lore:["{\"color\":\"gray\",\"italic\":false,\"text\":\"none\"}"],custom_name:"{\"color\":\"#99e550\",\"italic\":false,\"text\":\"freeze\"}", "minecraft:custom_data": {ui_item: {cmd: "function ui:menu/druid/slot_select/open {predicate:30}"}}}}

execute if entity @p[tag=skulk] run data modify storage ui mask insert 0 value {Slot: 21b, id: "minecraft:stick", "components": {"custom_model_data": 31, lore:["{\"color\":\"gray\",\"italic\":false,\"text\":\"none\"}"],custom_name:"{\"color\":\"#99e550\",\"italic\":false,\"text\":\"skulk\"}", "minecraft:custom_data": {ui_item: {cmd: "function ui:menu/druid/slot_select/open {predicate:31}"}}}}

execute if entity @p[tag=speed] run data modify storage ui mask insert 0 value {Slot: 22b, id: "minecraft:stick", "components": {"custom_model_data": 32, lore:["{\"color\":\"gray\",\"italic\":false,\"text\":\"none\"}"],custom_name:"{\"color\":\"#99e550\",\"italic\":false,\"text\":\"speed\"}", "minecraft:custom_data": {ui_item: {cmd: "function ui:menu/druid/slot_select/open {predicate:32}"}}}}

execute if entity @p[tag=arrows] run data modify storage ui mask insert 0 value {Slot: 23b, id: "minecraft:stick", "components": {"custom_model_data": 20, lore:["{\"color\":\"gray\",\"italic\":false,\"text\":\"none\"}"],custom_name:"{\"color\":\"#99e550\",\"italic\":false,\"text\":\"arrows\"}", "minecraft:custom_data": {ui_item: {cmd: "function ui:menu/druid/slot_select/open {predicate:20}"}}}}

execute if entity @p[tag=poison] run data modify storage ui mask insert 0 value {Slot: 24b, id: "minecraft:stick", "components": {"custom_model_data": 21, lore:["{\"color\":\"gray\",\"italic\":false,\"text\":\"none\"}"],custom_name:"{\"color\":\"#99e550\",\"italic\":false,\"text\":\"poison\"}", "minecraft:custom_data": {ui_item: {cmd: "function ui:menu/druid/slot_select/open {predicate:21}"}}}}

execute if entity @p[tag=underwater] run data modify storage ui mask insert 0 value {Slot: 25b, id: "minecraft:stick", "components": {"custom_model_data": 22, lore:["{\"color\":\"gray\",\"italic\":false,\"text\":\"none\"}"],custom_name:"{\"color\":\"#99e550\",\"italic\":false,\"text\":\"underwater\"}", "minecraft:custom_data": {ui_item: {cmd: "function ui:menu/druid/slot_select/open {predicate:22}"}}}}

execute if entity @p[tag=wall_climb] run data modify storage ui mask insert 0 value {Slot: 26b, id: "minecraft:stick", "components": {"custom_model_data": 23, lore:["{\"color\":\"gray\",\"italic\":false,\"text\":\"none\"}"],custom_name:"{\"color\":\"#99e550\",\"italic\":false,\"text\":\"wall_climb\"}", "minecraft:custom_data": {ui_item: {cmd: "function ui:menu/druid/slot_select/open {predicate:23}"}}}}





