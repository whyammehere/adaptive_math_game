from random import randint, shuffle

def randAns(ans, deviation=2):
    a = [ans]
    while len(a)<4:
        x = randint(ans-deviation, ans+deviation)
        if x not in a:
            a.append(x)

    shuffle(a)
    b = {"A": a[0], "B": a[1], "C": a[2], "D": a[3]}
    print("A:", a[0], "B:", a[1], "C:", a[2], "D:", a[3])
    return b

def incorrectAns(ans):
    print('incorrect')
    print('the correct answer is', ans)
    print()