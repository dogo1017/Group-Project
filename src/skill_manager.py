from menu import menu

def skill_menu(saved_skills, characters, selected_character):
    # Main skill management menu
    from menu import menu
    
    if selected_character == "":
        char_names = [char["name"] for char in characters]
        char_names.append("Return")
        result = menu(char_names)
        selected_index = result['index']
        
        if selected_index >= len(characters):
            return characters, selected_character
        
        selected_character = characters[selected_index]["name"]
    
    current_character = get_character(characters, selected_character)
    
    if current_character is None:
        print("Character not found!")
        input("Press Enter to continue...")
        return characters, ""
    
    skill_manage = True
    while skill_manage:
        result = menu(["Add Skill", "Remove Skill", "View Character Skills", "Level Up Skill", "View Skill Tree", "Return"])
        selected_index = result['index']
        
        if selected_index == 0:
            handle_add_skill(saved_skills, current_character)
        elif selected_index == 1:
            handle_remove_skill(current_character, saved_skills)
        elif selected_index == 2:
            handle_view_skills(saved_skills, current_character)
        elif selected_index == 3:
            handle_level_up_skill(saved_skills, current_character)
        elif selected_index == 4:
            handle_view_skill_tree(saved_skills, current_character)
        else:
            skill_manage = False
    
    return characters, selected_character


def get_character(characters, selected_character):
    # Helper function to find character by name
    for char in characters:
        if char["name"] == selected_character:
            return char
    return None


def initialize_skill_levels(character):
    # Initialize skill_levels dictionary if it doesn't exist
    if "skill_levels" not in character:
        character["skill_levels"] = {}


