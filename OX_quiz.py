## 백준 OX 퀴즈

test = int(input())
for i in range(test):
    score = 0
    O_score = 0
    OX = list(input())
    for j in OX:
        if j == 'O':
            O_score += 1
            score += O_score
        else:
            O_score = 0
    print(score)