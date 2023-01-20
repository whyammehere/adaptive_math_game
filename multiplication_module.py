from random import randint, seed
from functions import *


def multiplication():
    a = 0
    level = 1
    incorrect = 0

    print('----------------------')
    print("In this module, the difficulty increases every 10 correct answers, the difficulty will decrease every 3 incorrect answers")
    print()

    number = int(input("How many questions will you like to do? "))
    for i in range(number):

        seed()
        x = (randint(level*-10, level*10))
        y = (randint(level*-10, level*10))

        print('----------------------')
        ans = ''
        while ans not in ['A', 'B', 'C', 'D']:
            print(x, '*', y, '= ?')

            z = randAns(x*y, abs(x)+2)
            ans = input().capitalize()
            if ans in ['A', 'B', 'C', 'D']:
                if z[ans] == x*y:
                    print()
                    print('correct!')
                    print()
                    a += 1
                    if a == 10:
                        a = 0
                        level += 1
                else:
                    incorrectAns(x*y)
                    incorrect += 1
                    if incorrect % 3 == 0 and level > 1:
                        level -= 1
            else:
                print('[!] please only input \"A\", \"B\", \"C\", or \"D\"')
                print()

    print('----------------------')
    print('congrats! you completed the multiplication module!')
    score = ((number-incorrect)/number) * 100
    print(f'you completed {number} problems, great job :)')
    print(f'your score is: {round(score, 2)} ')
