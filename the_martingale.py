import matplotlib
from random import randint
import numpy as np
matplotlib.use('Agg')  # <-- Required if you're using matplotilb in Mimir, see below
from matplotlib import pyplot as plt


def Simulate(bankroll, spinLimit):
    
    spins = 1
    bet = 1
    while spins <= spinLimit:
        if bankroll - bet < 0:
            break
        if Play() == 1:
            bankroll += bet
            bet = 1
        else:
            bankroll -= bet
            bet *= 2

        spins += 1
        
    return bankroll

def Play():
    spin = randint(0,37)
    pockets = [15, 4, 2, 17, 6, 13, 11, 8, 10, 24, 33, 20, 31, 22, 29, 28, 35, 26]
    result = -1
    if spin == 0 or spin == 37:
        return 0
    elif spin in(pockets):
        return 1
        
    return 0

def main():
    trials = 1000
    bankroll = 255
    spins = 100
    sim = 0
    loss = 0
    win = 0
    data = []
    acum_win = 0
    acum_loss = 0
    for i in range(trials):
        sim = Simulate(bankroll, spins)
        data.append(sim - bankroll)
        if sim > bankroll:
            win += 1
            acum_win += sim - bankroll
        else:
            loss += 1
            acum_loss += bankroll - sim

    print("Winnings: $" + str(acum_win))
    print("Losses: $" + str(acum_loss))
    print("% of Earnings: " + str((acum_win/(acum_win + acum_loss))*100 ) + " %")
    print("------------------------------------------")
    print("Losses: " + str(loss))
    print("Winnings: " + str(win))
    print("Stats: " + str(( win / (i + 1))*100) + " %")
    
    plt.figure()
    plt.hist(data, int(len(data)* 0.1))
    plt.title('Histogram - Problem 4')
    plt.xlabel('Data value')
    plt.ylabel('Frequency')
    plt.savefig('The_Martingale.png', bbox_inches='tight')

    

main()   
    
