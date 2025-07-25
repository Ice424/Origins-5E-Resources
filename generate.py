"""_summary_

Returns:
    _type_: _description_
"""

import os
import json
from pathlib import Path
os.chdir(Path(__file__).parents[1])

RESOURCES = os.path.abspath(
    "./resourcepacks/Origins-5E-Reasources/assets/")

DATA = os.path.abspath(
    "./saves/New World/datapacks/Origins-5E-Data/data/chill/powers")

MODEL = {
    "parent": "minecraft:item/handheld",
    "textures": {
        "layer0": ""
    }
}
num_completed = 0


def key_value_exists(data, target_key, target_value):
    if isinstance(data, dict):
        for key, value in data.items():
            if key == target_key and value == target_value:
                return True
            if key_value_exists(value, target_key, target_value):
                return True
    elif isinstance(data, list):
        for item in data:
            if key_value_exists(item, target_key, target_value):
                return True
    return False


def add_power(powers, category, predicate, directory, group=None, types=None):
    """
    Adds a power entry to the JSON structure if it doesn't already exist.

    Args:
    powers (dict): The JSON structure containing power entries.
    category (str): The category of the power to add.
    predicate (str): The predicate for the power entry.
    directory (str): The directory path of the power entry.
    group (str, optional): The group of the power entry. Defaults to None.
    types (list, optional): The types of the power entry. Defaults to None.
    Returns:
    bool: True if the power was added successfully, False otherwise.
    """
    global num_completed
    directories = ["passive", "special", "high"]

    # Remove primary and secondary.json from the end of the directory if they exist
    if "\\low\\" in directory or "/low/" in directory:
        Id = (Path(directory).parts[-2] + "_" +
              Path(directory).parts[-1]).replace(".json", "")
    elif Path(directory).parts[-2] not in directories:
        Id = Path(directory).parts[-2]
    else:
        Id = Path(directory).stem.lower()
    Id = Id.lower().replace(" ", "_")

    if category in powers:
        if group and category == "class":
            if group in powers["class"] and types in powers["class"][group]:
                target_list = powers["class"][group][types]
            else:
                return False
        else:
            target_list = powers[category]
        if any(item["id"].strip().lower() == Id for item in target_list) or Id == "tag" or Id == "temp":
            return False

        description = "none"
        name = Id
        completed = False
        key_activated = False
        

        with open(directory, 'r') as file:
            try:
                data = json.load(file)
                try:
                    name = data["name"].strip().replace("'s", "\\\\\\'s")
                except KeyError:
                    name = Id.replace("'s", "\\\\\\'s")
                except Exception as e:
                    print(e)
                try:
                    description = data["description"].strip().replace("'s", "\\\\\\'s")

                except KeyError:
                    description = "none"
                except Exception as e:
                    print(e)
                if key_value_exists(data, "key", "key.origins.primary_active") or key_value_exists(data, "key", "key.origins.secondary_active"):
                    key_activated = True

                else:
                    key_activated = False
                if directory.endswith(".json"):
                    completed = True
                    num_completed += 1
                else:
                    with open("./saves/New World/datapacks/Origins-5E-Data/TODO.md", "a") as f:
                        f.write(f"{group} {Id}: {name}\n{description}\n\n")

            except json.JSONDecodeError:
                key_activated = False

                # print(f"Failed to decode JSON file: {directory}")
                pass
            file.close()
        target_list.append({"name": name, "description": description, "id": Id,
                           "predicate": predicate, "key_activated": key_activated, "completed": completed})
        return True


def generate_json():
    predicate = 10

    powers = {
        "high": [],
        "low": [],
        "class": {
            "cleric": {
                "special": [],
                "high": [],
                "passive": []
            },
            "druid": {
                "special": [],
                "high": [],
                "passive": []
            },
            "fighter": {
                "high": [],
                "passive": []
            },
            "rogue": {
                "special": [],
                "high": [],
                "passive": []
            },
            "tank": {
                "special": [],
                "high": [],
                "passive": []
            },
            "wizard": {
                "special": [],
                "high": [],
                "passive": []
            },
        }}
    with open("./saves/New World/datapacks/Origins-5E-Data/TODO.md", "w") as f:
                f.write("##TO DO\n")
    for path, subdirs, files in os.walk(DATA):
        for name in files:
            if os.name == "nt":
                file = (os.path.join(path, name).replace(
                    DATA + "\\", "").replace("\\", "/"))
            else:
                file = (os.path.join(path, name).replace(DATA + "/", ""))
            file = file.split("/")

            if file[0] == "class":
                if add_power(powers, "class", predicate, os.path.join(path, name), group=file[1], types=file[2]):
                    predicate += 1
            else:
                if add_power(powers, file[0], predicate, os.path.join(path, name)):
                    predicate += 1
    print(f"powers completed {num_completed}")

    file = open(os.path.abspath("./resourcepacks/powers.json"), "w", encoding="UTF-8")

    file.write(json.dumps(powers, indent=4))
    file.close()


