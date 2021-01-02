def check_score(supoza, answers):
    score = 0
    idx = 0
    max_idx = len(supoza) - 1
    
    for a in answers:
        if idx > max_idx:
            idx = 0
        if a == supoza[idx]:
            score += 1
        idx += 1
        
    return score

def solution(answers):
    answer = []
    
    supoza1 = [1,2,3,4,5]
    supoza2 = [2,1,2,3,2,4,2,5]
    supoza3 = [3,3,1,1,2,2,4,4,5,5]
    
    s1 = check_score(supoza1, answers)
    s2 = check_score(supoza2, answers)
    s3 = check_score(supoza3, answers)
    
    max_score = max(s1, s2, s3)
    score_list = [s1, s2, s3]
    
    for i, s in enumerate(score_list):
        if s == max_score:
            answer.append(i+1)
    return answer