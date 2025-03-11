import os
import json
from pathlib import Path
from PIL import Image
ASEPRITE_PATH = "D:/SteamLibrary/steamapps/common/Aseprite/aseprite.exe"

# -b special\lightning.ase -save-as {title}.png
file = open("powers.json", "r")
POWERS = json.loads(file.read())
file.close()

def GetData(path):
    try: 
        Path(path).parts[5]
    
    except IndexError: 
        print("Unused", Path(path).stem)
        return None

    if Path(path).parts[5] == "class":
        Data = [item for item in POWERS["class"][Path(path).parts[6]][Path(path).parts[7]] if item.get('id')==Path(path).stem]
        if not Data:
            print("No Data for " + Path(path).stem)
            return None
        Data = Data[0]

        Data["Type"] = "class"
        return Data
    elif Path(path).parts[5] == "high":
        Data = [item for item in POWERS[Path(path).parts[5]] if item.get('id')==Path(path).stem]
        if not Data:
            
            print("No Data for " + Path(path).stem)
            return None
        Data = Data[0]
        Data["Type"] = Path(path).parts[5]
        return Data
    elif Path(path).parts[5] == "low":
        Data = {"Type": "low", "key_activated": False, "name": Path(path).stem }

        return Data
    else:
        print("Unknown type: " + Path(path).parts[5])








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
            Data = GetData(png)
            print(Data)