def generate_models(path):
    file = open("./resourcepacks/powers.json", "r")
    powers = json.loads(file.read())
    file.close()

    def GetPowers(types):
        for power in powers[types]:
            power = power["id"]
            os.makedirs(os.path.join(path, types), exist_ok=True)

            file = open(os.path.join(path, types, power)+".json", "w", encoding="UTF-8")
            out = MODEL
            out["textures"]["layer0"] = "chill:item/" + types + "/" + power
            file.write(json.dumps(out, indent=4))
            file.close()

            file = open(os.path.join(path, types, power) +
                        "_greyscale.json", "w", encoding="UTF-8")
            out = MODEL
            out["textures"]["layer0"] = "chill:item/" + \
                types + "/" + power + "_greyscale"
            file.write(json.dumps(out, indent=4))
            file.close()
    GetPowers("low")
    GetPowers("high")
    for classes in powers["class"]:
        for types in powers["class"][classes]:
            for power in powers["class"][classes][types]:
                power = power["id"]
                try:
                    os.makedirs(os.path.join(path, "class", classes, types))
                except:
                    pass
                out = MODEL
                out["textures"]["layer0"] = "chill:item/class/" + \
                    classes + "/" + types + "/" + power
                file = open(os.path.join(path, "class",
                            classes, types, power)+".json", "w", encoding="UTF-8")
                file.write(json.dumps(out, indent=4))
                file.close()

                out["textures"]["layer0"] = "chill:item/class/" + \
                    classes + "/" + types + "/" + power + "_greyscale"
                file = open(os.path.join(path, "class", classes,
                            types, power)+"_greyscale.json", "w", encoding="UTF-8")
                file.write(json.dumps(out, indent=4))
                file.close()


def generate_tags(path):
    file = open("./resourcepacks/powers.json", "r")
    powers = json.loads(file.read())
    file.close()
    tag = {
        "type": "origins:action_on_callback",
        "entity_action_gained": {
            "type": "origins:execute_command",
            "command": ""
        },
        "entity_action_lost": [],
        "hidden": True
    }
    
    def GetPowers(types):
        for power in powers[types]:
            power = power["id"]
            out["entity_action_lost"].append({
                    "type": "origins:execute_command",
                    "command": "tag @s remove " + power
                })
    

    for classes in powers["class"]:
        out = tag
        out["entity_action_gained"]["command"] = "tag @s add " + classes
        GetPowers("low")
        GetPowers("high")
        try:
            os.makedirs(os.path.join(path, "class", classes, "passive"))
        except:
            pass
        for types in powers["class"][classes]:
            for power in powers["class"][classes][types]:
                power = power["id"]
                out["entity_action_lost"].append({
                    "type": "origins:execute_command",
                    "command": "tag @s remove " + power
                })
        
        out["entity_action_lost"].append({
            "type": "origins:execute_command",
                    "command": "tag @s remove " + classes
        })
        out["entity_action_lost"].append({
            "type": "origins:execute_command",
                    "command": "scoreboard players set @s primary 0"
        })
        out["entity_action_lost"].append({
            "type": "origins:execute_command",
                    "command": "scoreboard players set @s secondary 0"
        })
        out["entity_action_lost"].append({
            "type": "origins:execute_command",
                    "command": "scoreboard players set @s slot_3 0"
        })
        out["entity_action_lost"].append({
            "type": "origins:execute_command",
                    "command": "scoreboard players set @s slot_4 0"
        })
        out["entity_action_lost"].append({
            "type": "origins:execute_command",
                    "command": "power clear @s"
        })
        file = open(os.path.join(path, "class", classes,
                    "passive", "tag")+".json", "w", encoding="UTF-8")
        file.write(json.dumps(out, indent=4))
        file.close()
        out["entity_action_lost"] = []


def generate_predicates():
    file = open("./resourcepacks/powers.json", "r")
    powers = json.loads(file.read())
    file.close()
    out = []

    def GetPowers(types):
        for power in powers[types]:
            out.append({"predicate": {"custom_model_data": power["predicate"]},
                        "model": "chill:" + os.path.join(types, power["id"]).replace("\\", "/")})

    GetPowers("low")
    GetPowers("high")
    for classes in powers["class"]:

        for types in powers["class"][classes]:
            for power in powers["class"][classes][types]:
                out.append({"predicate": {"custom_model_data": power["predicate"]}, "model": "chill:" + os.path.join(
                    "class", classes, types, power["id"]).replace("\\", "/")})

    file = open(
        "./resourcepacks/Origins-5E-Resources/assets/minecraft/models/item/stick.json", "r")
    data = json.load(file)
    file.close()
    to_write = {
        "parent": "minecraft:item/handheld",
        "textures": {
            "layer0": "minecraft:item/stick"
        },
        "overrides": []
    }
    for item_dict in data["overrides"]:
        if item_dict["predicate"]["custom_model_data"] < 10:
            to_write["overrides"].append(item_dict)

    for override in out:
        to_write["overrides"].append(override)

    with open("./resourcepacks/Origins-5E-Resources/assets/minecraft/models/item/stick.json", "w", encoding="UTF-8") as file:
        json.dump(to_write, file, indent=4)
    for item_dict in to_write["overrides"]:
        item_dict["model"] = item_dict["model"] + "_greyscale"

    to_write["textures"]["layer0"] = "minecraft:item/iron_nugget"
    to_write["overrides"] = to_write["overrides"][3:]
    with open("./resourcepacks/Origins-5E-Resources/assets/minecraft/models/item/iron_nugget.json", "w", encoding="UTF-8") as file:
        json.dump(to_write, file, indent=4)


def refactor_predicates():
    file = open("./resourcepacks/powers.json", "r")
    powers = json.loads(file.read())
    file.close()
    predicate = 10

    def GetPowers(types, predicate):
        powers[types].sort(key=lambda x: x["id"])
        for power in powers[types]:
            power["predicate"] = predicate
            predicate += 1
        return predicate

    predicate = GetPowers("low", predicate)
    predicate = GetPowers("high", predicate)

    for classes in powers["class"]:

        for types in powers["class"][classes]:
            powers["class"][classes][types].sort(key=lambda x: x["id"])
            for power in powers["class"][classes][types]:
                power["predicate"] = predicate
                predicate += 1
    print(f"The largest predicate is {predicate}")
    file = open(os.path.abspath("./resourcepacks/powers.json"), "w", encoding="UTF-8")

    file.write(json.dumps(powers, indent=4))
    file.close()


# generate_shop()
