import random 
from itertools import repeat

HP = random.randint(1,8) + 4 
Power = random.randint(1,6) + random.randint(1,6) + random.randint(1,6)
Speed = random.randint(1,6) + random.randint(1,6) + random.randint(1,6)
Durability = random.randint(1,6) + random.randint(1,6) + random.randint(1,6)
Precision = random.randint(1,6) + random.randint(1,6) + random.randint(1,6)
Cunning = random.randint(1,6) + random.randint(1,6) + random.randint(1,6)
Charisma = random.randint(1,6) + random.randint(1,6) + random.randint(1,6)


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
    
    random_eight_hp = random.randint(1,6) + 1 
    random_twenty_power = random.randint(1,20)
    random_twenty_speed = random.randint(1,20)
    random_twenty_durability = random.randint(1,20)
    random_twenty_precision = random.randint(1,20)
    random_twenty_cunning = random.randint(1,20)
    random_twentychr = random.randint(1,20)

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
    