def initialize_default_skills():
    # Create a comprehensive skill library with 25+ skills organized by type
    
    def create_skill(description, effect, amount, target, level_req=1, max_level=10, prerequisites=None):
        # Inner function to create skill dictionary
        return {
            "description": description,
            "effect": effect,
            "amount": amount,
            "target": target,
            "level_requirement": level_req,
            "max_level": max_level,
            "prerequisites": prerequisites if prerequisites else [],
            "min_prerequisite_level": 1
        }
    
    skills = {}
    
    # BASIC COMBAT SKILLS (Only 3 starter skills - everything else builds from these)
    skills["Basic Strike"] = create_skill("A simple physical attack", "Attack", 10, "Enemy", 1, 5)
    skills["Defend"] = create_skill("Raise your guard to block attacks", "Defense", 5, "Self", 1, 5)
    skills["Minor Heal"] = create_skill("Restore a small amount of health", "Health", 15, "Self", 1, 5)
    
    # FIRE MAGIC TREE
    skills["Spark"] = create_skill("Shoot a small spark of fire", "Attack", 15, "Enemy", 2, 8)
    skills["Fireball"] = create_skill("Launch a ball of flames", "Attack", 50, "Enemy", 5, 10, ["Spark"])
    skills["Flame Wave"] = create_skill("A wave of fire hits all enemies", "Attack", 40, "Enemy", 8, 10, ["Fireball"])
    skills["Inferno"] = create_skill("Devastating flames engulf the battlefield", "Attack", 100, "Enemy", 15, 10, ["Flame Wave"])
    skills["Phoenix Fire"] = create_skill("Legendary flames that revive the caster", "Health", 80, "Self", 20, 10, ["Inferno"])
    
    # ICE MAGIC TREE
    skills["Frost Touch"] = create_skill("Freeze an enemy with a touch", "Attack", 12, "Enemy", 2, 8)
    skills["Ice Shard"] = create_skill("Launch sharp ice projectiles", "Attack", 45, "Enemy", 5, 10, ["Frost Touch"])
    skills["Blizzard"] = create_skill("Summon a freezing storm", "Attack", 70, "Enemy", 10, 10, ["Ice Shard"])
    skills["Absolute Zero"] = create_skill("Ultimate ice magic freezes everything", "Attack", 120, "Enemy", 18, 10, ["Blizzard"])
    
    # HEALING TREE
    skills["Heal"] = create_skill("Restore moderate health", "Health", 30, "Self", 3, 10, ["Minor Heal"])
    skills["Greater Heal"] = create_skill("Restore significant health", "Health", 60, "Self", 7, 10, ["Heal"])
    skills["Mass Heal"] = create_skill("Heal all allies", "Health", 40, "Ally", 12, 10, ["Greater Heal"])
    skills["Resurrection"] = create_skill("Bring an ally back from defeat", "Health", 100, "Ally", 20, 10, ["Mass Heal"])
    
    # DEFENSIVE TREE
    skills["Shield"] = create_skill("Create a protective barrier", "Defense", 20, "Self", 3, 10, ["Defend"])
    skills["Iron Skin"] = create_skill("Harden your body against attacks", "Defense", 35, "Self", 6, 10, ["Shield"])
    skills["Fortress"] = create_skill("Become nearly invulnerable", "Defense", 60, "Self", 12, 10, ["Iron Skin"])
    skills["Guardian's Aura"] = create_skill("Protect all allies with a shield", "Defense", 45, "Ally", 16, 10, ["Fortress"])
    
    # ADVANCED COMBAT TREE
    skills["Power Strike"] = create_skill("A stronger physical attack", "Attack", 35, "Enemy", 4, 10, ["Basic Strike"])
    skills["Cleave"] = create_skill("Attack multiple enemies at once", "Attack", 55, "Enemy", 8, 10, ["Power Strike"])
    skills["Berserker Rage"] = create_skill("Massive damage at the cost of defense", "Attack", 90, "Enemy", 14, 10, ["Cleave"])
    
    # SUPPORT SKILLS
    skills["Focus"] = create_skill("Increase your concentration", "Defense", 10, "Self", 2, 8)
    skills["Battle Cry"] = create_skill("Boost all allies' morale", "Defense", 25, "Ally", 6, 10, ["Focus"])
    skills["Divine Blessing"] = create_skill("Grant protection to all allies", "Defense", 50, "Ally", 11, 10, ["Battle Cry"])
    
    # ULTIMATE SKILLS (Require multiple high-level prerequisites)
    skills["Armageddon"] = create_skill(
        "Ultimate destruction magic", "Attack", 150, "Enemy", 25, 10, 
        ["Inferno", "Absolute Zero", "Berserker Rage"]
    )
    skills["Transcendence"] = create_skill(
        "Achieve a higher state of being", "Defense", 100, "Self", 25, 10,
        ["Guardian's Aura", "Divine Blessing", "Resurrection"]
    )
    
    # LIGHTNING MAGIC TREE
    skills["Static Shock"] = create_skill("Release a small electric jolt", "Attack", 14, "Enemy", 3, 8, ["Basic Strike"])
    skills["Lightning Bolt"] = create_skill("Strike with pure electricity", "Attack", 48, "Enemy", 5, 10, ["Static Shock"])
    skills["Chain Lightning"] = create_skill("Electricity jumps between enemies", "Attack", 65, "Enemy", 9, 10, ["Lightning Bolt"])
    skills["Thunderstorm"] = create_skill("Call down devastating lightning strikes", "Attack", 95, "Enemy", 16, 10, ["Chain Lightning"])
    skills["Mjolnir's Wrath"] = create_skill("Channel the power of thunder gods", "Attack", 125, "Enemy", 22, 10, ["Thunderstorm"])
    
    # EARTH MAGIC TREE
    skills["Stone Throw"] = create_skill("Hurl a chunk of rock", "Attack", 13, "Enemy", 3, 8, ["Basic Strike"])
    skills["Earthquake"] = create_skill("Shake the ground beneath enemies", "Attack", 42, "Enemy", 5, 10, ["Stone Throw"])
    skills["Boulder Crash"] = create_skill("Summon massive boulders to crush foes", "Attack", 68, "Enemy", 10, 10, ["Earthquake"])
    skills["Meteor Strike"] = create_skill("Call down flaming meteors", "Attack", 110, "Enemy", 17, 10, ["Boulder Crash"])
    
    # WIND MAGIC TREE
    skills["Gust"] = create_skill("Blow enemies back with wind", "Attack", 11, "Enemy", 3, 8, ["Basic Strike"])
    skills["Wind Blade"] = create_skill("Slice enemies with razor wind", "Attack", 40, "Enemy", 5, 10, ["Gust"])
    skills["Tornado"] = create_skill("Create a devastating whirlwind", "Attack", 72, "Enemy", 11, 10, ["Wind Blade"])
    skills["Hurricane Force"] = create_skill("Summon the fury of a hurricane", "Attack", 105, "Enemy", 19, 10, ["Tornado"])
    
    # SHADOW/DARK MAGIC TREE
    skills["Shadow Step"] = create_skill("Move through shadows briefly", "Defense", 8, "Self", 3, 8, ["Defend"])
    skills["Dark Bolt"] = create_skill("Fire a bolt of dark energy", "Attack", 38, "Enemy", 4, 10, ["Shadow Step"])
    skills["Curse"] = create_skill("Weaken an enemy's defenses", "Attack", 25, "Enemy", 6, 10, ["Dark Bolt"])
    skills["Shadow Clone"] = create_skill("Create illusory copies of yourself", "Defense", 40, "Self", 9, 10, ["Shadow Step"])
    skills["Void Blast"] = create_skill("Unleash devastating dark magic", "Attack", 85, "Enemy", 15, 10, ["Curse"])
    skills["Eclipse"] = create_skill("Bring total darkness to the battlefield", "Attack", 115, "Enemy", 21, 10, ["Void Blast"])
    
    # LIGHT/HOLY MAGIC TREE
    skills["Light Ray"] = create_skill("Beam of purifying light", "Attack", 16, "Enemy", 3, 8, ["Basic Strike"])
    skills["Holy Smite"] = create_skill("Strike with divine judgment", "Attack", 44, "Enemy", 5, 10, ["Light Ray"])
    skills["Purify"] = create_skill("Remove negative effects", "Health", 25, "Ally", 7, 10, ["Holy Smite"])
    skills["Radiance"] = create_skill("Emit blinding holy light", "Attack", 75, "Enemy", 13, 10, ["Holy Smite"])
    skills["Divine Intervention"] = create_skill("Call upon divine protection", "Defense", 70, "Ally", 18, 10, ["Radiance"])
    
    # POISON/NATURE TREE
    skills["Poison Dart"] = create_skill("Shoot a toxic projectile", "Attack", 20, "Enemy", 3, 8, ["Basic Strike"])
    skills["Venom Strike"] = create_skill("Attack with deadly poison", "Attack", 46, "Enemy", 6, 10, ["Poison Dart"])
    skills["Toxic Cloud"] = create_skill("Release a cloud of poison gas", "Attack", 55, "Enemy", 9, 10, ["Venom Strike"])
    skills["Nature's Wrath"] = create_skill("Summon vines to entangle enemies", "Attack", 62, "Enemy", 12, 10, ["Toxic Cloud"])
    skills["Plague"] = create_skill("Spread virulent disease", "Attack", 88, "Enemy", 17, 10, ["Toxic Cloud"])
    
    # STEALTH/ROGUE SKILLS
    skills["Backstab"] = create_skill("Strike from the shadows for extra damage", "Attack", 32, "Enemy", 4, 10, ["Basic Strike"])
    skills["Evasion"] = create_skill("Dodge incoming attacks", "Defense", 18, "Self", 4, 8)
    skills["Stealth"] = create_skill("Become nearly invisible", "Defense", 28, "Self", 7, 10, ["Evasion"])
    skills["Assassinate"] = create_skill("Instant kill low-health enemies", "Attack", 75, "Enemy", 13, 10, ["Backstab", "Stealth"])
    skills["Shadow Master"] = create_skill("Become one with darkness", "Defense", 65, "Self", 19, 10, ["Assassinate"])
    
    # BLOOD MAGIC TREE
    skills["Blood Drain"] = create_skill("Steal life from enemies", "Health", 22, "Self", 5, 8)
    skills["Crimson Pact"] = create_skill("Trade health for power", "Attack", 58, "Enemy", 8, 10, ["Blood Drain"])
    skills["Hemorrhage"] = create_skill("Cause uncontrollable bleeding", "Attack", 64, "Enemy", 11, 10, ["Crimson Pact"])
    skills["Life Exchange"] = create_skill("Transfer health between allies", "Health", 45, "Ally", 14, 10, ["Blood Drain"])
    skills["Crimson Tsunami"] = create_skill("Ultimate blood magic devastation", "Attack", 98, "Enemy", 20, 10, ["Hemorrhage"])
    
    # SUMMONING TREE
    skills["Summon Familiar"] = create_skill("Call a small magical creature to aid you", "Defense", 15, "Self", 4, 8)
    skills["Summon Elemental"] = create_skill("Summon a powerful elemental being", "Attack", 52, "Enemy", 8, 10, ["Summon Familiar"])
    skills["Summon Beast"] = create_skill("Call forth a mighty beast", "Attack", 60, "Enemy", 11, 10, ["Summon Familiar"])
    skills["Summon Dragon"] = create_skill("Summon an ancient dragon", "Attack", 100, "Enemy", 18, 10, ["Summon Elemental", "Summon Beast"])
    
    # TIME MAGIC TREE
    skills["Slow"] = create_skill("Reduce enemy speed", "Attack", 18, "Enemy", 5, 8)
    skills["Haste"] = create_skill("Increase your speed", "Defense", 24, "Self", 6, 8)
    skills["Time Stop"] = create_skill("Freeze time briefly", "Defense", 55, "Self", 14, 10, ["Slow", "Haste"])
    skills["Temporal Rift"] = create_skill("Tear through time itself", "Attack", 92, "Enemy", 20, 10, ["Time Stop"])
    
    # ILLUSION MAGIC TREE
    skills["Minor Illusion"] = create_skill("Create a simple illusion", "Defense", 12, "Self", 3, 8)
    skills["Confusion"] = create_skill("Disorient enemies", "Attack", 26, "Enemy", 6, 8, ["Minor Illusion"])
    skills["Mirror Image"] = create_skill("Create perfect copies of yourself", "Defense", 38, "Self", 10, 10, ["Minor Illusion"])
    skills["Mass Hallucination"] = create_skill("Fill enemies' minds with visions", "Attack", 70, "Enemy", 16, 10, ["Confusion", "Mirror Image"])
    
    # WATER/OCEAN MAGIC TREE
    skills["Water Jet"] = create_skill("Spray a high-pressure stream of water", "Attack", 12, "Enemy", 3, 8, ["Basic Strike"])
    skills["Tidal Wave"] = create_skill("Summon a massive wave to crash down", "Attack", 47, "Enemy", 5, 10, ["Water Jet"])
    skills["Whirlpool"] = create_skill("Create a swirling vortex of water", "Attack", 58, "Enemy", 9, 10, ["Tidal Wave"])
    skills["Tsunami"] = create_skill("Unleash devastating ocean fury", "Attack", 86, "Enemy", 15, 10, ["Whirlpool"])
    skills["Leviathan's Breath"] = create_skill("Channel the power of sea monsters", "Attack", 118, "Enemy", 21, 10, ["Tsunami"])
    
    # NECROMANCY TREE
    skills["Raise Dead"] = create_skill("Animate a fallen creature", "Defense", 20, "Self", 5, 8, ["Basic Strike"])
    skills["Soul Drain"] = create_skill("Steal the essence of life", "Health", 28, "Self", 7, 10, ["Raise Dead"])
    skills["Death Touch"] = create_skill("Kill with a single touch", "Attack", 80, "Enemy", 13, 10, ["Soul Drain"])
    skills["Army of Undead"] = create_skill("Raise multiple corpses to fight", "Attack", 65, "Enemy", 16, 10, ["Raise Dead"])
    skills["Lich Transformation"] = create_skill("Become an immortal lich", "Defense", 85, "Self", 22, 10, ["Death Touch", "Army of Undead"])
    
    # ARCANE/PURE MAGIC TREE
    skills["Magic Missile"] = create_skill("Fire unerring bolts of pure magic", "Attack", 17, "Enemy", 3, 8, ["Basic Strike"])
    skills["Arcane Blast"] = create_skill("Release raw magical energy", "Attack", 43, "Enemy", 6, 10, ["Magic Missile"])
    skills["Mana Shield"] = create_skill("Convert mana into protective barrier", "Defense", 32, "Self", 8, 10, ["Magic Missile"])
    skills["Arcane Storm"] = create_skill("Summon a tempest of pure magic", "Attack", 77, "Enemy", 14, 10, ["Arcane Blast"])
    skills["Reality Warp"] = create_skill("Bend the laws of magic itself", "Attack", 102, "Enemy", 20, 10, ["Arcane Storm"])
    
    # CELESTIAL/STAR MAGIC TREE
    skills["Starlight"] = create_skill("Summon gentle healing starlight", "Health", 20, "Self", 4, 8, ["Minor Heal"])
    skills["Comet"] = create_skill("Call down a burning comet", "Attack", 50, "Enemy", 7, 10, ["Starlight"])
    skills["Cosmic Ray"] = create_skill("Fire a beam of stellar energy", "Attack", 63, "Enemy", 11, 10, ["Comet"])
    skills["Supernova"] = create_skill("Explode with the power of dying stars", "Attack", 95, "Enemy", 17, 10, ["Cosmic Ray"])
    skills["Galaxy Collapse"] = create_skill("Harness the power of black holes", "Attack", 130, "Enemy", 23, 10, ["Supernova"])
    
    # MUSIC/BARD TREE
    skills["Inspiring Song"] = create_skill("Sing to boost ally morale", "Defense", 15, "Ally", 3, 8, ["Defend"])
    skills["Lullaby"] = create_skill("Put enemies to sleep with music", "Attack", 22, "Enemy", 5, 8, ["Inspiring Song"])
    skills["War Chant"] = create_skill("Energize allies for battle", "Defense", 30, "Ally", 8, 10, ["Inspiring Song"])
    skills["Sonic Scream"] = create_skill("Unleash devastating sound waves", "Attack", 56, "Enemy", 12, 10, ["Lullaby"])
    skills["Symphony of Destruction"] = create_skill("Conduct an orchestra of chaos", "Attack", 82, "Enemy", 18, 10, ["Sonic Scream", "War Chant"])
    
    # WEAPON MASTERY TREE
    skills["Parry"] = create_skill("Deflect incoming attacks", "Defense", 14, "Self", 3, 8, ["Defend"])
    skills["Riposte"] = create_skill("Counter-attack after blocking", "Attack", 28, "Enemy", 5, 10, ["Parry"])
    skills["Weapon Flourish"] = create_skill("Intimidate enemies with skill", "Defense", 22, "Self", 7, 8, ["Riposte"])
    skills["Disarm"] = create_skill("Knock weapon from enemy's hand", "Attack", 35, "Enemy", 9, 10, ["Riposte"])
    skills["Blade Dance"] = create_skill("Attack with graceful deadly precision", "Attack", 71, "Enemy", 14, 10, ["Disarm", "Weapon Flourish"])
    skills["Perfect Strike"] = create_skill("Land a flawless critical hit", "Attack", 108, "Enemy", 20, 10, ["Blade Dance"])
    
    # BEAST TAMING TREE
    skills["Animal Friendship"] = create_skill("Befriend wild animals", "Defense", 10, "Self", 3, 8, ["Defend"])
    skills["Beast Command"] = create_skill("Control a wild animal", "Attack", 24, "Enemy", 5, 10, ["Animal Friendship"])
    skills["Pack Tactics"] = create_skill("Coordinate attacks with beasts", "Attack", 41, "Enemy", 8, 10, ["Beast Command"])
    skills["Wild Shape"] = create_skill("Transform into a beast", "Defense", 48, "Self", 12, 10, ["Pack Tactics"])
    skills["Primal Fury"] = create_skill("Unleash unstoppable animal rage", "Attack", 79, "Enemy", 16, 10, ["Wild Shape"])
    
    # ALCHEMY/CHEMISTRY TREE
    skills["Acid Splash"] = create_skill("Throw corrosive acid", "Attack", 19, "Enemy", 3, 8, ["Basic Strike"])
    skills["Volatile Concoction"] = create_skill("Hurl an explosive mixture", "Attack", 39, "Enemy", 6, 10, ["Acid Splash"])
    skills["Transmute"] = create_skill("Transform matter into another form", "Defense", 29, "Self", 8, 8, ["Volatile Concoction"])
    skills["Alchemical Infusion"] = create_skill("Enhance equipment with alchemy", "Defense", 44, "Self", 11, 10, ["Transmute"])
    skills["Philosopher's Stone"] = create_skill("Create the ultimate alchemical power", "Health", 75, "Self", 19, 10, ["Alchemical Infusion"])
    
    # GRAVITY MAGIC TREE
    skills["Gravity Well"] = create_skill("Pull enemies toward a point", "Attack", 21, "Enemy", 4, 8, ["Basic Strike"])
    skills["Levitate"] = create_skill("Float above the ground", "Defense", 16, "Self", 5, 8, ["Gravity Well"])
    skills["Crushing Force"] = create_skill("Increase gravity on enemies", "Attack", 49, "Enemy", 9, 10, ["Gravity Well"])
    skills["Zero Gravity"] = create_skill("Remove all gravitational pull", "Defense", 37, "Ally", 11, 10, ["Levitate"])
    skills["Singularity"] = create_skill("Create a crushing gravity field", "Attack", 91, "Enemy", 17, 10, ["Crushing Force"])
    skills["Event Horizon"] = create_skill("Generate an inescapable gravity trap", "Attack", 112, "Enemy", 21, 10, ["Singularity"])
    
    # TECHNOLOGY/ARTIFICER TREE
    skills["Repair"] = create_skill("Fix broken equipment", "Health", 18, "Self", 3, 8, ["Minor Heal"])
    skills["Turret Deploy"] = create_skill("Place an automated turret", "Attack", 27, "Enemy", 6, 8, ["Repair"])
    skills["EMP Blast"] = create_skill("Disable magical and tech devices", "Attack", 34, "Enemy", 8, 10, ["Turret Deploy"])
    skills["Mech Suit"] = create_skill("Pilot a powerful mechanical suit", "Defense", 51, "Self", 12, 10, ["Repair"])
    skills["Orbital Strike"] = create_skill("Call down devastating energy from above", "Attack", 96, "Enemy", 18, 10, ["EMP Blast", "Mech Suit"])
    
    # DIMENSIONAL MAGIC TREE
    skills["Blink"] = create_skill("Teleport a short distance", "Defense", 13, "Self", 4, 8, ["Defend"])
    skills["Portal"] = create_skill("Create a gateway to another location", "Defense", 26, "Self", 7, 10, ["Blink"])
    skills["Dimension Door"] = create_skill("Step through dimensional barriers", "Defense", 42, "Self", 10, 10, ["Portal"])
    skills["Planar Shift"] = create_skill("Travel between dimensions", "Defense", 59, "Self", 15, 10, ["Dimension Door"])
    skills["Void Prison"] = create_skill("Trap enemies in another dimension", "Attack", 87, "Enemy", 19, 10, ["Planar Shift"])
    
    # DRUID/PLANT MAGIC TREE
    skills["Entangle"] = create_skill("Roots spring up to trap enemies", "Attack", 16, "Enemy", 3, 8, ["Basic Strike"])
    skills["Barkskin"] = create_skill("Harden your skin like tree bark", "Defense", 21, "Self", 5, 8, ["Entangle"])
    skills["Thorn Volley"] = create_skill("Launch a storm of sharp thorns", "Attack", 45, "Enemy", 8, 10, ["Entangle"])
    skills["Wall of Thorns"] = create_skill("Create an impassable barrier of plants", "Defense", 46, "Self", 11, 10, ["Barkskin"])
    skills["Nature's Avatar"] = create_skill("Become a massive plant creature", "Attack", 84, "Enemy", 16, 10, ["Thorn Volley", "Wall of Thorns"])
    
    # CRYSTAL/GEM MAGIC TREE
    skills["Crystal Shard"] = create_skill("Fire sharp crystalline projectiles", "Attack", 15, "Enemy", 3, 8, ["Basic Strike"])
    skills["Gem Shield"] = create_skill("Summon protective crystals", "Defense", 23, "Self", 5, 8, ["Crystal Shard"])
    skills["Prism Beam"] = create_skill("Refract light through crystals", "Attack", 52, "Enemy", 9, 10, ["Crystal Shard"])
    skills["Diamond Skin"] = create_skill("Become as hard as diamond", "Defense", 54, "Self", 12, 10, ["Gem Shield"])
    skills["Crystal Apocalypse"] = create_skill("Shatter reality with crystalline power", "Attack", 103, "Enemy", 19, 10, ["Prism Beam", "Diamond Skin"])
    
    # MIND/PSYCHIC TREE
    skills["Telepathy"] = create_skill("Read surface thoughts", "Defense", 11, "Self", 3, 8, ["Focus"])
    skills["Mind Blast"] = create_skill("Attack directly with mental force", "Attack", 33, "Enemy", 6, 10, ["Telepathy"])
    skills["Telekinesis"] = create_skill("Move objects with your mind", "Attack", 36, "Enemy", 8, 10, ["Telepathy"])
    skills["Mental Fortress"] = create_skill("Block mental intrusions", "Defense", 41, "Self", 10, 10, ["Telepathy"])
    skills["Dominate Mind"] = create_skill("Take control of an enemy", "Attack", 69, "Enemy", 14, 10, ["Mind Blast"])
    skills["Psychic Storm"] = create_skill("Overwhelm minds with raw power", "Attack", 99, "Enemy", 19, 10, ["Dominate Mind"])
    
    # CHAOS MAGIC TREE
    skills["Wild Surge"] = create_skill("Unleash unpredictable magical energy", "Attack", 25, "Enemy", 4, 8, ["Basic Strike"])
    skills["Entropy"] = create_skill("Accelerate decay and disorder", "Attack", 40, "Enemy", 7, 10, ["Wild Surge"])
    skills["Reality Glitch"] = create_skill("Cause random magical effects", "Attack", 53, "Enemy", 10, 10, ["Entropy"])
    skills["Chaos Rift"] = create_skill("Tear open a portal to chaos", "Attack", 76, "Enemy", 15, 10, ["Reality Glitch"])
    skills["Pandemonium"] = create_skill("Bring absolute chaos to battle", "Attack", 107, "Enemy", 20, 10, ["Chaos Rift"])
    
    # SPIRIT/SOUL MAGIC TREE
    skills["Spirit Touch"] = create_skill("Interact with ethereal beings", "Defense", 14, "Self", 3, 8, ["Defend"])
    skills["Astral Projection"] = create_skill("Send your soul out of your body", "Defense", 27, "Self", 6, 10, ["Spirit Touch"])
    skills["Soul Lance"] = create_skill("Pierce enemies with spirit energy", "Attack", 48, "Enemy", 9, 10, ["Spirit Touch"])
    skills["Ethereal Form"] = create_skill("Become partially incorporeal", "Defense", 50, "Self", 12, 10, ["Astral Projection"])
    skills["Soul Reaper"] = create_skill("Harvest the souls of the fallen", "Attack", 93, "Enemy", 18, 10, ["Soul Lance", "Ethereal Form"])
    
    # DRAGON MAGIC TREE
    skills["Dragon Breath"] = create_skill("Exhale elemental energy", "Attack", 31, "Enemy", 5, 8, ["Basic Strike"])
    skills["Dragon Scales"] = create_skill("Grow protective draconic scales", "Defense", 35, "Self", 7, 8, ["Dragon Breath"])
    skills["Draconic Roar"] = create_skill("Terrify enemies with a mighty roar", "Attack", 44, "Enemy", 9, 10, ["Dragon Breath"])
    skills["Dragon Wings"] = create_skill("Sprout powerful dragon wings", "Defense", 47, "Self", 11, 10, ["Dragon Scales"])
    skills["True Dragon Form"] = create_skill("Transform into an ancient dragon", "Attack", 120, "Enemy", 22, 10, ["Draconic Roar", "Dragon Wings"])
    
    return skills


