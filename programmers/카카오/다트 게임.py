import re
def solution(dartResult):
    bonus_score = {
        'S' : 1,
        'D' : 2,
        'T' : 3
    }

    a = re.findall("\d+", dartResult)
    b = re.findall("[S|D|T|*|#]+", dartResult)
    
    score = []
    for i, x in enumerate(b):
        bonus, opt = x[0], ''
        if len(x) == 2:
            opt = x[1]
        cur = pow(int(a[i]), bonus_score[bonus])
        if opt == '*':
            if i >= 1:
                score[i-1] *= 2
            cur *= 2
        elif opt == '#':
            cur *= -1
        score.append(cur)
    return sum(score)
