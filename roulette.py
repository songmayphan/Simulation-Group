# Laura Celis
# Problem 4
# CMS FALL 2019

import random 
import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt

# Spin the wheel
def spin():
    # Black 
    black = [2,4,6,8,10,11,13,15,17,20,22,26,28,29,31,33,35]
    
    # Spin on a random number
    spin_num = random.randint(-1,36)

    # Check num is black
    if spin_num in black:
        return True
    else:
        return False

# Simulate a bankroll
def simulate(bankroll):
    bet = 1
    spins = 0
    # Loop until 100 spins
    while spins <= 100:
        spins += 1
        
        # Can't play anymore, return remaining 
        if bet > bankroll:
            return bankroll
        else:
            bankroll -= bet
            # Win, add to bankroll
            if spin():
                bankroll = bankroll + bet*2
                bet = 1
            # Lose, double the bet
            else: 
                bet *= 2
 
    return bankroll

## MAIN ##
def main():
    game_results = []
    start_bal = 255
    spins = 100
    for x in range(0,spins):
       game_results.append(simulate(start_bal))
    print(spins)

    plt.figure()
    plt.hist(game_results, spins)
    plt.title('Martingale Histogram')
    plt.xlabel('Values')
    plt.ylabel('Spins')
    plt.savefig('roulette_histogram.pdf', bbox_inches='tight')


if __name__ == '__main__':
    main()