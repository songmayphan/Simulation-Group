# Laura Celis 
# Problem 2: Craps
# CMS 380, Fall 2019

import random 

def simulate(pass_bet=1):
    # Roll 2 dices
    die1 = random.randint(1,6)
    die2 = random.randint(1,6)
    
    sum = die1 + die2 
    # Check for wins and loses
    if sum == 7 or sum == 11:
        return True
    elif sum == 2 or sum == 3 or sum == 12:
        return False
    else:
        # Sum becomes the point
        point = sum
        while sum != point or sum != 7:
            # Roll again
            die1 = random.randint(1,6)
            die2 = random.randint(1,6)
        
            sum = die1 + die2
            # Roll another point val or 7
            if sum == point:
                return True
            elif sum == 7:
                return False

## MAIN ##
def main():
    rolling = 0
    countTrue = 0
    calc_wins = 0
    while rolling < 1000:
        rolling += 1
        responses = simulate(1000)
        # Check for each True response and count
        if responses is True:
            countTrue += 1
            calc_wins = (countTrue / rolling) * 100.00
    print('Winning "Pass" Bet Percentage: ' + '{0:.0f}%'.format(calc_wins))

if __name__ == '__main__':
    main()