def handle_add_skill(saved_skills, character):
    # Handle the skill addition menu
    result = menu(["Add Existing Skill", "Edit Existing Skill", "Add New Skill", "Return"])
    result_index = result['index']
    
    if result_index == 0:
        add_existing_skill(saved_skills, character)
    elif result_index == 1:
        edit_existing_skill(saved_skills, character)
    elif result_index == 2:
        add_new_skill(saved_skills, character)


def add_existing_skill(saved_skills, character):
    # Add a skill from the saved skills library
    if not saved_skills:
        print("No saved skills available!")
        input("Press Enter to continue...")
        return
    
    initialize_skill_levels(character)
    
    # Categorize skills for better organization
    categorized_skills = categorize_skills(saved_skills)
    
    # Show categories
    categories = list(categorized_skills.keys())
    categories.append("View All Skills")
    categories.append("Return")
    
    cat_result = menu(categories)
    cat_selected = cat_result['index']
    
    # Handle Return
    if cat_selected == len(categories) - 1:
        return
    
    # Handle View All Skills
    if cat_selected == len(categories) - 2:
        skill_names = list(saved_skills.keys())
    else:
        # Handle specific category
        category = categories[cat_selected]
        skill_names = categorized_skills[category]
    
    skill_names.append("Return")
    skill_result = menu(skill_names)
    selected = skill_result['index']
    
    if selected < len(skill_names) - 1:
        selected_skill = skill_names[selected]
        attempt_add_skill(character, selected_skill, saved_skills)


