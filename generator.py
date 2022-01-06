import random 
import itertools

import dice


# Create a stat block, save into a dictionary 

def create_stats():
    stat_block = {
        "HP": dice.roll_d8(1) + 4, 
        "Power": dice.roll_d6(3),
        "Speed": dice.roll_d6(3),
        "Durability": dice.roll_d6(3),
        "Precision": dice.roll_d6(3),
        "Cunning": dice.roll_d6(3),
        "Charisma": dice.roll_d6(3)
    }
    return stat_block

def print_stats(stat_block):
    # This should be the same as above, but does not test
    for key, value in stat_block.items():
        print (key, value)

def level_up(stats):
    # HP is increased by 1d8+1 per level
    HP_increase = dice.roll_d8(1) + 1
    stats["HP"] += HP_increase

    # For each non-HP stat
    # If value is less than 1d20, increase, otherwise don't
    for stat_type, stat_value in stats.items():
        if stat_type == "HP":
            continue
        increase_check = dice.roll_d20()
        if increase_check > stat_value:
            stats[stat_type] += 1

    return stats



# Start creating a character...

current_stats = create_stats()

print ('Your starting stats are...')
print_stats(current_stats)

# Ask for level-up info...
# TODO: Maybe clean this up?
while True:
    try:
        current_level = int(input('Please input your current level, from 1 to 10. \n'))
        print ('Your new stats at level ' + str(current_level) + ' are...')
    except ValueError:
        print("Hey! that's not a number")
        continue
    # made it past the exception, so input is a number
    if current_level <= 0 or current_level >= 11:
        print ('Need a number between 1 and 10')
        continue 
    break # Exit the loop by changing the while condition to false

# Start leveling the character, then print the result
for level in range(1, current_level):
    level_up(current_stats)

print_stats(current_stats)
    

    

