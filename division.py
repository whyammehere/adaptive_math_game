import random

def division():
    scorepos = 0
    score = 0
    ans = ['a','b','c','d']
    attempts = 0
    r = int(input('how many questions would you like to do:'))
    while score<r:
        if score<5:
            x = random.randint(1,6)
            y = random.randint(1,6)     #level 1
        if 5<=score<=10:
            x = random.randint(2,8)
            y = random.randint(2,8)   # level 2
        if 10<score:
            x = random.randint(3,12)
            y = random.randint(3,12)     #level 3
        z = x*y
        a = x + random.randint(1,3)
        b = x - random.randint(1,3)
        c = x
        while c == x or c == b or c==a:
            c = random.randint(1,14)
        
        
        print(z, '/', y, '= ?')
        answers =[a,b,c,x]
        random.shuffle(answers)

        g = {}
        n= 0
        for t in answers:
            g[ans[n]] = t
            n +=1
        
        for m in g:
            print(m,g[m])
        
        try:
            w = input('? =')
        
            if g[w] == x:
                score +=1
                print('score=',score)
                attempts +=1
                scorepos +=1
            else:
                print('sorry, incorrect. The answer was', x)
                score -=1
                print('score=',score)
                attempts +=1
        except KeyError:
            print('enter a,b,c or d')
        print()
    per = 100* score/attempts
    round(per)
    print('you completed',r,' problems, great job :)')
    print('you had a', per ,'% accuracy')
    if per == 100
        print('You answered perfectly!!!')
division()
