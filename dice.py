from random import randint
import re

#roll dice
def roll_many(x, n, p):
    for i in range(x):
        roll = randint(1, n)
        rolls.append(roll)
    print(rolls)
    print(sum(rolls) + p)

#single roll
def single_roll():
    num_str = re.split(r'[Dd+\s]\s*', dices)
    num_int = list(map(int, num_str))
    dice = num_int[0]
    side = num_int[1]
    if  len(num_int) < 3:
        plus = 0
    else:    
        plus = sum(num_int[2:])
    roll_many(dice, side, plus)

#repeat roll
def repeat_roll():
    num_str = re.split(r'[Dd+\s]\s*', dices)
    num_int = list(map(int, num_str))
    dice = num_int[1]
    side = num_int[2]
    if  len(num_int) < 4:
        plus = 0
    else:    
        plus = sum(num_int[3:])
    for j in range(num_int[0]):
        roll_many(dice, side, plus)
        rolls.clear()

while True:
    rolls = []
    dices = input('請打骰子:')
    if dices == 'q':
        break
    elif dices[1] == ' ':
        repeat_roll()
    else:    
        single_roll()