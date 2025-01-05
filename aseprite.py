import os
from pathlib import Path
from PIL import Image
ASEPRITE_PATH = "D:/SteamLibrary/steamapps/common/Aseprite/aseprite.exe"

# -b special\lightning.ase -save-as {title}.png


for path, subdirs, files in os.walk("./aseprite files"):
    for name in files:
        if name != "pallet.ase":
            image = os.path.join(path, name).replace("./", "")
            savepath = path.replace(
                "./aseprite files\\", "").replace("./aseprite files", "")
            os.makedirs(os.path.join("test", savepath), exist_ok=True)
            os.system(ASEPRITE_PATH + " -b \"" + image +
                      "\" -save-as test\\"+savepath+"\\{title}.png")
            png = "test/" + \
                image.replace("aseprite files\\", "").replace(
                    ".ase", ".png").replace("\\", "/")
            mg = Image.open(png).convert('LA')
            mg.save(png.replace(os.path.basename(png), Path(png).stem+"_grayscale.png"))
