import os
import shutil
from pathlib import Path
import generate_equipfiles
import generate_shop_slots
import generate_spellbook_slot_select
import generate_spellbook
import generate_unimplemented
import generate_shop_masks
import generate
import image


DATA = os.path.abspath("./saves/New World/datapacks/Origins-5E-Data/data/chill/powers")
#Wipe folders that are going to be regenerated
os.chdir("c:/Users/Ice424/curseforge/minecraft/Instances/Origins 5E Pack/resourcepacks")


shutil.rmtree(os.path.abspath("Origins-5E-Resources/assets/chill/textures/item/class"), ignore_errors=True)
shutil.rmtree(os.path.abspath("Origins-5E-Resources/assets/chill/textures/item/high"), ignore_errors=True)
shutil.rmtree(os.path.abspath("Origins-5E-Resources/assets/chill/textures/item/low"), ignore_errors=True)

os.chdir(Path(__file__).parents[1])
#The holy json file
generate.generate_json()

#Resource pack stuff
generate.refactor_predicates()
generate.generate_models("./resourcepacks/Origins-5E-Resources/assets/chill/models/")
generate.generate_tags(DATA)
generate.generate_predicates()

#.mcfunctions
generate_shop_masks.generate_shop_masks()
generate_equipfiles.generate_equipfiles()
generate_shop_slots.generate_shop_slots()
generate_spellbook_slot_select.generate_spellbook_slot_select()
generate_spellbook.generate_spellbook()

#image handling
os.chdir("c:/Users/Ice424/curseforge/minecraft/Instances/Origins 5E Pack/resourcepacks")
os.system("python aseprite.py")
generate_unimplemented.generate_unimplemented()
image.image_overlays()
