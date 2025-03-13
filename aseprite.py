import os
from pathlib import Path
from PIL import Image


# -b special\lightning.ase -save-as {title}.png


def convert_aseprite():
    ASEPRITE_PATH = "aseprite"
    for path, subdirs, files in os.walk("./aseprite files"):
        for name in files:
            if name != "pallet.ase":
                image = (os.path.join(path, name))
                if path.endswith("unused"):
                    savepath = os.path.join("testunused")
                else:
                    savepath = os.path.join("Origins-5E-Resources/assets/chill/textures/item/", image.replace(Path(image).parts[0], "").replace(name, ""))
                os.system(ASEPRITE_PATH + " -b \"" + image + "\" -save-as " + savepath + "/{title}.png")

                png = os.path.join(savepath, name.replace("ase", "png"))
                print(png)
                mg = Image.open(png).convert('LA')
                mg.save(png.replace(".png", "_greyscale.png"))
convert_aseprite()