def categorize_skills(saved_skills):
    # Categorize skills by their effect type and prerequisites
    
    def get_category(skill_name, skill_info):
        # Inner function to determine skill category
        if not skill_info.get("prerequisites"):
            return "Basic Skills"
        elif skill_info["effect"] == "Attack":
            if "fire" in skill_name.lower() or "flame" in skill_name.lower() or "inferno" in skill_name.lower():
                return "Fire Magic"
            elif "ice" in skill_name.lower() or "frost" in skill_name.lower() or "blizzard" in skill_name.lower():
                return "Ice Magic"
            else:
                return "Combat Skills"
        elif skill_info["effect"] == "Health":
            return "Healing Skills"
        elif skill_info["effect"] == "Defense":
            return "Defensive Skills"
        return "Special Skills"
    
    categories = {}
    for skill_name, skill_info in saved_skills.items():
        category = get_category(skill_name, skill_info)
        if category not in categories:
            categories[category] = []
        categories[category].append(skill_name)
    
    return categories


def attempt_add_skill(character, selected_skill, saved_skills):
    # Attempt to add a skill to character with validation
    skill_info = saved_skills[selected_skill]
    
    # Check if already has skill
    if selected_skill in character["skills"]:
        print(f"{selected_skill} is already in {character['name']}'s skills!")
        input("Press Enter to continue...")
        return
    
    # Validate prerequisites
    prereq_check = validate_prerequisites(character, skill_info, saved_skills)
    if not prereq_check["valid"]:
        print(f"\nCannot add {selected_skill}!")
        print(f"Missing prerequisites: {', '.join(prereq_check['missing'])}")
        if prereq_check["low_level_prereqs"]:
            print(f"Insufficient prerequisite levels: {', '.join(prereq_check['low_level_prereqs'])}")
        input("Press Enter to continue...")
        return
    
    # Check level requirement
    if character.get("level", 1) < skill_info.get("level_requirement", 1):
        print(f"\nCannot add {selected_skill}!")
        print(f"Character level {character.get('level', 1)} is too low. Required level: {skill_info['level_requirement']}")
        input("Press Enter to continue...")
        return
    
    # Add the skill
    character["skills"].add(selected_skill)
    character["skill_levels"][selected_skill] = 1
    print(f"Added {selected_skill} to {character['name']} at level 1!")
    input("Press Enter to continue...")


