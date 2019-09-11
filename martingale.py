import random
import matplotlib.pyplot as plot
import numpy as np

#Change this to only play Black

def main():

    bankroll = 255
    list = []
    allResMoney = 0
    
    #In each totalTries, you are going to have the number of totalSpins
    totalSpins = 100
    totalTries = 1000
    
    for i in range(totalTries):
        startingMoney = bankroll
        for x in range(totalSpins):
            if(startingMoney > 0):
                returnedMoney = simulate(startingMoney) 
                #list.append(returnedMoney) #previous had only list.append(bankroll)
                startingMoney += (returnedMoney - startingMoney)   
            
        list.append(startingMoney)
    
    for x in list:
        allResMoney += x
        
    averageEndMoney = allResMoney / len(list)
    
    #print("Starting money: " + str(bankroll) + ". Ending money: " + str(simulate(bankroll)))
    
    print(averageEndMoney)
    
    plot.hist(list, bins = 10, rwidth = 1)
    plot.savefig("martingaleHistogram.png")
    
def checkResults(x, y):
    
    rteResult = ""
    userResult = ""
    
    if x == 0 or x == 37:
        rteResult = "Green"
    elif 0 < x <= 18:
        rteResult = "Black"
    elif 19 < x <= 36:
        rteResult = "Red"
    
    if y == 0 or y == 37:
        userResult = "Green"
    elif 0 < y <= 18:
        userResult = "Black"
    elif 19 < y <= 36:
        userResult = "Red"
     
        
    if rteResult == userResult:
        return True
    
    return False
    

#Do 1 iteration of the bet simulation    
def simulate(x):

    #The amount you start with
    totalMoney = x
    bet = 1
    
    totalMoney -= bet
    
    #0 and 37 are green, 1 to 18 are black, 19 to 36 are red   
    rouletteResult = random.randint(0,37)
    
    #Change userChoice to pick only between Black numbers
    userChoice = random.randint(1,18)
    
    #If user won, return the new total money
    if checkResults(rouletteResult, userChoice) == True:
        totalMoney += (bet*2)
        print("TotalMoneyWon: " + str(totalMoney))
        return totalMoney
    
    #If user lost, double the next bet, and take out the previous bet from totalMoney 
    #bet *= 2
    #totalMoney -= bet    
    
    #Keep doubling bet until the user is out of money, or wins 
    while checkResults(rouletteResult, userChoice) == False and totalMoney >= 0:
        rouletteResult = random.randint(0,37)
        
        #Change userChoice to pick only between Black numbers
        userChoice = random.randint(1,18)
        
        if checkResults(rouletteResult, userChoice) == True:
            totalMoney += (bet * 2)
            print("TotalMoneyWon: " + str(totalMoney))
            return totalMoney
            
        bet = bet * 2
        totalMoney =  totalMoney - bet
        
        
    
    
    #If we did an extra bet that we had no money for, return money to the user
    #User can't bet if he has less than 0
    if totalMoney < 0:
        totalMoney += bet
    print("TotalMoney: " + str(totalMoney))
    return totalMoney
    
if __name__ == '__main__':    
    main()