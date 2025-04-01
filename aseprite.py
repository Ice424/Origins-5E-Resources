import os
from pathlib import Path
from PIL import Image
from sys import platform


if platform == "linux" or platform == "linux2":
    ASEPRITE_PATH = "/home/elliotd/.local/share/Steam/steamapps/common/Aseprite/aseprite"
elif platform == "win32":
    if os.getlogin() == "bigfe":
        ASEPRITE_PATH= "C:/Users/bigfe/Documents/bin/aseprite.exe"
    else:
        ASEPRITE_PATH = "D:/SteamLibrary/steamapps/common/Aseprite/aseprite.exe"
# -b special\lightning.ase -save-as {title}.png

def low_power(image, savepath, name):
    os.system(ASEPRITE_PATH + " -b  \"" + image + "\" --palette \"aseprite files/low/pallet_iron.ase\" -save-as " + savepath + "/{title}_1.png")
    os.system(ASEPRITE_PATH + " -b  \"" + image + "\" --palette \"aseprite files/low/pallet_copper.ase\" -save-as " + savepath + "/{title}_2.png")
    os.system(ASEPRITE_PATH + " -b  \"" + image + "\" --palette \"aseprite files/low/pallet_gold.ase\" -save-as " + savepath + "/{title}_3.png")
    os.system(ASEPRITE_PATH + " -b  \"" + image + "\" --palette \"aseprite files/low/pallet_emerald.ase\" -save-as " + savepath + "/{title}_4.png")
    os.system(ASEPRITE_PATH + " -b  \"" + image + "\" --palette \"aseprite files/low/pallet_diamond.ase\" -save-as " + savepath + "/{title}_5.png")
    png = os.path.join(savepath, name.replace("ase", "png"))
    png = "Origins-5E-Resources/assets/chill/textures/item/.//low/" + name.replace(".ase", "_1.png")
    mg = Image.open(png).convert('LA')
    
    mg.save(png.replace(".png", "_greyscale.png"))

def convert_aseprite():
    for path, subdirs, files in os.walk("./aseprite files"):
        for name in files:
            if not "pallet" in name:
                image = (os.path.join(path, name))
                if path.endswith("unused"):
                    savepath = os.path.join("testunused")
                else:
                    savepath = os.path.join("Origins-5E-Resources/assets/chill/textures/item/", image.replace(Path(image).parts[0], "").replace(name, ""))
                if not "low" in path:
                    os.system(ASEPRITE_PATH + " -b \"" + image + "\" -save-as " + savepath + "/{title}.png")
                    png = os.path.join(savepath, name.replace("ase", "png"))
                    if not "menu" in path:
                        mg = Image.open(png).convert('LA')
                        mg.save(png.replace(".png", "_greyscale.png"))
                elif "low" in path:
                    low_power(image, savepath, name)

                
convert_aseprite()