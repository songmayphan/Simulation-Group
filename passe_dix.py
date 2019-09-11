
from random import randint

def simulate():
    
    if random() > 10:
        return True
    else: 
        return False


def random():

    dice_sum = randint(1,6) + randint(1,6) + randint(1,6)
    return dice_sum

def main():
    
    total = 0
    trials = 1000  
    for i in range(trials):
        if simulate():
            total += 1
    
    i += 1
    total = (total/i)*100
    print(str(total) + ' %') 

if __name__ == '__main__':
    main()




        
