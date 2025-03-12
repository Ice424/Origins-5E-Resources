import os
from pathlib import Path
from PIL import Image


# -b special\lightning.ase -save-as {title}.png


def convert_images():
    ASEPRITE_PATH = "D:/SteamLibrary/steamapps/common/Aseprite/aseprite.exe"
    for path, subdirs, files in os.walk("./aseprite files"):
        for name in files:
            if name != "pallet.ase":
                image = os.path.join(path, name).replace("./", "")
                if path.endswith("unused"):
                    savepath = "test" + path.replace("./aseprite files\\", "").replace("./aseprite files", "")
                else:
                    savepath = "Origins-5E-Resources\\assets\\chill\\textures\\item\\" + \
                        path.replace("./aseprite files\\", "") + "/"

                os.makedirs(os.path.join(savepath), exist_ok=True)
                os.system(ASEPRITE_PATH + " -b \"" + image + "\" -save-as " + savepath + "\\{title}.png")
                if path.endswith("unused"):
                    png = "test" + image.replace("aseprite files\\", "").replace(
                        ".ase", ".png").replace("\\", "/")

                else:
                    png = "Origins-5E-Resources\\assets\\chill\\textures\\item\\" + \
                    image.replace("aseprite files\\", "").replace(
                        ".ase", ".png").replace("\\", "/")
                mg = Image.open(png).convert('LA')
                mg.save(png.replace(os.path.basename(png), Path(png).stem+"_greyscale.png"))

                
convert_images()