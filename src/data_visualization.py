import matplotlib.pyplot as plt
import numpy as np
import os


class DataVisualization:

    def __init__(self):
        self.output_folder = "docs\\charts"
        if not os.path.exists(self.output_folder):
            os.makedirs(self.output_folder)

    def get_character_attributes(self, character):
        keys = ["dmg", "dex", "int", "con", "cha"]
        labels = ["Damage", "Dexterity", "Intelligence", "Constitution", "Charisma"]
        values = []
        if character.get("attributes") and len(character["attributes"]) == 5:
            values = [float(v) for v in character["attributes"]]
        elif character.get("base_attributes") and len(character["base_attributes"]) == 5:
            values = [float(v) for v in character["base_attributes"]]
        else:
            values = [0.0, 0.0, 0.0, 0.0, 0.0]
        return labels, values

    def show_and_maybe_save(self, fig, default_filename):
        plt.show()
        save = input("Save this chart? (y/n): ").strip().lower()
        if save == 'y':
            path = os.path.join(self.output_folder, default_filename)
            fig.savefig(path)
            print(f"Chart saved to {path}")
        plt.close(fig)

    def radar_chart(self, character):
        labels, values = self.get_character_attributes(character)
        num_vars = len(labels)
        angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
        values_plot = values + [values[0]]
        angles += angles[:1]

        fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))
        ax.plot(angles, values_plot, color='blue', linewidth=2)
        ax.fill(angles, values_plot, color='blue', alpha=0.25)
        ax.set_thetagrids(np.degrees(angles[:-1]), labels)
        ax.set_title(f"{character['name']} - Stat Radar", size=14, pad=20)

        self.show_and_maybe_save(fig, f"{character['name']}_radar.png")

    def bar_chart(self, character):
        labels, values = self.get_character_attributes(character)

        fig, ax = plt.subplots(figsize=(8, 5))
        ax.bar(labels, values, color='steelblue')
        ax.set_title(f"{character['name']} - Attribute Bar Chart")
        ax.set_ylabel("Value")
        ax.set_xlabel("Attribute")

        self.show_and_maybe_save(fig, f"{character['name']}_bar.png")

    def comparison_bar_chart(self, characters):
        if not characters:
            print("No characters to compare.")
            return

        labels = ["Damage", "Dexterity", "Intelligence", "Constitution", "Charisma"]
        x = np.arange(len(labels))
        width = 0.8 / len(characters)

        fig, ax = plt.subplots(figsize=(10, 6))

        for i, character in enumerate(characters):
            _, values = self.get_character_attributes(character)
            offset = (i - len(characters) / 2) * width + width / 2
            ax.bar(x + offset, values, width, label=character["name"])

        ax.set_title("Character Attribute Comparison")
        ax.set_xticks(x)
        ax.set_xticklabels(labels)
        ax.set_ylabel("Value")
        ax.legend()

        names = "_vs_".join(c["name"] for c in characters)
        self.show_and_maybe_save(fig, f"{names}_comparison.png")

    def class_distribution_chart(self, characters):
        if not characters:
            print("No characters to analyze.")
            return

        class_counts = {}
        for character in characters:
            char_class = character.get("class", "Unknown")
            if char_class not in class_counts:
                class_counts[char_class] = 0
            class_counts[char_class] += 1

        fig, ax = plt.subplots(figsize=(7, 7))
        ax.pie(class_counts.values(), labels=class_counts.keys(), autopct="%1.1f%%")
        ax.set_title("Class Distribution")

        self.show_and_maybe_save(fig, "class_distribution.png")

    def level_progression_chart(self, characters):
        if not characters:
            print("No characters to display.")
            return

        names = [c["name"] for c in characters]
        levels = [c.get("level", 1) for c in characters]

        fig, ax = plt.subplots(figsize=(10, 5))
        ax.bar(names, levels, color='green')
        ax.set_title("Character Level Progression")
        ax.set_ylabel("Level")
        ax.set_xlabel("Character")
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()

        self.show_and_maybe_save(fig, "level_progression.png")