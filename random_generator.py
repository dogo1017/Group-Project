from faker import Faker
import random


class RandomGenerator:

    def __init__(self):
        self.faker = Faker()
        self.classes = ["rogue", "warrior", "mage", "paladin", "ranger", "bard", "tank"]
        self.races = ["Human", "Elf", "Ork", "Dwarf", "Halfling"]
        self.personality_traits = [
            "brave", "cunning", "wise", "hot-headed", "calm", "reckless",
            "loyal", "selfish", "honorable", "mysterious", "cheerful", "brooding"
        ]
        self.locations = [
            "the frozen north", "a desert oasis", "a hidden forest village",
            "a bustling port city", "an underground dwarf city", "a mountain monastery",
            "a war-torn kingdom", "a magical academy", "a pirate island", "a haunted swamp"
        ]
        self.motivations = [
            "seeking revenge for their fallen family",
            "searching for a legendary artifact",
            "fleeing a dark past",
            "trying to restore their family's honor",
            "hunting a powerful monster",
            "trying to lift an ancient curse",
            "gathering power to overthrow a tyrant",
            "searching for a lost sibling"
        ]

    def generate_name(self):
        return self.faker.first_name() + " " + self.faker.last_name()

    def generate_backstory(self, character_name, char_class, race):
        origin = random.choice(self.locations)
        motivation = random.choice(self.motivations)
        trait = random.choice(self.personality_traits)
        trait2 = random.choice(self.personality_traits)
        while trait2 == trait:
            trait2 = random.choice(self.personality_traits)

        backstory = (
            f"{character_name} is a {trait} and {trait2} {race} {char_class} "
            f"who hails from {origin}. "
            f"They have spent years {motivation}, and their journey has shaped them "
            f"into the adventurer they are today. "
            f"Those who cross their path rarely forget the encounter."
        )
        return backstory

    def generate_random_character(self):
        name = self.generate_name()
        char_class = random.choice(self.classes)
        race = random.choice(self.races)
        level = random.randint(1, 20)
        base_attrs = [random.randint(1, 20) for _ in range(5)]

        character = {
            "name": name,
            "class": char_class,
            "race": race,
            "level": level,
            "attributes": [],
            "base_attributes": base_attrs,
            "skills": set(),
            "skill_levels": {},
            "inventory": []
        }
        return character

    def generate_quest(self):
        quest_types = ["Defeat", "Retrieve", "Escort", "Explore", "Investigate", "Protect"]
        quest_targets = [
            "the ancient dragon in the mountain caves",
            "the stolen crown from the thieves guild",
            "the merchant caravan through bandit territory",
            "the ruins of the lost elven city",
            "the mysterious disappearances in the village",
            "the shrine from the undead horde"
        ]
        reward_types = ["gold", "a rare weapon", "an enchanted artifact", "land and title", "a magical skill tome"]

        quest_type = random.choice(quest_types)
        target = random.choice(quest_targets)
        reward = random.choice(reward_types)
        giver = self.generate_name()

        quest = (
            f"Quest: {quest_type} {target}.\n"
            f"Given by: {giver}\n"
            f"Reward: {reward}\n"
            f"Details: {self.faker.sentence(nb_words=20)}"
        )
        return quest

    def generate_character_description(self, character):
        age = random.randint(18, 120)
        height_options = ["short", "average height", "tall", "towering"]
        build_options = ["lean", "stocky", "muscular", "slim", "broad-shouldered"]
        feature_options = ["piercing eyes", "a long scar", "braided hair", "a weathered face", "sharp cheekbones"]

        height = random.choice(height_options)
        build = random.choice(build_options)
        feature = random.choice(feature_options)

        description = (
            f"{character['name']} is a {height}, {build} {character.get('race', 'unknown')} "
            f"with {feature}. Aged around {age}, they carry themselves with the confidence "
            f"of an experienced {character.get('class', 'adventurer')} of level {character.get('level', 1)}."
        )
        return description