from random import *

from addition import *
from subtraction import *
from multiplication import *
from division import *


#redo leveling systems

def randAns(ans,deviation):
    a=[ans]
    for i in range(3):
        x=randint(ans-deviation,ans+deviation)
        if x != a:
            a.append(x)
    
    shuffle(a)
    b={"A":a[0],"B":a[1],"C":a[2],"D":a[3]}
    print("A:",a[0],"B:",a[1],"C:",a[2],"D:",a[3])
    return b

def incorrectAns(ans):
    print('incorrect')
    print('the correct answer is',ans)
    print()





#do division

a=float(input())
if a == 1:
    addition()
elif a == 2:
    subtraction()
elif a == 3:
    multiplication()
elif a == 4:
    addition()
