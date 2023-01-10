from random import *

from addition import *
from subtraction import *
from multiplication import *
from division import *


#redo leveling systems

def randAns(ans,deviation=2):
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
print("""
which of the following modules would you like to do?

addition
subtraction
ultiplication
division

""")
ask=input()
if ask == 'addition':
    addition()
elif ask == 'subtraction':
    subtraction()
elif ask == 'multiplication':
    multiplication()
elif ask == 'division':
    division()
