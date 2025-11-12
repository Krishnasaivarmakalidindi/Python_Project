"""
Rainbow Quest Adventure - Simple Version

Goal: Keep code easy for beginners.
- Small functions with comments
- Clear choices and short text
- No extra libraries
"""

import random

# Minimal emojis to keep it fun but simple.
E = {
    "forest": "🌳",
    "cave": "🕳️",
    "river": "🌊",
    "mountain": "⛰️",
    "temple": "🏛️",
    "key": "🗝️",
    "map": "🗺️",
    "treasure": "💎",
    "wolf": "🐺",
    "statue": "🗿",
    "ok": "✅",
}

def choose(valid):
    """Ask until the user types one of the valid words."""
    while True:
        ans = input("> ").strip().lower()
        if ans in valid:
            return ans
        print(f"Please type: {', '.join(valid)}")

def intro():
    """Show the simple intro card."""
    print("=" * 40)
    print("Rainbow Quest Adventure 🌈")
    print("Hero: A kid explorer with simple tools.")
    print(f"World: Forest {E['forest']} Cave {E['cave']} River {E['river']} Mountain {E['mountain']} Temple {E['temple']}")
    print("Enemies: Animals, bandits, statues (friendly challenge).")
    print("Puzzles: Levers, lights, symbols.")
    print("Boss: Guardian on the mountain.")
    print("Goal: Find treasure and help friends.")
    print("=" * 40)

def fight():
    """Very simple and safe fight.
    You choose: hit, block, or dodge.
    You are always safe after 1-2 tries.
    """
    print("Fight! Choose: hit / block / dodge")
    while True:
        move = choose({"hit", "block", "dodge"})
        # 70% chance to be safe each try to keep it easy.
        if random.random() < 0.7:
            print(f"You are safe! {E['ok']}")
            return True
        print("You step back. Try again.")

def puzzle_lever():
    """Pick left or right. Random success."""
    print("Puzzle: Pull a lever. left or right?")
    ans = choose({"left", "right"})
    good = random.choice(["left", "right"]) == ans
    print("Click! A bridge lowers." if good else "Clank! Not this time.")
    return good

def puzzle_lights():
    """Type 123 to light torches in order."""
    print("Puzzle: Light torches in order. Type 123.")
    ans = input("> ").strip()
    ok = ans == "123"
    print("They glow bright!" if ok else "They go out.")
    return ok

def puzzle_symbols():
    """Choose a symbol. Always ok (keeps it friendly)."""
    print("Puzzle: Pick a symbol. sun / moon / star")
    _ = choose({"sun", "moon", "star"})
    print("Great pick!")
    return True

def forest(state):
    """Forest start. Pick an item. Meet a wolf. Choose next area."""
    print(f"Forest {E['forest']}. Birds sing.")
    print("Pick one: stick / apple / none")
    pick = choose({"stick", "apple", "none"})
    if pick == "stick":
        state["tools"].add("stick")
        print("You take the stick.")
    elif pick == "apple":
        state["items"].append("apple")
        print("You take the apple.")

    print(f"A wolf {E['wolf']} blocks the path.")
    fight()
    print("The wolf runs away.")
    print("Go to: cave or river")
    return "cave" if choose({"cave", "river"}) == "cave" else "river"

def river(state):
    """At the river, a lever may give a key. Then go to mountain."""
    print(f"River {E['river']}. Water flows.")
    if puzzle_lever():
        print(f"You find a key! {E['key']}")
        state["items"].append("key")
    print("A bridge leads to the mountain.")
    return "mountain"

def cave(state):
    """In the cave, light torches and maybe find a map. Then go to temple."""
    print(f"Cave {E['cave']}. It is dark.")
    print("Light a torch? yes / no")
    if choose({"yes", "no"}) == "yes":
        state["tools"].add("torch")
        print("The cave is bright.")
    print(f"A statue {E['statue']} moves.")
    fight()
    if puzzle_lights():
        print(f"You find a map! {E['map']}")
        state["items"].append("map")
    print("Go to the temple.")
    return "temple"

def temple(state):
    """In the temple, symbols open a chest if you have a key."""
    print(f"Temple {E['temple']}. It is calm.")
    puzzle_symbols()
    print("A chest is here. It needs a key.")
    if "key" in state["items"]:
        print("Click! The chest opens.")
        state["items"].append("treasure")
        print(f"Treasure found! {E['treasure']}")
    else:
        print("No key yet. You can return later.")
    print("Stairs go up the mountain.")
    return "mountain"

def mountain(state):
    """Final area with a friendly boss test."""
    print(f"Mountain {E['mountain']}. The wind is strong.")
    print("A friendly bandit says hello. A quick duel.")
    fight()
    print("At the top, the Rainbow Guardian smiles.")
    print("Final test. Win three times.")
    wins = 0
    while wins < 3:
        print("Choose: hit / block / dodge")
        if fight():
            wins += 1
            print(f"Good job! {wins}/3")
    if "treasure" in state["items"]:
        print("You protected the treasure.")
    print("Friends cheer! You win the Rainbow Quest! 🎉")
    return "end"

def game():
    """Main loop: ask name, choose start, move through areas."""
    intro()
    name = input("What is your name? ").strip() or "Explorer"
    print(f"Welcome, {name}!")
    state = {"items": [], "tools": set()}

    # Choose the starting place.
    print("Start in: forest or cave")
    place = "forest" if choose({"forest", "cave"}) == "forest" else "cave"

    # Move between places until the game ends.
    while True:
        if place == "forest":
            place = forest(state)
        elif place == "river":
            place = river(state)
        elif place == "cave":
            place = cave(state)
        elif place == "temple":
            place = temple(state)
        elif place == "mountain":
            place = mountain(state)
        elif place == "end":
            break
        else:
            print("You sit and rest. The sky is bright.")
            break

if __name__ == "__main__":
    game()
