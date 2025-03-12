import json
import re
import os
from PIL import Image, ImageDraw, ImageFont, ImageOps

def generate_unimplemented():
    done = 0
    os.chdir("c:\\Users\\Ice424\\curseforge\\minecraft\\Instances\\Origins 5E Pack\\resourcepacks")
    file = open("powers.json", "r")
    powers = json.loads(file.read())
    file.close()

    font = ImageFont.truetype("./testunused/Monocraft.ttc", size=9)


    def GetPowers(types, done):
        for power in powers[types]:
            os.makedirs("./Origins-5E-Resources/assets/chill/textures/item/" + types + "/", exist_ok=True)
            if os.path.isfile("./Origins-5E-Resources/assets/chill/textures/item/" + types + "/" + power["id"] + ".png"):
                done += 1
            else:
                image = Image.open("./testunused/unimplemented.png")
                draw = ImageDraw.Draw(image)
                draw.text((1,1), '\n'.join(re.findall('.{1,%i}' % 5, power["id"])), font=font)
                image.save("./Origins-5E-Resources/assets/chill/textures/item/" + types + "/" + power["id"] + ".png")
            if os.path.isfile("./Origins-5E-Resources/assets/chill/textures/item/" + types + "/" + power["id"] + "_greyscale.png"):
                pass
            else:
                image = Image.open("./testunused/unimplemented.png")
                draw = ImageDraw.Draw(image)
                draw.text((1,1), '\n'.join(re.findall('.{1,%i}' % 5, power["id"])), font=font)
                image = ImageOps.grayscale(image)
                image.save("./Origins-5E-Resources/assets/chill/textures/item/" + types + "/" + power["id"] + "_greyscale.png")
        return done

    done = GetPowers("low", done)
    done = GetPowers("high", done)

    for classes in powers["class"]:
        out = []
        for types in powers["class"][classes]:
            for power in powers["class"][classes][types]:
                os.makedirs("./Origins-5E-Resources/assets/chill/textures/item/class/" + classes +"/"+ types + "/", exist_ok=True)
                if os.path.isfile("./Origins-5E-Resources/assets/chill/textures/item/class/" + classes +"/"+ types + "/" + power["id"] + ".png"):
                    done += 1
                else:

                    image = Image.open("./testunused/unimplemented.png")
                    draw = ImageDraw.Draw(image)
                    draw.text((1,1), '\n'.join(re.findall('.{1,%i}' % 5, power["id"])), font=font)
                    image.save("./Origins-5E-Resources/assets/chill/textures/item/class/" + classes + "/" + types + "/" + power["id"] + ".png")
                if os.path.isfile("./Origins-5E-Resources/assets/chill/textures/item/class/" + classes +"/"+ types + "/" + power["id"] + "_greyscale.png"):
                    pass
                else:
                    image = Image.open("./testunused/unimplemented.png")
                    draw = ImageDraw.Draw(image)
                    draw.text((1,1), '\n'.join(re.findall('.{1,%i}' % 5, power["id"])), font=font)
                    image = ImageOps.grayscale(image)
                    image.save("./Origins-5E-Resources/assets/chill/textures/item/class/" + classes + "/" + types + "/" + power["id"] + "_greyscale.png")
    print("Textures Competed", done)

