import os
from random import randint

def main():
    os.system('cls')
    n = 1
    
    while True:
        #os.system('cls')
        print(f'Current n: {n}')
        print(f'Current odds: {1/(2**n)}')
        print(f'Current value: {2**n}')
        
        p = randint(1, 10)
        if p <= 5:
            print('Won.\n')
            n+=1
        else:
            print('Lost.')
            break

if __name__ == '__main__':
    main()