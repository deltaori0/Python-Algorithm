from collections import Counter
def solution(participant, completion): 
    answer = Counter(participant) - Counter(completion)
    # print(Counter(participant))
    # print(Counter(completion))
    # print(answer)
    return list(answer.keys())[0]