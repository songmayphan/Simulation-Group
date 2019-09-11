import random


def main():

    totalWins = 0
    totalTries = 100000
    
    //Calculate total wins
    for i in range(totalTries):
        result = simulate()
    
        if result == True:
            totalWins += 1   

    print("The user won " + str(totalWins) + " times, out of " + str(totalTries))

#Simulate 1 iteration of the game passedix
def simulate():

    firstRoll = random.randint(1,6)
    secondRoll = random.randint(1,6)
    thirdRoll = random.randint(1,6)

    sum = firstRoll + secondRoll + thirdRoll

    if sum > 10:
        return True
        
    return False    

main()