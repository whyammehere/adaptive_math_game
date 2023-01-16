from random import randint, shuffle

import addition_module
import subtraction_module
import multiplication_module
import division_module

# redo leveling systems


def randAns(ans, deviation=2):
    a = [ans]
    for i in range(3):
        x = randint(ans-deviation, ans+deviation)
        if x != a:
            a.append(x)

    shuffle(a)
    b = {"A": a[0], "B": a[1], "C": a[2], "D": a[3]}
    print("A:", a[0], "B:", a[1], "C:", a[2], "D:", a[3])
    return b


def incorrectAns(ans):
    print('incorrect')
    print('the correct answer is', ans)
    print()


# do division
print("""
which of the following modules would you like to do?

addition
subtraction
multiplication
division

""")
ask = input()
if ask == 'addition':
    addition_module.addit()
elif ask == 'subtraction':
    subtraction_module.subtraction()
elif ask == 'multiplication':
    multiplication_module.multiplication()
elif ask == 'division':
    division_module.division()
