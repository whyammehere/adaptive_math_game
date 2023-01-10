from random import*
from adaptive_math import *

def addition():
    a=0
    level = 1
    incorrect=0
    for i in range(50):
        
        seed()
        x=[]
        for j in range(randint(2,level+1)):
            x.append(randint(0,level*10))
        for j in range(len(x)-1):
            print(x[j], end = ' + ')
        print(x[-1], '= ?')
        #print(sum(x))
        y=randAns(sum(x),level*3)
        try:
            if y[input()] == sum(x):
                print('correct!')
                print()
                a+=1
                if a >= 8:
                    a=0
                    level +=1
            else:
                incorrectAns(sum(x))
                incorrect+=1
                if incorrect%3==0 and level > 1:
                    level -= 1        
        except:
            incorrectAns(sum(x))
            incorrect+=1
            
    print('congrats! you completed the addition module!')
    print('you score is:', 2*(50-incorrect), '%')