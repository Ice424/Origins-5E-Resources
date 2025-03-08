import json
import re
import os
from PIL import Image, ImageDraw, ImageFont, ImageOps

file = open("powers.json", "r")
powers = json.loads(file.read())
file.close()

font = ImageFont.truetype("./testunused/Monocraft.ttc", size=9)


def GetPowers(types):
    for power in powers[types]:
        os.makedirs("./Origins-5E-Resources/assets/chill/textures/item/" + types + "/", exist_ok=True)
        if os.path.isfile("./Origins-5E-Resources/assets/chill/textures/item/" + types + "/" + power["id"] + ".png"):
            print(power["id"])
        else:
            image = Image.open("./testunused/unimplemented.png")
            draw = ImageDraw.Draw(image)
            draw.text((1,1), '\n'.join(re.findall('.{1,%i}' % 5, power["id"])), font=font)
            image.save("./Origins-5E-Resources/assets/chill/textures/item/" + types + "/" + power["id"] + ".png")
        if os.path.isfile("./Origins-5E-Resources/assets/chill/textures/item/" + types + "/" + power["id"] + "_greyscale.png"):
            print(power["id"])
        else:
            image = Image.open("./testunused/unimplemented.png")
            draw = ImageDraw.Draw(image)
            draw.text((1,1), '\n'.join(re.findall('.{1,%i}' % 5, power["id"])), font=font)
            image = ImageOps.grayscale(image)
            image.save("./Origins-5E-Resources/assets/chill/textures/item/" + types + "/" + power["id"] + "_greyscale.png")

GetPowers("low")
GetPowers("high")

for classes in powers["class"]:
    out = []
    for types in powers["class"][classes]:
        for power in powers["class"][classes][types]:
            os.makedirs("./Origins-5E-Resources/assets/chill/textures/item/class/" + classes +"/"+ types + "/", exist_ok=True)
            if os.path.isfile("./Origins-5E-Resources/assets/chill/textures/item/class/" + classes +"/"+ types + "/" + power["id"] + ".png"):
                print(power["id"])
            else:
                
                image = Image.open("./testunused/unimplemented.png")
                draw = ImageDraw.Draw(image)
                draw.text((1,1), '\n'.join(re.findall('.{1,%i}' % 5, power["id"])), font=font)
                image.save("./Origins-5E-Resources/assets/chill/textures/item/class/" + classes + "/" + types + "/" + power["id"] + ".png")
            if os.path.isfile("./Origins-5E-Resources/assets/chill/textures/item/class/" + classes +"/"+ types + "/" + power["id"] + "_greyscale.png"):
                print(power["id"])
            else:
                image = Image.open("./testunused/unimplemented.png")
                draw = ImageDraw.Draw(image)
                draw.text((1,1), '\n'.join(re.findall('.{1,%i}' % 5, power["id"])), font=font)
                image = ImageOps.grayscale(image)
                image.save("./Origins-5E-Resources/assets/chill/textures/item/class/" + classes + "/" + types + "/" + power["id"] + "_greyscale.png")

