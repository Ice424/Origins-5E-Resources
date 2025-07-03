import json
from PIL import Image

def image_overlays():
    file = open("powers.json", "r")
    powers = json.loads(file.read())
    file.close()

    key_activated_overlay = Image.open("testunused/corner_overlay.png", mode="r")
    
    def GetPowers(types):
        for power in powers[types]:
            if power["key_activated"] is True:
                original = Image.open("./Origins-5E-Resources/assets/chill/textures/item/" + types + "/" + power["id"] + ".png", mode="r")
                original = original.convert("RGBA")
                new = Image.alpha_composite(original, key_activated_overlay)
                new.save("./Origins-5E-Resources/assets/chill/textures/item/" + types + "/" + power["id"] + ".png")
                grey = new.convert('LA')
                grey.save("./Origins-5E-Resources/assets/chill/textures/item/" + types + "/" + power["id"] +  "_greyscale.png")



    GetPowers("low")
    GetPowers("high")

    for classes in powers["class"]:
        for types in powers["class"][classes]:
                for power in powers["class"][classes][types]:
                    if power["key_activated"] is True:
                        original = Image.open("./Origins-5E-Resources/assets/chill/textures/item/class/" + classes + "/" + types + "/" + power["id"] + ".png", mode="r")
                        original = original.convert("RGBA")
                        new = Image.alpha_composite(original, key_activated_overlay)
                        new.save("./Origins-5E-Resources/assets/chill/textures/item/class/" + classes + "/" + types + "/" + power["id"] + ".png")
                        grey =new.convert('LA')
                        grey.save("./Origins-5E-Resources/assets/chill/textures/item/class/" + classes + "/" + types + "/" + power["id"] + "_greyscale.png")
