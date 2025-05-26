import json
import os
from pathlib import Path

def shop_active():
    os.chdir(Path(__file__).parents[1])
    DATA = os.path.abspath(
        "./saves/New World/datapacks/Origins-5E-Data/data/ui/function/menu")
    file = open("resourcepacks/powers.json", "r")
    powers = json.loads(file.read())
    file.close()

    template = "execute if score @p predicate matches {predicate} run scoreboard players set @p activated 1"
    out = []

    def GetPowers(types):
        for power in powers[types]:
            if power["key_activated"] is True:
                out.append(template.format(predicate = power["predicate"]))



    GetPowers("low")
    GetPowers("high")

    for classes in powers["class"]:
        for types in powers["class"][classes]:
            if types != "passive":
                for power in powers["class"][classes][types]:
                    if power["key_activated"] is True:
                        out.append(template.format(predicate = power["predicate"]))
    file = open(os.path.join(DATA, "main", "shop_confirm", "active.mcfunction"), "w", encoding="UTF-8")
    file.write("scoreboard players set @p activated 0\n\n")
    file.write("\n".join(out))
    file.close()

def shop_mask():
    out = []
    out.append('data modify storage ui mask set value [{Slot:0b,id:"minecraft:barrier","components":{"custom_name": "{\\"text\\":\\"Back\\", \\"color\\": \\"red\\", \\"italic\\": false}","minecraft:custom_model_data": 7, "minecraft:custom_data":{ui_item: {cmd:"function ui:menu/main/shop/open_after_buy"}}}}, {Slot:2b,id:"minecraft:acacia_boat","components":{"custom_name": "{\\"text\\":\\"\\", \\"color\\": \\"red\\", \\"italic\\": false}","minecraft:custom_model_data": 2, "minecraft:custom_data":{ui_item:{empty:1b}}}}]')
    out.append('data modify storage ui mask insert 0 value {Slot: 23b, id:"minecraft:acacia_boat", "components": {"custom_model_data": 4, custom_name:"{\\"color\\":\\"red\\",\\"italic\\":false,\\"text\\":\\"No\\"}", "minecraft:custom_data": {ui_item: {cmd: "function ui:menu/main/shop/open_after_buy"}}}}')
    out.append("function ui:menu/main/shop_confirm/active")

    os.chdir(Path(__file__).parents[1])
    DATA = os.path.abspath(
        "./saves/New World/datapacks/Origins-5E-Data/data/ui/function/menu")
    file = open("resourcepacks/powers.json", "r", encoding="UTF-8")
    powers = json.loads(file.read())
    file.close()

    power_display_template = 'execute if score @p predicate matches {predicate} run data modify storage ui mask insert 0 value {{Slot: {slot}b, id: "minecraft:stick", "components": {{"custom_model_data": {predicate}, lore:["{{\\"color\\":\\"gray\\",\\"italic\\":false,\\"text\\":\\"{description}\\"}}","{{\\"color\\":\\"dark_aqua\\",\\"font\\":\\"chill:essence\\",\\"italic\\":false,\\"text\\":\\"{cost} Θ\\"}}"],custom_name:"{{\\"color\\":\\"{color}\\",\\"italic\\":false,\\"text\\":\\"{name}\\"}}", "minecraft:custom_data": {{ui_item: {{empty: 1b}}}}}}}}'
    
    yes_button_template = 'execute if score @p predicate matches {predicate} run data modify storage ui mask insert 0 value {{Slot: 21b, id:"minecraft:acacia_boat", "components": {{"custom_model_data": 3, custom_name:"{{\\"color\\":\\"green\\",\\"italic\\":false,\\"text\\":\\"Yes\\"}}", "minecraft:custom_data": {{ui_item: {{cmd: "function ui:menu/main/shop_confirm/buy_power {{cost:{cost},path:\\"{path}\\",id:{id}}}"}}}}}}}}'
    
    ClassColours = {
        "cleric": "#fbf236",
        "druid": "#99e550",
        "fighter": "#ac3232",
        "rogue": "#121212",
        "tank": "#2c2d51",
        "wizard": "#5b6ee1"
    }

    def GetPowers(types):
        for power in powers[types]:
            if types == "low":
                out.append(power_display_template.format(predicate=power["predicate"], name=power["name"], description=power["description"], slot=13, color="dark_gray", cost="5"))
                if power["key_activated"] is True:
                    out.append(yes_button_template.format(predicate=power["predicate"], cost=5, id=power["id"], path="blank"))
                else:
                    if power["id"] == "xp_xp":
                        out.append(yes_button_template.format(predicate=power["predicate"], cost=5, id=power["id"], path=f"low/xp/xp"))
                    else:
                        out.append(yes_button_template.format(predicate=power["predicate"], cost=5, id=power["id"], path=f"low/{power["id"][:-2]}/{power["id"][-1]}"))
                    
            elif types == "high":
                out.append(power_display_template.format(predicate=power["predicate"], name=power["name"], description=power["description"], slot=13, color="dark_purple", cost="10"))
                if power["key_activated"] is True:
                    out.append(yes_button_template.format(predicate=power["predicate"], cost=10, id=power["id"],  path="blank"))
                else:
                    out.append(yes_button_template.format(predicate=power["predicate"], cost=10, id=power["id"], path=f"high/{power["id"]}"))
                    





    GetPowers("low")
    GetPowers("high")



    for classes in powers["class"]:
        for types in powers["class"][classes]:
                for power in powers["class"][classes][types]:
                    color = ClassColours[classes]
                    if types != "passive":
                        if types == "high":
                            out.append(power_display_template.format(predicate=power["predicate"], name=power["name"], description=power["description"],   slot=13, color=color, cost="15"))
                            if power["key_activated"] is True:
                                out.append(yes_button_template.format(predicate=power["predicate"], cost=15, id=power["id"], path="blank"))
                            else:
                                out.append(yes_button_template.format(predicate=power["predicate"], cost=15, id=power["id"],  path=f"class/{classes}/high/{power["id"]}"))
                        else:
                            out.append(power_display_template.format(predicate=power["predicate"], name=power["name"], description=power["description"],  slot=13, color=color, cost="20"))
                            if power["key_activated"] is True:
                                out.append(yes_button_template.format(predicate=power["predicate"], cost=20, id=power["id"], path="blank"))
                            else:
                                out.append(yes_button_template.format(predicate=power["predicate"], cost=20, id=power["id"],  path=f"class/{classes}/special/{power["id"]}"))


    file = open(os.path.join(DATA, "main", "shop_confirm", "mask.mcfunction"), "w",encoding="UTF-8")
    file.write("\n\n".join(out))
    file.close()

