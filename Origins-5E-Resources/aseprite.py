import os
from pathlib import Path
from PIL import Image
ASEPRITE_PATH = "D:/SteamLibrary/steamapps/common/Aseprite/aseprite.exe"

# -b special\lightning.ase -save-as {title}.png


for path, subdirs, files in os.walk("./aseprite files"):
    for name in files:
        if name != "pallet.ase":
            image = os.path.join(path, name).replace("./", "")
            if path.endswith("unused"):
                savepath = "test" + path.replace("./aseprite files\\", "").replace("./aseprite files", "")
            else:
                savepath = "assets\\chill\\textures\\" + path.replace("./aseprite files\\", "") + "/"
            print(savepath)
            os.makedirs(os.path.join(savepath), exist_ok=True)
            os.system(ASEPRITE_PATH + " -b \"" + image + "\" -save-as " + savepath + "\\{title}.png")
            if path.endswith("unused"):
                png = "test"
                
            else:
                png = "assets\\chill\\textures\\" + \
                image.replace("aseprite files\\", "").replace(
                    ".ase", ".png").replace("\\", "/")
            print(png)
            mg = Image.open(png).convert('LA')
            mg.save(png.replace(os.path.basename(png), Path(png).stem+"_greyscale.png"))
