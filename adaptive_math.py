from random import *

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
        y=randAns(sum(x))
        try:
            if y[input()] == sum(x):
                print('correct!')
                print()
                a+=1
                if a >= 8:
                    a=0
                    level +=1
            else:
                incorrectAns()
                incorrect+=1
                if incorrect%3==0 and level > 1:
                    level -= 1        
        except:
            incorrectAns()
            incorrect+=1
            
    print('congrats! you completed the addition module!')
    print('you score is:', 2*(50-incorrect), '%')

def subtraction():
    a=0
    level = 1
    incorrect=0
    for i in range(100):
        
        seed()
        x=(randint(0,level**2*10))
        y=(randint(0,x))
        print(x, '-', y, '= ?')
        try:
            if float(input()) == x-y:
                print('correct!')
                print()
                a+=1
                if a == 10:
                    a=0
                    level +=1
            else:
                print('incorrect')
                incorrect+=1
                if incorrect%3==0 and level > 1:
                    level -= 1
                print('the correct answer is',x-y)
                print()
        except:
            print('incorrect')
            incorrect+=1
    print('congrats! you completed the subtraction module!')
    print('you score is:', (100-incorrect), '%')

def multiplication():
    a=0
    level = 1
    incorrect=0
    for i in range(100):
        
        seed()
        x=(randint(0,level*10))
        y=(randint(0,level*10))
        print(x, '*', y, '= ?')
        try:
            if float(input()) == x*y:
                print('correct!')
                print()
                a+=1
                if a == 10:
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
