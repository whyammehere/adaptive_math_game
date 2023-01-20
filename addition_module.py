from random import randint, seed
from functions import randAns, incorrectAns


def addit():
    
    a = 0
    level = 1
    incorrect = 0

    print('----------------------')
    print("In this module, the difficulty increases every 10 correct answers, the difficulty will decrease every 3 incorrect answers")

    print()
    number = int(input("How many questions will you like to do? "))
    for i in range(number):

        #create problem
        seed() 
        x = []
        for j in range(randint(2, level+1)):
            x.append(randint(0, level*10))

        print('----------------------')
        ans=''
        while ans not in ['A','B','C','D']:

            #print problem
            for j in range(len(x)-1):
                print(x[j], end=' + ')
            print(x[-1], '= ?')
            # print(sum(x))
            y = randAns(sum(x), level*3)


            #answer problem
            ans=input().capitalize()
            if ans in ['A','B','C','D']:
                if y[ans] == sum(x):
                    print()
                    print('correct!')
                    a += 1
                    if a >= 10:
                        a = 0
                        level += 1
                else:
                    incorrectAns(sum(x))
                    incorrect += 1
                    if incorrect % 3 == 0 and level > 1:
                        level -= 1
            else:
                print('[!] please only input \"A\", \"B\", \"C\", or \"D\"')
                print()

    print('----------------------')
    print('congrats! you completed the addition module!')
    score = ((number-incorrect)/number) * 100
    print(f'you completed {number} problems, great job :)')
    print(f'your score is: {round(score, 2)} ')
