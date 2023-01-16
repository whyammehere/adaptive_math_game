import random


def subtraction():
    level = 1
    score = 0
    #two numbers that are added together 
    x = 0
    y = 0
    ans = ["a", "b", "c", "d"]
    while level < 7:
        if score < 5:
            x = random.randint(1, 10)
            y = random.randint(1, 10)
            level = 1
        elif score <= 10:
            x = random.randint(1, 50)
            y = random.randint(1, 30)
            level = 2
        elif 10 <= score <= 15:
            x = random.randint(1, 150)
            y = random.randint(1, 150)
            level = 3
        elif 15 <= score <= 20:
            x = random.randint(-10, 10)
            y = random.randint(-10, 10)
            level = 4
        elif 20 <= score <= 25:
            x = random.randint(-30, 30)
            y = random.randint(-30, 30)
            level = 5
        elif 25 <= score <= 30:
            x = random.randint(-100, 100)
            y = random.randint(-100, 100)
            level = 6
        elif score >= 31:
            level = 7

        z = x + y
        a = x - random.randint(1, 3)
        b = x + random.randint(1, 3)
        c = x

        print(f"{z} - {y} = ?")
        answers = [a, b, c, x]
        random.shuffle(answers)

        g = {}
        n = 0
        for t in answers:
            g[ans[n]] = t
            n += 1
        for m in g:
            print(m, g[m])

        try:
            w = input("? = ")
            if g[w] == x:
                score += 1
            else:
                print("Sorry, that's wrong. The answer was", x)
                score -= 1
        except KeyError:
            print("Only enter a, b, c, or d")
        print()
    print("You have completed the Subtraction Module, congrats!")


subtraction()
