import pandas as pd
import os


class StatisticalAnalyzer:

    def __init__(self):
        self.output_folder = "exports"
        if not os.path.exists(self.output_folder):
            os.makedirs(self.output_folder)

    def characters_to_dataframe(self, characters):
        rows = []
        for character in characters:
            attrs = character.get("attributes") or character.get("base_attributes") or [0, 0, 0, 0, 0]
            row = {
                "name": character.get("name", ""),
                "class": character.get("class", ""),
                "race": character.get("race", ""),
                "level": character.get("level", 1),
                "damage": attrs[0] if len(attrs) > 0 else 0,
                "dexterity": attrs[1] if len(attrs) > 1 else 0,
                "intelligence": attrs[2] if len(attrs) > 2 else 0,
                "constitution": attrs[3] if len(attrs) > 3 else 0,
                "charisma": attrs[4] if len(attrs) > 4 else 0,
                "skill_count": len(character.get("skills", [])),
                "inventory_count": len(character.get("inventory", []))
            }
            rows.append(row)
        return pd.DataFrame(rows)

    def print_summary_stats(self, characters):
        if not characters:
            print("No characters to analyze.")
            input("Press Enter to continue...")
            return

        df = self.characters_to_dataframe(characters)
        stat_cols = ["level", "damage", "dexterity", "intelligence", "constitution", "charisma"]

        print("\n" + "=" * 60)
        print("ROSTER STATISTICAL SUMMARY")
        print("=" * 60)
        print(f"Total Characters: {len(df)}")
        print()

        for col in stat_cols:
            print(f"{col.capitalize():<20} Mean: {df[col].mean():.2f}   Median: {df[col].median():.2f}   Min: {df[col].min():.2f}   Max: {df[col].max():.2f}")

        print("=" * 60)
        input("\nPress Enter to continue...")

    def print_filtered_by_class(self, characters, class_name):
        df = self.characters_to_dataframe(characters)
        filtered = df[df["class"].str.lower() == class_name.lower()]
        if filtered.empty:
            print(f"No characters found with class '{class_name}'.")
        else:
            print(f"\nCharacters with class '{class_name}':")
            print(filtered[["name", "level", "damage", "dexterity", "intelligence", "constitution", "charisma"]].to_string(index=False))
        input("\nPress Enter to continue...")

    def print_sorted_by(self, characters, column):
        valid_cols = ["level", "damage", "dexterity", "intelligence", "constitution", "charisma", "skill_count", "inventory_count"]
        if column not in valid_cols:
            print(f"Invalid column. Choose from: {', '.join(valid_cols)}")
            input("Press Enter to continue...")
            return

        df = self.characters_to_dataframe(characters)
        sorted_df = df.sort_values(by=column, ascending=False)
        print(f"\nCharacters sorted by {column} (highest first):")
        print(sorted_df[["name", "class", "race", "level", column]].to_string(index=False))
        input("\nPress Enter to continue...")

    def export_to_csv(self, characters):
        if not characters:
            print("No characters to export.")
            input("Press Enter to continue...")
            return

        df = self.characters_to_dataframe(characters)
        path = os.path.join(self.output_folder, "characters_export.csv")
        df.to_csv(path, index=False)
        print(f"Exported {len(df)} characters to {path}")
        input("\nPress Enter to continue...")

    def import_from_csv(self, characters):
        path = os.path.join(self.output_folder, "characters_export.csv")
        if not os.path.exists(path):
            print(f"No export file found at {path}. Export first.")
            input("Press Enter to continue...")
            return characters

        df = pd.read_csv(path)
        existing_names = {c["name"] for c in characters}
        added = 0

        for _, row in df.iterrows():
            if row["name"] in existing_names:
                continue
            new_character = {
                "name": row["name"],
                "class": row["class"],
                "race": row["race"],
                "level": int(row["level"]),
                "attributes": [],
                "base_attributes": [
                    float(row["damage"]),
                    float(row["dexterity"]),
                    float(row["intelligence"]),
                    float(row["constitution"]),
                    float(row["charisma"])
                ],
                "skills": set(),
                "skill_levels": {},
                "inventory": []
            }
            characters = list(characters)
            characters.append(new_character)
            characters = tuple(characters)
            existing_names.add(row["name"])
            added += 1

        print(f"Imported {added} new character(s) from {path}.")
        input("\nPress Enter to continue...")
        return characters

    def print_top_characters(self, characters, stat, top_n=3):
        valid = ["level", "damage", "dexterity", "intelligence", "constitution", "charisma"]
        if stat not in valid:
            print(f"Invalid stat. Choose from: {', '.join(valid)}")
            input("Press Enter to continue...")
            return

        df = self.characters_to_dataframe(characters)
        top = df.nlargest(top_n, stat)[["name", "class", "race", stat]]
        print(f"\nTop {top_n} characters by {stat}:")
        print(top.to_string(index=False))
        input("\nPress Enter to continue...")