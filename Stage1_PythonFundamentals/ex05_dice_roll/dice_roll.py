import random

# Function to roll a dice
def roll_dice():
    return random.randint(1, 6)

# Display result
print(f"You rolled a {roll_dice()}")
