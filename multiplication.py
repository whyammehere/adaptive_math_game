from random import *
from adaptive_math import *

def multiplication():
    a=0
    level = 1
    incorrect=0
    for i in range(50):
        
        seed()
        x=(randint(level*-10,level*10))
        y=(randint(level*-10,level*10))
        print(x, '*', y, '= ?')
        try:
            if float(input()) == x*y:
                print('correct!')
                print()
                a+=1
                if a == 9:
                    a=0
                    level +=1
            else:
                print('incorrect')
                incorrect+=1
                if incorrect%3==0 and level > 1:
                    level -= 1
                print('the correct answer is',x*y)
                print()
        except:
            print('incorrect')
            incorrect+=1
    print('congrats! you completed the multiplication module!')
    print('you score is:', (100-incorrect), '%')