def validate_prerequisites(character, skill_info, saved_skills):
    # Validate all prerequisites for a skill
    
    def check_single_prereq(prereq):
        # Inner function to check a single prerequisite
        if prereq not in character["skills"]:
            return {"valid": False, "reason": "not_learned"}
        
        prereq_info = saved_skills.get(prereq, {})
        min_level = prereq_info.get("min_prerequisite_level", 1)
        current_level = character.get("skill_levels", {}).get(prereq, 0)
        
        if current_level < min_level:
            return {"valid": False, "reason": "low_level", "required": min_level, "current": current_level}
        
        return {"valid": True}
    
    result = {
        "valid": True,
        "missing": [],
        "low_level_prereqs": []
    }
    
    prerequisites = skill_info.get("prerequisites", [])
    if not prerequisites:
        return result
    
    for prereq in prerequisites:
        check = check_single_prereq(prereq)
        if not check["valid"]:
            result["valid"] = False
            if check["reason"] == "not_learned":
                result["missing"].append(prereq)
            elif check["reason"] == "low_level":
                result["low_level_prereqs"].append(f"{prereq} (Lv {check['current']}/{check['required']})")
    
    return result


def handle_level_up_skill(saved_skills, character):
    # Level up a skill to improve its effectiveness
    if not character["skills"]:
        print("No skills to level up!")
        input("Press Enter to continue...")
        return
    
    initialize_skill_levels(character)
    
    skill_list = list(character["skills"])
    
    # Show skills with their current levels and upgrade costs
    skill_display = []
    for skill in skill_list:
        level = character['skill_levels'].get(skill, 1)
        max_level = saved_skills.get(skill, {}).get("max_level", 10)
        skill_display.append(f"{skill} (Lv {level}/{max_level})")
    skill_display.append("Return")
    
    result = menu(skill_display)
    selected = result['index']
    
    if selected < len(skill_list):
        skill_name = skill_list[selected]
        perform_skill_levelup(character, skill_name, saved_skills)


def perform_skill_levelup(character, skill_name, saved_skills):
    # Perform the actual skill level up with calculations
    
    def calculate_stat_increase(base_amount, current_level):
        # Inner function to calculate stat increase per level
        return base_amount * 0.1 * current_level
    
    current_level = character["skill_levels"].get(skill_name, 1)
    skill_info = saved_skills.get(skill_name, {})
    max_level = skill_info.get("max_level", 10)
    
    if current_level >= max_level:
        print(f"{skill_name} is already at max level ({max_level})!")
        input("Press Enter to continue...")
        return
    
    # Level up the skill
    new_level = current_level + 1
    character["skill_levels"][skill_name] = new_level
    
    # Calculate and display improvements
    base_amount = skill_info.get("amount", 0)
    old_amount = base_amount + calculate_stat_increase(base_amount, current_level - 1)
    new_amount = base_amount + calculate_stat_increase(base_amount, new_level - 1)
    
    print(f"\n{'='*50}")
    print(f"SKILL LEVEL UP!")
    print(f"{'='*50}")
    print(f"{skill_name}: Level {current_level} → Level {new_level}")
    print(f"Effect strength: {old_amount:.1f} → {new_amount:.1f}")
    print(f"Improvement: +{new_amount - old_amount:.1f}")
    print(f"{'='*50}")
    input("\nPress Enter to continue...")


