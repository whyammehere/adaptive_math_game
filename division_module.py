import random


def division():
    score = 0
    ans = ['a', 'b', 'c', 'd']

    while score < 20:
        if score < 5:
            x = random.randint(1, 6)
            y = random.randint(1, 6)  # level 1
        if 5 <= score <= 10:
            x = random.randint(2, 8)
            y = random.randint(2, 8)   # level 2
        if 10 < score:
            x = random.randint(3, 12)
            y = random.randint(3, 12)  # level 3
        z = x*y
        a = x-1
        b = x+1
        c = x
        while c == x:
            c = random.randint(1, 14)

        print(z, '/', y, '= ? ')
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
            w = input('? = ')

            if g[w] == x:
                score += 1
            else:
                print('sorry, incorrect. The answer was', x)
                score -= 1
        except KeyError:
            print('enter a, b, c or d')
        print()
    print('you either completed 999 levels, so congradulations,or you broke the code')
