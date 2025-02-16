"""_summary_

Returns:
    _type_: _description_
"""

import os
import json
from pathlib import Path
os.chdir(Path(__file__).parents[2])

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


    # Remove primary and secondary.json from the end of the directory if they exist
    if directory.endswith("primary.json") or directory.endswith("secondary.json"):
        directory = directory.replace(
            "primary.json", "").replace("secondary.json", "")

    if "\\low\\" in directory:
        Id = Path(directory).parts[-2] + "_"+ Path(directory).parts[-1]
        print(directory)
    else:
        Id = Path(directory).stem.lower()

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
        name = Path(directory).stem.lower()
        if os.path.isdir(directory):
            with open(os.path.join(directory, "primary.json"), 'r') as file:
                data = json.load(file)
                try:
                    name = data["name"].strip()
                except KeyError:
                    name = Path(directory).stem.lower()
                except Exception as e:
                    print(e)
                try:
                    description = data["description"].strip()
                except KeyError:
                    description = "none"
                except Exception as e:
                    print(e)
            target_list.append({"name": name, "description": description, "id": Id, "predicate": predicate, "key_activated": True})
            target_list.append({"name": name, "description": description, "id": Id+"_greyscale", "predicate": predicate+1000, "key_activated": True})
            return True
        else:
            with open(directory, 'r') as file:
                try:
                    data = json.load(file)
                    try:
                        name = data["name"].strip()
                    except KeyError:
                        name = Path(directory).stem.lower()
                    except Exception as e:
                        print(e)
                    try:
                        description = data["description"].strip()
                    except KeyError:
                        description = "none"
                    except Exception as e:
                        print(e)
                except json.JSONDecodeError:
                    print(f"Failed to decode JSON file: {directory}")
                file.close()

            target_list.append({"name": name, "description": description, "id": Id, "predicate": predicate, "key_activated": False})
            target_list.append({"name": name, "description": description, "id": Id+"_greyscale", "predicate": predicate+1000, "key_activated": False})
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

    file = open(os.path.abspath(
        "./resourcepacks/Origins-5E-Resources/powers.json"), "w")

    file.write(json.dumps(powers, indent=4))
    file.close()
    print(f"The largest predicate is {predicate}")


def generate_models(path):
    file = open("./resourcepacks/Origins-5E-Resources/powers.json", "r")
    powers = json.loads(file.read())
    file.close()

    def GetPowers(types):
        for power in powers[types]:
            power = power["id"]
            os.makedirs(os.path.join(path, types), exist_ok=True)

            file = open(os.path.join(path, types, power)+".json", "w")
            out = MODEL
            out["textures"]["layer0"] = "chill:" + types + "/" + power
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
                out["textures"]["layer0"] = "chill:class/" + \
                    classes + "/" + types + "/" + power
                file = open(os.path.join(path, "class",
                            classes, types, power)+".json", "w")
                file.write(json.dumps(out, indent=4))
                file.close()


def generate_tags(path):
    file = open("./resourcepacks/Origins-5E-Resources/powers.json", "r")
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
    out = tag
    for classes in powers["class"]:

        for types in powers["class"][classes]:
            out["entity_action_gained"]["command"] = "tag @s add " + classes
            for power in powers["class"][classes][types]:
                power = power["id"]
                out["entity_action_lost"].append({
                    "type": "origins:execute_command",
                    "command": "tag @s remove " + power
                })
            try:
                os.makedirs(os.path.join(path, "class", classes, "passive"))
            except:
                pass
        file = open(os.path.join(path, "class", classes,
                    "passive", "tag")+".json", "w")
        file.write(json.dumps(out, indent=4))
        file.close()
        out["entity_action_lost"] = []


def generate_predicates():
    file = open("./resourcepacks/Origins-5E-Resources/powers.json", "r")
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

    with open("./resourcepacks/Origins-5E-Resources/assets/minecraft/models/item/stick.json", "w") as file:
        json.dump(to_write, file, indent=4)


generate_json()
#
generate_models(
    "./resourcepacks/Origins-5E-Resources/assets/chill/models/")

generate_tags(DATA)

generate_predicates()

# generate_shop()
