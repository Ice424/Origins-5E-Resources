import json
import os
from pathlib import Path

def generate_spellbook_slot_select():
    os.chdir(Path(__file__).parents[1])

    DATA = os.path.abspath(
        "./saves/New World/datapacks/Origins-5E-Data/data/ui/function/menu")

    file = open("resourcepacks/powers.json", "r")
    powers = json.loads(file.read())
    file.close()
    ClassMenuPredicates = {
        "cleric": 8,
        "druid": 9,
        "fighter": 4,
        "rogue": 10,
        "tank": 11,
        "wizard": 12
    }


    ClassColours = {
        "cleric": "#fbf236",
        "druid": "#99e550",
        "fighter": "#ac3232",
        "rogue": "#403352",
        "tank": "#2c2d51",
        "wizard": "#5b6ee1"
    }
    slot_select_template = 'execute as @a[scores={{ui.id=1..}}] if score @s ui.id = @s ui.id run execute if score @s predicate matches {predicate} run data modify storage ui mask insert 0 value {{Slot: {slot}b, id:\"minecraft:stick\", \"components\": {{\"custom_model_data\": {predicate}, custom_name:\"{{\\"color\\":\\"{color}\\",\\"italic\\":false,\\"text\\":\\"{name}\\"}}\", lore:[\'[{{\"color\":\"gray\",\"italic\":false,\"text\":\"Key set to \"}},{{\"color\":\"gray\",\"italic\":false,\"keybind\":\"key.origins.{key}_active\"}}]\'], \"minecraft:custom_data\": {{ui_item: {{cmd: \"function ui:menu/main/{key}\"}}}}}}}}'


    # generate spellbooks
    out = []
    for classes in powers["class"]:
        for types in powers["class"][classes]:
            for power in powers["class"][classes][types]:
                color = ClassColours[classes]
                if power["key_activated"] is True:
                    out.append(slot_select_template.format(slot=21, key="primary", predicate=power["predicate"], color=color, name = "Primary"))
                    out.append(slot_select_template.format(slot=23, key="secondary", predicate=power["predicate"],  color=color, name = "Secondary"))
        os.makedirs(os.path.join(DATA, f"{classes}/slot_select"), exist_ok=True)
        file = open(os.path.join(DATA, f"{classes}/slot_select/mask.mcfunction"), "w", encoding="UTF-8")
        file.write(f"""data modify storage ui mask set value [{{Slot:0b,id:"minecraft:barrier","components":{{"custom_name": "{{\\"text\\":\\"Back\\", \\"color\\": \\"red\\", \\"italic\\": false}}","minecraft:custom_model_data": {ClassMenuPredicates[classes]}, "minecraft:custom_data":{{ui_item: {{cmd:"function ui:menu/{classes}/spellbook/open"}}}}}}}}, {{Slot:2b,id:"minecraft:acacia_boat","components":{{"custom_name": "{{\\"text\\":\\"\\", \\"color\\": \\"red\\", \\"italic\\": false}}","minecraft:custom_model_data": 1, "minecraft:custom_data":{{ui_item:{{empty:1b}}}}}}}}]""")
        file.write("\n\n")
        file.write("\n\n".join(out))
        file.close()

        file = open(os.path.join(DATA, f"{classes}/slot_select/open.mcfunction"), "w", encoding="UTF-8")
        file.write(f"""$execute as @a[scores={{ui.id=1..}}] if score @s ui.id = @s ui.id run scoreboard players set @s predicate $(predicate)
function ui:menu/{classes}/slot_select/mask
data modify storage ui current set from storage ui mask
execute on passengers run data modify entity @s data.page.mask set value \"function ui:menu/{classes}/slot_select/mask\"""")
        file.close()




    def GetPowers(types):
        out = []
        slot = 9
        for power in powers[types]:
                if power["key_activated"] == True:
                    out.append(slot_select_template.format(slot=21, name = "Primary", key="primary", predicate=power["predicate"], color="dark_gray"    if types == "low" else "dark_purple"))
                    out.append(slot_select_template.format(slot=23, name = "Secondary", key="secondary", predicate=power["predicate"],      color="dark_gray" if types == "low" else"dark_purple"))
        os.makedirs(os.path.join(DATA, f"{types}/slot_select"), exist_ok=True)
        file = open(os.path.join(DATA, f"{types}/slot_select/mask.mcfunction"), "w", encoding="UTF-8")
        file.write(f"""data modify storage ui mask set value [{{Slot:0b,id:"minecraft:barrier","components":{{"custom_name": "{{\\"text\\":\\"Back\\", \\"color\\": \\"red\\", \\"italic\\": false}}","minecraft:custom_model_data": 8, "minecraft:custom_data":{{ui_item: {{cmd:"function ui:menu/{types}/spellbook/open"}}}}}}}}, {{Slot:2b,id:"minecraft:acacia_boat","components":{{"custom_name": "{{\\"text\\":\\"\\", \\"color\\": \\"red\\", \\"italic\\": false}}","minecraft:custom_model_data": 1, "minecraft:custom_data":{{ui_item:{{empty:1b}}}}}}}}]""")
        file.write("\n\n")
        file.write("\n\n".join(out))
        file.close()

        file = open(os.path.join(DATA, f"{types}/slot_select/open.mcfunction"), "w", encoding="UTF-8")
        file.write(f"""$execute as @a[scores={{ui.id=1..}}] if score @s ui.id = @s ui.id run scoreboard players set @s predicate $(predicate)
function ui:menu/{types}/slot_select/mask
data modify storage ui current set from storage ui mask
execute on passengers run data modify entity @s data.page.mask set value \"function ui:menu/{types}/slot_select/mask\"""")
        file.close()


    GetPowers("low")
    GetPowers("high")


