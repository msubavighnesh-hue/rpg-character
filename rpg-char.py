def create_character(name, strength, intelligence, charisma):

    # Validate character name
    if not isinstance(name, str):
        return "The character name should be a string"

    if name == "":
        return "The character should have a name"

    if len(name) > 10:
        return "The character name is too long"

    if " " in name:
        return "The character name should not contain spaces"

    # Validate stats
    stats = [strength, intelligence, charisma]

    if not all(isinstance(stat, int) for stat in stats):
        return "All stats should be integers"

    if not all(stat >= 1 for stat in stats):
        return "All stats should be no less than 1"

    if not all(stat <= 4 for stat in stats):
        return "All stats should be no more than 4"

    if sum(stats) != 7:
        return "The character should start with 7 points"

    # Create character
    return (
        f"\n{name}\n"
        f"STR {'●' * strength}{'○' * (10 - strength)}\n"
        f"INT {'●' * intelligence}{'○' * (10 - intelligence)}\n"
        f"CHA {'●' * charisma}{'○' * (10 - charisma)}"
    )


# Get input from the user
print("=== RPG CHARACTER CREATOR ===")

name = input("Enter your character name: ")

strength = int(input("Enter Strength (1-4): "))
intelligence = int(input("Enter Intelligence (1-4): "))
charisma = int(input("Enter Charisma (1-4): "))

# Create and display character
result = create_character(name, strength, intelligence, charisma)

print("\n" + result)