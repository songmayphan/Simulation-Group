import random

def simulate():
    if random.randint(1,6) + random.randint(1,6) + random.randint(1,6) > 10:
        return True
    else:
        return False
    
def main():
    data_set = 5000
    win = 0
    lose = 0

    for x in range(data_set):
        if simulate():
            win = win + 1
        else:
            lose = lose + 1
    
    print(win/data_set)

main()