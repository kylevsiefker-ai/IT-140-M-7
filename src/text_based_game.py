"""Project Two starter for the student's text-based adventure game."""

# Name: [Kyle Siefker]
# Course: IT 140 - Introduction to Scripting
# Project Two: Text-Based Adventure Game


def show_instructions():
    """Display the game objective and available commands."""
   print("\nAbandoned Facility: Text Adventure")
    print("Collect all six items before entering the Main Entrance.")
    print("Avoid Dr. Voss until you have collected everything.")
    print("\nMovement commands: go north, go south, go east, go west")
    print("Item command: get item name")
    print("Type quit to exit the game.")

    pass


def show_status(current_room, inventory, rooms):
    """Display the player's current game status."""
     print("\n" + "-" * 35)
    print("You are in the", current_room)
    print("Inventory:", inventory)

    if "item" in rooms[current_room]:
        print("You see:", rooms[current_room]["item"])
    else:
        print("There are no items in this room.")

    print("-" * 35)
    pass


def main():
    """Run the main gameplay loop."""
     # Create the room connections and room items.
    rooms = {
        "Security Office": {
            "north": "Laboratory",
            "east": "Computer Lab"
        },
        "Laboratory": {
            "south": "Security Office",
            "east": "Research Library",
            "item": "Chemical Sample"
        },
        "Research Library": {
            "west": "Laboratory",
            "south": "Storage Room",
            "item": "Keycard"
        },
        "Storage Room": {
            "north": "Research Library",
            "east": "Generator Room",
            "west": "Computer Lab",
            "item": "Flashlight"
        },
        "Computer Lab": {
            "west": "Security Office",
            "east": "Storage Room",
            "north": "Medical Bay",
            "item": "Access Chip"
        },
        "Medical Bay": {
            "south": "Computer Lab",
            "east": "Main Entrance",
            "item": "First Aid Kit"
        },
        "Generator Room": {
            "west": "Storage Room",
            "north": "Main Entrance",
            "item": "Power Cell"
        },
        "Main Entrance": {
            "west": "Medical Bay",
            "south": "Generator Room",
            "item": "Dr. Voss"
        }
    }

    # Set the player's starting room and inventory.
    current_room = "Security Office"
    inventory = []
    total_items = 6

    # Display the instructions before starting the game.
    show_instructions()

    # Continue until the player wins, loses, or quits.
    while True:
        show_status(current_room, inventory, rooms)
        command = input("Enter your move: ").strip().lower()

        # Allow the player to exit.
        if command == "quit":
            print("Thanks for playing the game. Goodbye!")
            break

        # Handle movement commands.
        elif command.startswith("go "):
            direction = command[3:].strip()

            if direction in rooms[current_room]:
                current_room = rooms[current_room][direction]
                print("You moved to the", current_room)

                # Check whether the player entered the villain's room.
                if current_room == "Main Entrance":
                    if len(inventory) == total_items:
                        print(
                            "\nCongratulations! You collected all items "
                            "and escaped Dr. Voss!"
                        )
                    else:
                        print("\nDr. Voss catches you! GAME OVER!")

                    print("Thanks for playing the game. Hope you enjoyed it.")
                    break
            else:
                print("You cannot go that way. Try another direction.")

        # Handle item collection commands.
        elif command.startswith("get "):
            requested_item = command[4:].strip()

            # Find the item available in the current room.
            room_item = rooms[current_room].get("item")

            if room_item is None:
                print("There is no item to collect in this room.")
            elif room_item == "Dr. Voss":
                print("You cannot collect Dr. Voss!")
            elif requested_item == room_item.lower():
                if room_item not in inventory:
                    inventory.append(room_item)
                    print("You collected:", room_item)
                else:
                    print("You already collected this item.")
            else:
                print("That item is not available in this room.")

        # Handle commands that are not recognized.
        else:
            print(
                "Invalid command. Use 'go direction' or 'get item name'."
            )

    pass


if __name__ == "__main__":
    main()
