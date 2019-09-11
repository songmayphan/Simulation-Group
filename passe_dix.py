# Laura Celis
# Problem 1: Passe Dix
# CMS 380, Fall 2019

import random

def simulate(sim=1):
    # Roll 3 dices
    die1 = random.randint(1,6)
    die2 = random.randint(1,6)
    die3 = random.randint(1,6)
    
    sum = die1 + die2 + die3
    # Check for wins and loses
    if sum > 10:
        return True
    else:
        return False

def main():
    rolling = 0
    countTrue = 0
    calc_wins = 0
    while rolling < 1000:
        rolling += 1
        responses = simulate(1000)
        if responses is True:
            countTrue += 1
            calc_wins = (countTrue / rolling) * 100
        
    print('Winning Percentage: ' + '{0:.0f}%'.format(calc_wins))

if __name__ == '__main__':
    main()