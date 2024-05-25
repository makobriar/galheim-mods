# galheim-mods
Downloadable modpack for da Valheim server. Intended to be a Vanilla+ experience with some added variety, convenience, and quality-of-life features.

# Installation instructions

1. Extract the `galheim-modpack.zip` somewhere, then move all the contents of the `galheim-modpack` folder into your Valheim installation folder.
    - Your game folder (`../Steam/steamapps/common/Valheim/`) should look something like this:  
      :file_folder: BepInEx  
      :file_folder: MonoBleedingEdge  
      :page_facing_up: doorstop_config.ini  
      :page_facing_up: winhttp.dll  
      :cd: valheim.exe  
      ... (other files and folders)
2. Start the game like normal
    - It should start with a command prompt that logs the BepInEx (mod loader) output.
    - If you ever have any problems you can read the output to see what failed. It should be relatively obvious (and even highlighted red)

# What's included?

### :heavy_check_mark: BepInEx
The general purpose modding framework for Valheim. Nothing else would work without this, as it effectively 'injects' our logic in the game.

### :heavy_check_mark: ValheimPlus (Grantapher fork)
An updated and still-maintained "Vanilla+" mod. It adds TONS of functionality, including but not limited to:
- Auto-deposit and auto-pulling for refinery equipment (smelters, furnaces, etc.)
    - Stick a chest directly next to the equipment and the machine will attempt to grab fuel from it and deposit goods back into it
- Larger exploration radius for the map to remove fog of war
- Auto-repair equipment when interacting with a workbench/forge
- Craft from nearby chests
- Build from nearby chests
- No more refueling light sources like torches. Campfires still require wood, however
- Further camera zoom

All of these options and more can be configured in the `/BepInEx/config/valheim_plus.cfg` file. **The one we use for the server has been provided for you.**


### :heavy_check_mark: PlantEasily
Adds snapping and hotkeys for planting; you shouldn't accidentally place crops too close any more!

The keybind for increasing the grid of plants is RIGHT CTRL + ARROW KEYS. As an example RCTRL + → will increase the row by 1, and RCTRL + ↑ will increased the column by 1. Using left and down arrow keys reduce it, of course.

### :heavy_check_mark: PlantEverything
Does what it says. You can now plant berries, thistle, and more! They are a bit expensive but the harvested crop does not go away - it will stay as a 'stem' and continue to regrow over time. The values have been modified (increased) for our convenience, and the `.cfg` file used for this is included in the `/BepInEx/config/` folder.

### :heavy_check_mark: Epic Loot
Adds some variety to equipment in Valheim. They can now drop as different rarities with their own stat bonuses and unique modifiers. Armor that gives you additional movement speed, or weapons that use less stamina.
