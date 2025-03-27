import os
import shutil
from pathlib import Path
from sys import platform
import generate_equipfiles
import generate_shop_slots
import generate_spellbook_slot_select
import generate_spellbook
import generate_unimplemented
import generate_shop_masks
import generate
import generate_power_buy
import image


originaldir = __file__.replace("main.py", "")
DATA = os.path.abspath("./saves/New World/datapacks/Origins-5E-Data/data/chill/powers")
#Wipe folders that are going to be regenerated
os.chdir(originaldir)


shutil.rmtree(os.path.abspath("Origins-5E-Resources/assets/chill/textures/item/class"), ignore_errors=True)
shutil.rmtree(os.path.abspath("Origins-5E-Resources/assets/chill/textures/item/high"), ignore_errors=True)
shutil.rmtree(os.path.abspath("Origins-5E-Resources/assets/chill/textures/item/low"), ignore_errors=True)
shutil.rmtree(os.path.abspath("Origins-5E-Resources/assets/chill/textures/item/menu"), ignore_errors=True)


shutil.rmtree(os.path.abspath("Origins-5E-Resources/assets/chill/models/class"), ignore_errors=True)
shutil.rmtree(os.path.abspath("Origins-5E-Resources/assets/chill/models/high"), ignore_errors=True)
shutil.rmtree(os.path.abspath("Origins-5E-Resources/assets/chill/models/low"), ignore_errors=True)

os.chdir(Path(__file__).parents[1])
shutil.rmtree(os.path.abspath("./saves/New World/datapacks/Origins-5E-Data/data/ui/function/menu/cleric"), ignore_errors=True)
shutil.rmtree(os.path.abspath("./saves/New World/datapacks/Origins-5E-Data/data/ui/function/menu/druid"), ignore_errors=True)
shutil.rmtree(os.path.abspath("./saves/New World/datapacks/Origins-5E-Data/data/ui/function/menu/fighter"), ignore_errors=True)
shutil.rmtree(os.path.abspath("./saves/New World/datapacks/Origins-5E-Data/data/ui/function/menu/high"), ignore_errors=True)
shutil.rmtree(os.path.abspath("./saves/New World/datapacks/Origins-5E-Data/data/ui/function/menu/low"), ignore_errors=True)
shutil.rmtree(os.path.abspath("./saves/New World/datapacks/Origins-5E-Data/data/ui/function/menu/rogue"), ignore_errors=True)
shutil.rmtree(os.path.abspath("./saves/New World/datapacks/Origins-5E-Data/data/ui/function/menu/tank"), ignore_errors=True)
shutil.rmtree(os.path.abspath("./saves/New World/datapacks/Origins-5E-Data/data/ui/function/menu/wizard"), ignore_errors=True)

#The holy json file
#generate.generate_json()

#if platform == "linux" or platform == "linux2":
#    pass
#elif platform == "win32":
#    generate.generate_json()
generate.generate_json()
#Resource pack stuff
generate.refactor_predicates()
generate.generate_models("./resourcepacks/Origins-5E-Resources/assets/chill/models/")
generate.generate_tags(DATA)
generate.generate_predicates()

#.mcfunctions
generate_power_buy.shop_mask()
generate_power_buy.shop_active()
generate_shop_masks.generate_shop_masks()
generate_equipfiles.generate_equipfiles()
generate_shop_slots.generate_shop_slots()
generate_spellbook_slot_select.generate_spellbook_slot_select()
generate_spellbook.generate_spellbook()

#image handling
os.chdir(originaldir)
os.system("python aseprite.py")
generate_unimplemented.generate_unimplemented(originaldir)
image.image_overlays()