def handle_view_skill_tree(saved_skills, character):
    # Display available skills and their prerequisites in a tree structure
    
    def build_dependency_map():
        # Inner function to build skill dependency relationships
        root_skills = []
        dependent_skills = {}
        
        for skill_name, skill_info in saved_skills.items():
            prereqs = skill_info.get("prerequisites", [])
            if not prereqs:
                root_skills.append(skill_name)
            else:
                for prereq in prereqs:
                    if prereq not in dependent_skills:
                        dependent_skills[prereq] = []
                    if skill_name not in dependent_skills[prereq]:
                        dependent_skills[prereq].append(skill_name)
        
        return root_skills, dependent_skills
    
    import os
    os.system('cls')
    
    print("\n" + "="*80)
    print(" "*25 + "SKILL TREE OVERVIEW")
    print("="*80)
    
    # Show legend first
    print("\nLEGEND:")
    print("  ✓ = You have this skill")
    print("  ○ = Available to learn now")
    print("  ● = Locked (need prerequisites)")
    print("  ⚠ = Locked (character level too low)")
    print("\n" + "-"*80)
    
    root_skills, dependent_skills = build_dependency_map()
    
    # Organize skills by category for cleaner display
    categories = {
        "Basic": [],
        "Fire Magic": [],
        "Ice Magic": [],
        "Healing": [],
        "Defense": [],
        "Combat": [],
        "Support": [],
        "Ultimate": []
    }
    
    for skill_name, skill_info in saved_skills.items():
        desc = skill_info.get("description", "").lower()
        name = skill_name.lower()
        prereqs = skill_info.get("prerequisites", [])
        
        if not prereqs:
            categories["Basic"].append(skill_name)
        elif "fire" in name or "flame" in name or "inferno" in name or "spark" in name or "phoenix" in name:
            categories["Fire Magic"].append(skill_name)
        elif "ice" in name or "frost" in name or "blizzard" in name or "zero" in name:
            categories["Ice Magic"].append(skill_name)
        elif "heal" in name or "resurrection" in name:
            categories["Healing"].append(skill_name)
        elif "shield" in name or "fortress" in name or "guardian" in name or "iron skin" in name:
            categories["Defense"].append(skill_name)
        elif "strike" in name or "cleave" in name or "berserker" in name:
            categories["Combat"].append(skill_name)
        elif "focus" in name or "battle cry" in name or "blessing" in name:
            categories["Support"].append(skill_name)
        elif len(prereqs) >= 3:  # Ultimate skills have multiple prereqs
            categories["Ultimate"].append(skill_name)
    
    # Display each category
    for category, skills in categories.items():
        if not skills:
            continue
            
        print(f"\n┌─ {category.upper()}")
        for i, skill_name in enumerate(sorted(skills)):
            is_last = (i == len(skills) - 1)
            display_skill_in_tree(skill_name, saved_skills, character, dependent_skills, is_last)
    
    print("\n" + "="*80)
    input("\nPress Enter to return to skill menu...")


def display_skill_in_tree(skill_name, saved_skills, character, dependent_skills, is_last_in_category):
    # Display a single skill in the tree with better formatting
    
    def get_skill_status_symbol(skill_name, skill_info, character):
        # Get the status symbol for a skill
        if skill_name in character.get("skills", set()):
            level = character.get("skill_levels", {}).get(skill_name, 1)
            max_level = skill_info.get("max_level", 10)
            return "✓", f"Lv{level}/{max_level}"
        
        prereq_check = validate_prerequisites(character, skill_info, saved_skills)
        char_level = character.get("level", 1)
        req_level = skill_info.get("level_requirement", 1)
        
        if char_level < req_level:
            return "⚠", f"Need Lv{req_level}"
        elif not prereq_check["valid"]:
            return "●", "Locked"
        else:
            return "○", "Available"
    
    skill_info = saved_skills.get(skill_name, {})
    symbol, status = get_skill_status_symbol(skill_name, skill_info, character)
    
    # Get skill stats
    effect = skill_info.get("effect", "?")
    amount = skill_info.get("amount", 0)
    target = skill_info.get("target", "?")
    
    # Main skill line
    branch = "└─" if is_last_in_category else "├─"
    print(f"│ {branch} {symbol} {skill_name:<20} [{effect}: {amount} → {target}] ({status})")
    
    # Show prerequisites if any
    prereqs = skill_info.get("prerequisites", [])
    if prereqs:
        continuation = "  " if is_last_in_category else "│ "
        prereq_str = " + ".join(prereqs)
        print(f"│ {continuation}   └─ Requires: {prereq_str}")
    
    # Show what this unlocks (only for unlocked skills)
    if skill_name in character.get("skills", set()) and skill_name in dependent_skills:
        continuation = "  " if is_last_in_category else "│ "
        unlocks = ", ".join(dependent_skills[skill_name][:3])
        if len(dependent_skills[skill_name]) > 3:
            unlocks += f" +{len(dependent_skills[skill_name]) - 3} more"
        print(f"│ {continuation}   └─ Unlocks: {unlocks}")


def handle_view_skills(saved_skills, character):
    # View all of character's current skills with detailed information
    import os
    os.system('cls')
    
    print("\n" + "="*80)
    print(f" "*25 + f"{character['name'].upper()}'S SKILLS")
    print("="*80)
    
    if character["skills"]:
        initialize_skill_levels(character)
        
        # Organize skills by category for better viewing
        categorized = {}
        for skill_name in character["skills"]:
            skill_info = saved_skills.get(skill_name, {})
            effect = skill_info.get("effect", "Other")
            if effect not in categorized:
                categorized[effect] = []
            categorized[effect].append(skill_name)
        
        # Display skills by category
        for category in sorted(categorized.keys()):
            print(f"\n┌─ {category.upper()} SKILLS")
            skills_in_cat = sorted(categorized[category])
            for i, skill_name in enumerate(skills_in_cat):
                is_last = (i == len(skills_in_cat) - 1)
                display_owned_skill_info(saved_skills, skill_name, character, is_last)
            print("│")
    else:
        print("\n  No skills learned yet!")
        print("  Visit 'Add Skill' to learn your first skill.")
    
    print("="*80)
    input("\nPress Enter to continue...")


