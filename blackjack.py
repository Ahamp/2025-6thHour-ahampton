import random
import time

# --- Player setup ---
player = {
    "name": "",
    "health": 100,
    "attack": 10,
    "level": 1,
    "xp": 0
}

# --- Enemy setup ---
enemies = [
    {"name": "Slime", "health": 30, "attack": 5, "xp": 10},
    {"name": "Goblin", "health": 50, "attack": 8, "xp": 20},
    {"name": "Orc", "health": 80, "attack": 12, "xp": 30},
    {"name": "Dragon", "health": 150, "attack": 20, "xp": 50}
]

# --- Helper functions ---
def slow_print(text, delay=0.03):
    """Prints text slowly for dramatic effect."""
    for c in text:
        print(c, end="", flush=True)
        time.sleep(delay)
    print()

def battle(enemy):
    """Fight an enemy until someone loses."""
    slow_print(f"\nA wild {enemy['name']} appears!")
    enemy_health = enemy["health"]

    while enemy_health > 0 and player["health"] > 0:
        slow_print(f"\n{player['name']}'s Health: {player['health']}")
        slow_print(f"{enemy['name']}'s Health: {enemy_health}")
        slow_print("Choose an action:\n1. Attack\n2. Heal\n3. Run")

        choice = input("> ")
        if choice == "1":
            damage = random.randint(player["attack"] - 3, player["attack"] + 3)
            slow_print(f"You strike the {enemy['name']} for {damage} damage!")
            enemy_health -= damage
        elif choice == "2":
            heal = random.randint(10, 20)
            player["health"] = min(100, player["health"] + heal)
            slow_print(f"You heal yourself for {heal} HP.")
        elif choice == "3":
            slow_print("You run away!")
            return False
        else:
            slow_print("Invalid choice!")
            continue

        if enemy_health > 0:
            enemy_damage = random.randint(enemy["attack"] - 2, enemy["attack"] + 2)
            slow_print(f"The {enemy['name']} attacks you for {enemy_damage} damage!")
            player["health"] -= enemy_damage

    if player["health"] <= 0:
        slow_print("\nYou have been defeated... Game Over.")
        return True
    else:
        slow_print(f"\nYou defeated the {enemy['name']}!")
        player["xp"] += enemy["xp"]
        level_up()
        return False

def level_up():
    """Check if the player can level up."""
    if player["xp"] >= player["level"] * 30:
        player["level"] += 1
        player["attack"] += 5
        player["health"] = 100
        slow_print(f"\n*** You leveled up! You are now Level {player['level']}! ***")

# --- Game starts ---
slow_print("Welcome, hero! What is your name?")
player["name"] = input("> ")

slow_print(f"\nGreetings, {player['name']}! Your adventure begins now...")
game_over = False

while not game_over:
    slow_print("\nYou are in a dark forest. What will you do?")
    slow_print("1. Explore\n2. Rest\n3. Check Stats\n4. Quit")
    action = input("> ")

    if action == "1":
        enemy = random.choice(enemies)
        game_over = battle(enemy)
    elif action == "2":
        heal = random.randint(15, 25)
        player["health"] = min(100, player["health"] + heal)
        slow_print(f"You rest and recover {heal} HP.")
    elif action == "3":
        slow_print(f"\n{player['name']} - Level {player['level']}")
        slow_print(f"Health: {player['health']}")
        slow_print(f"Attack: {player['attack']}")
        slow_print(f"XP: {player['xp']}")
    elif action == "4":
        slow_print("Farewell, brave hero!")
        break
    else:
        slow_print("Invalid action!")

slow_print("\nThanks for playing!")
