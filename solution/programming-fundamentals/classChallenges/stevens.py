# [a, b, c]
answers = [
    [True, False, False],
    [False, True, False],
    [False, False, True],
    [True, False, False],
    [False, False, True],
    [True, False, False],
    [False, True, False],
    [True, False, False],
    [False, True, False],
    [False, False, True]
]

counta = 0
countb = 0
countc = 0

for i in range(len(answers)):
    if answers[i][0] == True:
        counta = counta + 1
    elif answers[i][1] == True:
        countb = countb + 1
    elif answers[i][2] == True:
        countc = countc + 1


if counta > countb and counta > countc:
    print("Count A is the biggest!")
if countb > counta and countb > countc:
    print("Count B is the biggest!")
if countc > counta and countc > countb:
    print("Count C is the biggest!")