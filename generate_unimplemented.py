import json
import os
import shutil

file = open("powers.json", "r")
powers = json.loads(file.read())
file.close()


def GetPowers(types):
    for power in powers[types]:
        if os.path.isfile("./Origins-5E-Resources/assets/chill/textures/" + types + "/" + power["id"] + ".png"):
            print(power["id"])
        else:
            if "greyscale" in power["id"]:
                shutil.copy("testunused/unimplemented_grey.png", "./Origins-5E-Resources/assets/chill/textures/" + types + "/" + power["id"] + ".png")
            else:
                shutil.copy("testunused/unimplemented.png", "./Origins-5E-Resources/assets/chill/textures/" + types + "/" + power["id"] + ".png")



GetPowers("low")
GetPowers("high")

for classes in powers["class"]:
    out = []
    for types in powers["class"][classes]:
        for power in powers["class"][classes][types]:
            if os.path.isfile("./Origins-5E-Resources/assets/chill/textures/class/" + classes +"/"+ types + "/" + power["id"] + ".png"):
                print(power["id"])
            else:
                if "greyscale" in power["id"]:
                    shutil.copy("testunused/unimplemented_grey.png", "./Origins-5E-Resources/assets/chill/textures/class/" +
                                classes + "/" + types + "/" + power["id"] + ".png")
                else:
                    shutil.copy("testunused/unimplemented.png", "./Origins-5E-Resources/assets/chill/textures/class/" +
                                classes + "/" + types + "/" + power["id"] + ".png")

