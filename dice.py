import random 
import itertools


#  Making dice rollers to make code cleaner

def roll_d6(num):
    dice_roll = 0
    for num in itertools.repeat(None, num):
        dice_roll += random.randint(1,6)
    return dice_roll

def roll_d8(num):
    dice_roll = 0
    for num in itertools.repeat(None, num):
        dice_roll += random.randint(1,8)
    return dice_roll

def roll_d20():
    return random.randint(1,20)