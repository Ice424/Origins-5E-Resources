import os
from pathlib import Path
from PIL import Image
from sys import platform


if platform == "linux" or platform == "linux2":
    ASEPRITE_PATH = "/home/elliotd/.local/share/Steam/steamapps/common/Aseprite/aseprite"
elif platform == "win32":
    if os.getlogin() == "bigfe":
        ASEPRITE_PATH= "C:/Users/bigfe/Documents/bin/aseprite.exe"
    elif os.getlogin() == "negre":
        ASEPRITE_PATH = "D:/IsaacMods/Aseprite/Aseprite.exe"
    else:
        ASEPRITE_PATH = "D:/SteamLibrary/steamapps/common/Aseprite/aseprite.exe"
# -b special\lightning.ase -save-as {title}.png

def low_power(image, savepath, name):
    os.system(ASEPRITE_PATH + " -b  \"" + image + "\" --palette \"aseprite files/low/pallet_iron.ase\" -save-as " + savepath + "/{title}_1.png")
    os.system(ASEPRITE_PATH + " -b  \"" + image + "\" --palette \"aseprite files/low/pallet_copper.ase\" -save-as " + savepath + "/{title}_2.png")
    os.system(ASEPRITE_PATH + " -b  \"" + image + "\" --palette \"aseprite files/low/pallet_gold.ase\" -save-as " + savepath + "/{title}_3.png")
    os.system(ASEPRITE_PATH + " -b  \"" + image + "\" --palette \"aseprite files/low/pallet_emerald.ase\" -save-as " + savepath + "/{title}_4.png")
    os.system(ASEPRITE_PATH + " -b  \"" + image + "\" --palette \"aseprite files/low/pallet_diamond.ase\" -save-as " + savepath + "/{title}_5.png")
    
    os.system(ASEPRITE_PATH + " -b  \"" + image + "\"  -save-as " + "testunused" + "/{title}_1.png")
    png = os.path.join(savepath, name.replace(".ase", "_1_greyscale.png"))
    img = Image.open("testunused\\" + name.replace(".ase", "_1.png")).convert('LA')
    img.save(png)

def convert_aseprite():
    for path, subdirs, files in os.walk("./aseprite files"):
        for name in files:
            if not "pallet" in name:
                image = (os.path.join(path, name))
                if path.endswith("unused"):
                    savepath = os.path.join("testunused")
                else:
                    savepath = os.path.join("Origins-5E-Resources/assets/chill/textures/item/", image.replace(Path(image).parts[0], "").replace(name, ""))
                
                if "low" in path and name != "xp_xp.ase":
                    low_power(image, savepath, name)
                elif "bars" in path:
                    os.system(ASEPRITE_PATH + " --layer \"Layer 1\" -b \"" + image + "\" -save-as " + savepath + "/{title}.png")
                else:
                    os.system(ASEPRITE_PATH + " -b \"" + image + "\" -save-as " + savepath + "/{title}.png")
                    png = os.path.join(savepath, name.replace("ase", "png"))
                    if not "menu" in path:
                        mg = Image.open(png).convert('LA')
                        mg.save(png.replace(".png", "_greyscale.png"))
                    

def Check_Power(power_path):
    os.chdir(Path(__file__).parents[1])
    DATA = os.path.abspath("./saves/New World/datapacks/Origins-5E-Data/data/chill/powers")
    if os.path.exists(os.path.join(DATA, power_path)) or os.path.exists(os.path.join(DATA, power_path + ".json")):
        return True
    else:
        return False





def Validate(Data):
    original_dir = __file__.replace("aseprite.py", "")
    os.chdir(original_dir)
    import click
    valid = True

    for path, subdirs, files in os.walk("./aseprite files"):
        for name in files:
            if not "pallet" in name and not path.endswith("unused") and not path.endswith("bars"):
                if name.endswith(".aseprite"):
                    if click.confirm(f"Would you like to convert {name} to ase?", default=True):
                        os.rename(os.path.join(path, name), os.path.join(path, name.replace(".aseprite", ".ase")))
                        name = name.replace(".ase", ".aseprite")

                if not name.endswith(".ase"):
                    print(f"{name} is not an ASE file")
                    valid = False
                if "menu" not in path:
                    if name != "xp_xp.ase":
                        power_path = Path(os.path.join(path, Path(name).stem)).parts[1:]
                        power_path = "/".join(power_path)
                        if not Check_Power(power_path):
                            valid = False
                            print(f"{name} is not a valid power")
                        os.chdir(original_dir)
    if valid:
        print("All textures are valid converting...")
        convert_aseprite()
    else:
        print("Some textures are invalid, NOT CONVERTING, please check the logs for more information.")

       



                    
                    

                        
                
                        



