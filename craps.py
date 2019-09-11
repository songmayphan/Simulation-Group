import random


def main():

    totalWins = 0
    totalTries = 100000
    
    for i in range(totalTries):
        result = simulate()
    
        if result == True:
            totalWins += 1   

    percentage = (totalWins * 100) / totalTries
    print("The user won " + str(totalWins) + " times, out of " + str(totalTries) + " for a total percentage of " + str(percentage))

#Simulate 1 iteration of the game
def simulate():

    #Get the two random numbers from dice
    firstRoll = random.randint(1,6)
    secondRoll = random.randint(1,6)

    sum = firstRoll + secondRoll

    if sum == 7 or sum == 11:
        return True
        
    if sum == 2 or sum == 3 or sum == 12:
        return False

    points = sum
    
    #Keep playing until one of the needed results
    while sum != 7:
        firstRoll = random.randint(1,6)
        secondRoll = random.randint(1,6)
        sum = firstRoll + secondRoll
        
        if sum == points:
            return True
        if sum == 7:
            return False
            
        points = sum
            
        
        
    

main()