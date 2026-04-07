eadme · MD
Copy

# RPG Character Manager - Enhanced Edition
 
![Image of code while running](src\rpg_manager.png)

A terminal-based RPG character management system with data visualization, statistical analysis, and random content generation. The program lets you build and manage a full roster of characters, track their attributes, skills, and inventory, and now includes charts, pandas-powered stat analysis, and Faker-generated backstories and quests.
 
## How to Use
 
1. Run `main.py` from inside the project folder.
2. Use the numbered menu to navigate between all features.
3. Add characters manually or generate random ones using the Random Generator.
4. Manage each character's skills, inventory, and attributes through their dedicated menus.
5. Use Character Visualization to generate radar charts and bar graphs for any character.
6. Use Statistical Analysis to view roster-wide stats, filter by class, or sort by any attribute.
7. Use Data Management to export your roster to CSV or import characters from a previous export.
 
Libraries used:
 
* `matplotlib`
* `pandas`
* `faker`
* `os`
* `csv`
* `random`
 
## Project Features
 
* 🎭 Create characters with a name, class, race, level, and base attributes.
* ⚔️ Manage a deep skill tree with prerequisites, skill levels, and custom skill creation.
* 🎒 Manage character inventories with items that apply stat multipliers.
* 📊 Radar charts and bar charts for individual character stats that display on screen with optional saving.
* 📈 Side-by-side attribute comparison charts for multiple characters.
* 🥧 Class distribution pie chart and level progression bar chart across your full roster.
* 🔢 Statistical analysis using pandas: mean, median, min, and max for every attribute across your roster.
* 🔍 Filter characters by class, sort by any stat, and find your top performers.
* 💾 Export your full roster to CSV and import it back in a later session.
* 🎲 Generate random characters with realistic names using Faker.
* 📖 Generate character backstories, physical descriptions, and random quests.
* 🔎 Search and select characters by keyword to set your active character.
* 🖥️ Clean terminal interface that clears between screens.
 
## Contributors
 
* dogo1017