def display_owned_skill_info(saved_skills, skill_name, character, is_last):
    # Display detailed information about a skill the character owns
    skill_info = saved_skills.get(skill_name, {})
    skill_level = character.get("skill_levels", {}).get(skill_name, 1)
    max_level = skill_info.get("max_level", 10)
    
    # Calculate level-adjusted amount
    base_amount = skill_info.get("amount", 0)
    adjusted_amount = base_amount + (skill_level - 1) * (base_amount * 0.1)
    
    branch = "└─" if is_last else "├─"
    continuation = "  " if is_last else "│ "
    
    # Skill name and level
    print(f"│ {branch} {skill_name} [Level {skill_level}/{max_level}]")
    
    # Description
    desc = skill_info.get('description', 'N/A')
    print(f"│ {continuation}   • {desc}")
    
    # Stats
    effect = skill_info.get('effect', 'N/A')
    target = skill_info.get('target', 'N/A')
    print(f"│ {continuation}   • Power: {adjusted_amount:.1f} (Base: {base_amount}) | {effect} → {target}")
    
    # Level progress bar
    if skill_level < max_level:
        progress = int((skill_level / max_level) * 20)
        bar = "█" * progress + "░" * (20 - progress)
        print(f"│ {continuation}   • Progress: [{bar}] {skill_level}/{max_level}")
    else:
        print(f"│ {continuation}   • ⭐ MAX LEVEL ⭐")


def handle_level_up_skill(saved_skills, character):
    # Level up a skill to improve its effectiveness
    if not character["skills"]:
        print("No skills to level up!")
        input("Press Enter to continue...")
        return
    
    initialize_skill_levels(character)
    
    skill_list = sorted(list(character["skills"]))
    
    # Show skills with their current levels and upgrade info
    skill_display = []
    for skill in skill_list:
        level = character['skill_levels'].get(skill, 1)
        max_level = saved_skills.get(skill, {}).get("max_level", 10)
        
        if level >= max_level:
            skill_display.append(f"{skill} (Lv {level}/{max_level}) [MAX]")
        else:
            skill_display.append(f"{skill} (Lv {level}/{max_level})")
    
    skill_display.append("Return")
    
    result = menu(skill_display)
    selected = result['index']
    
    if selected < len(skill_list):
        skill_name = skill_list[selected]
        perform_skill_levelup(character, skill_name, saved_skills)


def perform_skill_levelup(character, skill_name, saved_skills):
    # Perform the actual skill level up with calculations
    import os
    
    def calculate_stat_increase(base_amount, current_level):
        # Inner function to calculate stat increase per level
        return base_amount * 0.1 * current_level
    
    current_level = character["skill_levels"].get(skill_name, 1)
    skill_info = saved_skills.get(skill_name, {})
    max_level = skill_info.get("max_level", 10)
    
    if current_level >= max_level:
        print(f"\n{skill_name} is already at max level ({max_level})!")
        input("Press Enter to continue...")
        return
    
    # Level up the skill
    new_level = current_level + 1
    character["skill_levels"][skill_name] = new_level
    
    # Calculate and display improvements
    base_amount = skill_info.get("amount", 0)
    old_amount = base_amount + calculate_stat_increase(base_amount, current_level - 1)
    new_amount = base_amount + calculate_stat_increase(base_amount, new_level - 1)
    
    os.system('cls')
    print("\n" + "="*60)
    print(" "*20 + "⚔ SKILL LEVEL UP! ⚔")
    print("="*60)
    print(f"\n  {skill_name}")
    print(f"\n  Level: {current_level} ──→ {new_level}")
    print(f"  Power: {old_amount:.1f} ──→ {new_amount:.1f} (+{new_amount - old_amount:.1f})")
    
    if new_level == max_level:
        print(f"\n  ⭐ MAXIMUM LEVEL ACHIEVED! ⭐")
    
    print("\n" + "="*60)
    input("\nPress Enter to continue...")


def display_skill_node(skill_name, saved_skills, character, dependent_skills, indent=0):
    # Recursively display a skill and its dependents
    
    def get_skill_status(skill_name, skill_info, character):
        # Inner function to determine skill status symbol
        if skill_name in character.get("skills", set()):
            return "✓", f" [Lv {character.get('skill_levels', {}).get(skill_name, 1)}]"
        
        prereq_check = validate_prerequisites(character, skill_info, saved_skills)
        
        if character.get("level", 1) < skill_info.get("level_requirement", 1):
            return "⚠", f" [Req: Char Lv {skill_info.get('level_requirement', 1)}]"
        elif not prereq_check["valid"] and prereq_check["low_level_prereqs"]:
            return "⊗", f" [Low Prereq Levels]"
        elif not prereq_check["valid"]:
            return "✗", f" [Missing: {', '.join(prereq_check['missing'][:2])}]"
        else:
            return "✓", " [Available]"
    
    skill_info = saved_skills.get(skill_name, {})
    status, level_info = get_skill_status(skill_name, skill_info, character)
    
    # Print the skill
    prefix = "  " * indent + "├─ "
    effect = skill_info.get("effect", "?")
    amount = skill_info.get("amount", 0)
    print(f"{prefix}{status} {skill_name}{level_info} ({effect}: {amount})")
    
    # Show prerequisites if any
    if "prerequisites" in skill_info and skill_info["prerequisites"]:
        prereq_str = ", ".join(skill_info["prerequisites"])
        print(f"{'  ' * (indent + 1)}  └─ Requires: {prereq_str}")
    
    # Recursively display dependent skills
    if skill_name in dependent_skills:
        for dependent in sorted(dependent_skills[skill_name]):
            display_skill_node(dependent, saved_skills, character, dependent_skills, indent + 1)


def edit_existing_skill(saved_skills, character):
    # Edit an existing skill in the character's skill list
    if not character["skills"]:
        print("No skills to edit!")
        input("Press Enter to continue...")
        return
        
    skill_list = list(character["skills"])
    edit_result = menu([*skill_list, "Return"])
    selected = edit_result['index']
    
    if selected < len(skill_list):
        skill_to_edit = skill_list[selected]
        skill_info = saved_skills.get(skill_to_edit, {})
        
        skill_data = get_skill_data_from_menu(skill_info)
        
        if skill_data['index'] == 7:  # Save Changes index
            update_skill(saved_skills, character, skill_to_edit, skill_info, skill_data)


def get_skill_data_from_menu(skill_info=None):
    # Get skill data with prerequisites and level requirements
    if skill_info is None:
        skill_info = {}
    
    return menu(
        ["Skill Name", "Skill Description", "Skill Effect", "Effect Strength", 
         "Skill Target", "Level Requirement", "Max Skill Level", "Save Changes", "Return"],
        writable=[0, 1],
        toggle=[2, 4],
        tog_opts=[["Attack", "Defense", "Health"], [["Enemy", "Self", "Ally"], [4]]],
        number=[3, 5, 6],
        num_min=1,
        num_max=100
    )


def update_skill(saved_skills, character, skill_to_edit, skill_info, skill_data):
    # Update a skill's properties
    new_name = ''.join(skill_data['writable'][0]) or skill_to_edit
    new_desc = ''.join(skill_data['writable'][1]) or skill_info.get("description", "")
    
    updated_skill = {
        "description": new_desc,
        "effect": skill_data['toggles'][2],
        "amount": skill_data['numbers'][3],
        "target": skill_data['toggles'][4],
        "level_requirement": skill_data['numbers'][5],
        "max_level": skill_data['numbers'][6],
        "prerequisites": skill_info.get("prerequisites", [])
    }
    
    saved_skills[new_name] = updated_skill
    
    if new_name != skill_to_edit:
        character["skills"].remove(skill_to_edit)
        if skill_to_edit in saved_skills:
            del saved_skills[skill_to_edit]
        if "skill_levels" in character and skill_to_edit in character["skill_levels"]:
            character["skill_levels"][new_name] = character["skill_levels"][skill_to_edit]
            del character["skill_levels"][skill_to_edit]
    
    character["skills"].add(new_name)
    print("Skill updated!")
    input("Press Enter to continue...")


