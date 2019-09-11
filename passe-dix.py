import random

def simulate():
    sum = 0
    d1 = random.randint(1,6)
    d2 = random.randint(1,6)
    d3 = random.randint(1,6)
    print(d1, d2,d3)
    sum = d1 + d2 + d3
    if sum > 10:
        return True
    else:
        return False
def main():
    times = 1000
    count = 0
    #print(count)
    for i in range(times):
        result = simulate()
        if result is True:
            count = count +1 
        #print (count)
    print ("Percentage: ", (count / times) * 100.00)
    
if __name__ == '__main__':
    main()
#end class