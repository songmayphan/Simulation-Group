from random import randint

def simulate():
    sum = random(2) # 2 is the qty of dices
    if sum == 7 or sum == 11:
        return 1
    elif sum == 2 or sum == 3 or sum == 12:
        return 0
    else: 
        point = sum
        while sum != 7:
            sum = random(2)
            if sum == point:
                return 1
        return 0

def random(x):
    sum = 0
    for i in range(x):
        dice = randint(1,6)
        sum += dice
    return sum

def main():
    win = 0
    trials = 1000
    for i in range(trials):
        sim = simulate()
        if sim > 0:
            win += 1
    i += 1
    total = (win/i) * 100
    print(str(total) + ' %')
    
main()
            
