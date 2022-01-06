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


HP = roll_d8(1) + 4 
Power = roll_d6(3)
Speed = roll_d6(3)
Durability = roll_d6(3)
Precision = roll_d6(3)
Cunning = roll_d6(3)
Charisma = roll_d6(3)


print ('Your starting stats are...')
print ('HP is ' + str(HP))
print ('Power is ' + str(Power))
print ('Speed is ' + str(Speed))
print ('Durability is ' + str(Durability))
print ('Precision is ' + str(Precision))
print ('Cunning is ' + str(Cunning))
print ('Charisma is ' + str(Charisma))

while True:
    try:
        Currentlevel=int(input('Please input your current level, from 1 to 10. \n'))
        print ('Your new stats at level ' + str(Currentlevel) + ' are...')
    except ValueError:
        print("Hey! that's not a number")
        continue
    # made it past the exception, so input is a number
    if Currentlevel <= 0 or Currentlevel >= 11:
        print ('Need a number between 1 and 10')
        continue 
    break # Exit the loop by changing the while condition to false

while True:
    
    random_eight_hp = roll_d6(1) + 1 
    random_twenty_power = roll_d20()
    random_twenty_speed = roll_d20()
    random_twenty_durability = roll_d20()
    random_twenty_precision = roll_d20()
    random_twenty_cunning = roll_d20()
    random_twentychr = roll_d20()

    if random_eight_hp > 0:
        HP += random_eight_hp
    if random_twenty_power > Power:
        Power += 1 
    if random_twenty_speed > Speed:
        Speed += 1 
    if random_twenty_durability > Durability:
        Durability+= 1
    if random_twenty_precision  > Precision:
        Precision += 1 
    if random_twenty_cunning > Cunning:
        Cunning += 1 
    if random_twentychr > Charisma:
        Charisma += 1
    Currentlevel -= 1
    if Currentlevel < 2:
        break
    
print ('HP is ' + str(HP))
print ('Power is ' + str(Power))
print ('Speed is ' + str(Speed))
print ('Durability is ' + str(Durability))
print ('Precision is ' + str(Precision))
print ('Cunning is ' + str(Cunning))
print ('Charisma is ' + str(Charisma))
    
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