def add_new_skill(saved_skills, character):
    # Create and add a completely new skill
    skill_data = menu(
        ["Skill Name", "Skill Description", "Skill Effect", "Effect Strength", 
         "Skill Target", "Level Requirement", "Max Skill Level", "Save Skill", "Return"],
        writable=[0, 1],
        toggle=[2, 4],
        tog_opts=[["Attack", "Defense", "Health"], [["Enemy", "Self", "Ally"], [4]]],
        number=[3, 5, 6],
        num_min=1,
        num_max=100
    )
    
    if skill_data['index'] == 7:  # Save Skill
        skill_name = ''.join(skill_data['writable'][0])
        skill_desc = ''.join(skill_data['writable'][1])
        
        if skill_name:
            new_skill = create_skill_dict(skill_data, skill_desc)
            
            # Ask for prerequisites
            prereqs = get_prerequisites(saved_skills, skill_name)
            new_skill["prerequisites"] = prereqs
            
            saved_skills[skill_name] = new_skill
            
            # Check if character can add this skill
            prereq_check = validate_prerequisites(character, new_skill, saved_skills)
            if prereq_check["valid"] and character.get("level", 1) >= new_skill["level_requirement"]:
                character["skills"].add(skill_name)
                initialize_skill_levels(character)
                character["skill_levels"][skill_name] = 1
                print(f"Created and added {skill_name} to {character['name']}!")
            else:
                print(f"Created {skill_name} but prerequisites/level requirements not met to add to character.")
        else:
            print("Skill name cannot be empty!")
        input("Press Enter to continue...")


def get_prerequisites(saved_skills, current_skill_name):
    # Let user select prerequisite skills
    if not saved_skills:
        return []
    
    print("\nSelect prerequisite skills (skills that must be learned first)")
    print("This skill cannot be its own prerequisite!")
    
    available_skills = [s for s in saved_skills.keys() if s != current_skill_name]
    if not available_skills:
        print("No available skills for prerequisites.")
        input("Press Enter to continue...")
        return []
    
    selected_prereqs = []
    
    while True:
        display_list = available_skills.copy()
        display_list.append("Done - No more prerequisites")
        
        result = menu(display_list)
        selected = result['index']
        
        if selected >= len(available_skills):
            break
        
        prereq_skill = available_skills[selected]
        selected_prereqs.append(prereq_skill)
        available_skills.remove(prereq_skill)
        print(f"Added {prereq_skill} as a prerequisite.")
        
        if not available_skills:
            break
    
    return selected_prereqs


def create_skill_dict(skill_data, skill_desc):
    # Create a skill dictionary from menu data
    return {
        "description": skill_desc,
        "effect": skill_data['toggles'][2],
        "amount": skill_data['numbers'][3],
        "target": skill_data['toggles'][4],
        "level_requirement": skill_data['numbers'][5],
        "max_level": skill_data['numbers'][6],
        "prerequisites": []
    }


def handle_remove_skill(character, saved_skills):
    # Remove a skill from character with dependency checking
    
    def check_dependents(skill_to_remove, character, saved_skills):
        # Inner function to check if other skills depend on this one
        dependents = []
        for skill in character["skills"]:
            if skill == skill_to_remove:
                continue
            skill_info = saved_skills.get(skill, {})
            if skill_to_remove in skill_info.get("prerequisites", []):
                dependents.append(skill)
        return dependents
    
    if not character["skills"]:
        print("No skills to remove!")
        input("Press Enter to continue...")
        return
    
    skill_list = list(character["skills"])
    result = menu([*skill_list, "Return"])
    selected = result['index']
    
    if selected < len(skill_list):
        removed_skill = skill_list[selected]
        
        # Check if other skills depend on this one
        dependents = check_dependents(removed_skill, character, saved_skills)
        if dependents:
            print(f"\nWarning! The following skills require {removed_skill}:")
            for dep in dependents:
                print(f"  - {dep}")
            print("\nRemoving this skill will also remove all dependent skills.")
            confirm = input("Continue? (y/n): ").strip().lower()
            if confirm != 'y':
                return
            
            # Remove all dependent skills
            for dep in dependents:
                character["skills"].remove(dep)
                if "skill_levels" in character and dep in character["skill_levels"]:
                    del character["skill_levels"][dep]
        
        # Remove the skill
        character["skills"].remove(removed_skill)
        if "skill_levels" in character and removed_skill in character["skill_levels"]:
            del character["skill_levels"][removed_skill]
        
        print(f"Removed {removed_skill} from {character['name']}!")
        if dependents:
            print(f"Also removed: {', '.join(dependents)}")
        input("Press Enter to continue...")


def handle_view_skills(saved_skills, character):
    # View all of character's current skills with detailed information
    print(f"\n{'='*70}")
    print(f"{character['name']}'s Skills")
    print(f"{'='*70}")
    
    if character["skills"]:
        initialize_skill_levels(character)
        
        # Organize skills by category for better viewing
        categorized = {}
        for skill_name in character["skills"]:
            skill_info = saved_skills.get(skill_name, {})
            effect = skill_info.get("effect", "Other")
            if effect not in categorized:
                categorized[effect] = []
            categorized[effect].append(skill_name)
        
        # Display skills by category
        for category in sorted(categorized.keys()):
            print(f"\n[{category} Skills]")
            for skill_name in sorted(categorized[category]):
                display_skill_info(saved_skills, skill_name, character)
    else:
        print("  No skills yet!")
    
    print(f"\n{'='*70}")
    input("\nPress Enter to continue...")


def display_skill_info(saved_skills, skill_name, character):
    # Display detailed information about a specific skill
    skill_info = saved_skills.get(skill_name, {})
    skill_level = character.get("skill_levels", {}).get(skill_name, 1)
    max_level = skill_info.get("max_level", 10)
    
    # Calculate level-adjusted amount
    base_amount = skill_info.get("amount", 0)
    adjusted_amount = base_amount + (skill_level - 1) * (base_amount * 0.1)
    
    print(f"\n  ◆ {skill_name} [Level {skill_level}/{max_level}]")
    print(f"    Description: {skill_info.get('description', 'N/A')}")
    print(f"    Effect Type: {skill_info.get('effect', 'N/A')}")
    print(f"    Power: {adjusted_amount:.1f} (Base: {base_amount})")
    print(f"    Target: {skill_info.get('target', 'N/A')}")
    
    if "prerequisites" in skill_info and skill_info["prerequisites"]:
        print(f"    Required Skills: {', '.join(skill_info['prerequisites'])}")
    
    if "level_requirement" in skill_info:
        print(f"    Minimum Level: {skill_info['level_requirement']}")