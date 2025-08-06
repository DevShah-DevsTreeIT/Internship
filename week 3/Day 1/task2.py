##### this is a 
def create_character(name="Hero", *skills, **traits):
    print(f"Character Name: {name}\n")
    
    if skills:
        print("Skills:")
        for skill in skills:
            print(f" - {skill}")
    else:
        print("\nNo skills added.")

    if traits:
        print("\nTraits:")
        for key, value in traits.items():
            print(f" - {key.capitalize()}: {value}")
    else:
        print("\nNo special traits.")


# 1. Just using default
create_character()

# 2. With name, skills, and traits
create_character("Max", "Sword", "Shield", level=5, team="Red")


# 3. With name and skills
create_character("Spiderman", "Genius-Level Intellect,Super Strength", "Spider-Sense")