# T'Keyah Jefferies
# 12/10/2025
# Final Project - Text-Based Game
# Simple glam spa game where a stylist and a client "battle" using health.
# Uses loops, functions, dictionaries, and the random and time modules.

import random
import time


def pause():
    """Small pause so the text does not all appear at once."""
    time.sleep(0.7)


def create_stylist():
    """
    Create the main character for the game.
    This is a value-returning function (returns a dictionary).
    """
    print("=== Create Your Glam Stylist ✨ ===")
    name = input("Enter stylist name: ").strip()
    if name == "":
        name = "Stylist"

    print("Choose a vibe:")
    print("1) Lash Tech 👁️")
    print("2) Hair Stylist 💇‍♀️")
    print("3) Nail Tech 💅")

    vibe_choice = input("> ").strip()
    if vibe_choice == "2":
        role = "Hair Stylist"
    elif vibe_choice == "3":
        role = "Nail Tech"
    else:
        role = "Lash Tech"

    # main character as a dictionary
    stylist = {
        "name": name,
        "role": role,
        "health": 20,        # how much energy she has left
        "strength": 5,       # how strong her glam skills are
        "confidence": 8,     # how confident she feels
        "mood": "chill 🙂",
        "inventory": {       # inventory as another dictionary
            "iced_coffee": 1,
            "lip_gloss": True
        }
    }

    print(f"\nCreated stylist: {stylist['name']} the {stylist['role']} is ready for a glam day! 💖")
    pause()
    return stylist


def create_client():
    """
    Create a random client for the stylist to work with.
    This also returns a dictionary.
    """
    client_names = ["Birthday Girl", "Bride-To-Be", "Influencer", "Soft Girl", "Busy Mom"]
    name = random.choice(client_names)

    # random stats for the client
    client = {
        "name": name,
        "health": random.randint(10, 20),    # how grumpy / stressed they start
        "strength": random.randint(3, 7),    # how dramatic they can be
        "mood": "unsure 😐"
    }

    print(f"\nA new client walks in: {client['name']} 💫")
    pause()
    return client


def show_character(character):
    """
    Non-value returning function that prints character attributes.
    Works for both stylist and client dictionaries.
    """
    print("\n--- Character Info ---")
    for key, value in character.items():
        print(f"{key}: {value}")
    print("----------------------")
    pause()


def show_menu():
    """Display the main menu options. Non-value returning."""
    print("\n===== Glam Spa Game Menu =====")
    print("1) Create / Re-create Stylist")
    print("2) Create / Re-roll Client")
    print("3) Show Stylist")
    print("4) Show Client")
    print("5) Stylist Gives Glow-Up (Attack)")
    print("6) Client Brings Drama (Attack)")
    print("7) Stylist Takes a Break (Heals)")
    print("8) Exit Game")
    print("===============================")


def apply_attack(attacker, defender):
    """
    Value-returning function that calculates damage and updates defender health.
    Returns the damage done as an integer.
    """
    base_damage = attacker["strength"]
    random_bonus = random.randint(0, 2)
    damage = base_damage + random_bonus

    defender["health"] -= damage
    if defender["health"] < 0:
        defender["health"] = 0

    return damage


def stylist_glow_up(stylist, client):
    """Stylist 'attacks' by giving a glow-up. Non-value returning."""
    if stylist is None or client is None:
        print("You need both a stylist and a client created first.")
        pause()
        return

    print(f"\n{stylist['name']} starts the glow-up on {client['name']}... ✨")
    pause()
    damage = apply_attack(stylist, client)
    print(f"{stylist['name']}'s skills reduce {client['name']}'s stress by {damage} points.")
    print(f"{client['name']}'s health (stress level) is now {client['health']}.")

    stylist["mood"] = "focused 😐"

    if client["health"] == 0:
        print(f"{client['name']} is fully relaxed and obsessed with the look. 💕")
        client["mood"] = "glowing 😌"
    else:
        client["mood"] = "getting happier 💗"

    pause()


def client_drama(client, stylist):
    """Client 'attacks' by bringing drama. Non-value returning."""
    if stylist is None or client is None:
        print("You need both a stylist and a client created first.")
        pause()
        return

    print(f"\n{client['name']} starts nitpicking the look and scrolling TikTok sounds out loud... 🙄")
    pause()
    damage = apply_attack(client, stylist)
    print(f"{client['name']}'s drama drains {damage} health from {stylist['name']}.")
    print(f"{stylist['name']}'s health is now {stylist['health']}.")

    stylist["confidence"] -= 1
    if stylist["confidence"] < 0:
        stylist["confidence"] = 0

    if stylist["health"] == 0:
        print(f"{stylist['name']} is completely drained and needs to close the station. 😴")
        stylist["mood"] = "exhausted 🥱"
    elif stylist["confidence"] == 0:
        stylist["mood"] = "over it 😤"
    else:
        stylist["mood"] = "stressed 😓"

    pause()


def stylist_break(stylist):
    """Stylist takes a break and heals. Non-value returning."""
    if stylist is None:
        print("You need to create a stylist first.")
        pause()
        return

    print(f"\n{stylist['name']} takes a quick self-care break. 🧋")
    if stylist["inventory"]["iced_coffee"] > 0:
        print("She sips her iced coffee and scrolls cute hairstyles. ☕📱")
        stylist["inventory"]["iced_coffee"] -= 1
        heal = random.randint(3, 6)
    else:
        print("No coffee left, just deep breaths and vibes. 😮‍💨")
        heal = random.randint(1, 3)

    stylist["health"] += heal
    if stylist["health"] > 20:
        stylist["health"] = 20

    stylist["confidence"] += 1
    if stylist["confidence"] > 10:
        stylist["confidence"] = 10

    stylist["mood"] = "reset 🙂"

    print(f"{stylist['name']} recovers {heal} health.")
    print(f"Health is now {stylist['health']}, confidence is now {stylist['confidence']}.")
    pause()


def main():
    """
    Main function that runs the game loop.
    All other functions are called from here.
    """
    print("Welcome to the Glam Spa Shift Game! 💅✨")
    print("Create a stylist and a client, then see how the appointment goes.\n")
    pause()

    stylist = None
    client = None

    # main game loop (loop requirement)
    running = True
    while running:
        show_menu()
        choice = input("Choose an option: ").strip()

        if choice == "1":
            stylist = create_stylist()
        elif choice == "2":
            client = create_client()
        elif choice == "3":
            if stylist is None:
                print("No stylist created yet.")
                pause()
            else:
                show_character(stylist)
        elif choice == "4":
            if client is None:
                print("No client created yet.")
                pause()
            else:
                show_character(client)
        elif choice == "5":
            stylist_glow_up(stylist, client)
        elif choice == "6":
            client_drama(client, stylist)
        elif choice == "7":
            stylist_break(stylist)
        elif choice == "8":
            print("\nEnding the glam day. Thanks for playing! 🌸")
            running = False
        else:
            print("Invalid choice. Please pick from the menu.")
            pause()

        # end game if stylist is totally done
        if stylist is not None and stylist["health"] == 0:
            print("\nYour stylist has no energy left. Appointment day is over. 💤")
            running = False

    print("Goodbye.")


if __name__ == "__main__":
    main()
