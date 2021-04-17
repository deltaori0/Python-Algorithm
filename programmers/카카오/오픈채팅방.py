# dictionary del이 오래걸린다는 것을 알았다!
def solution(record):
    result = []
    dic = dict()
    for r in record:
        temp = r.split()
        action, id = temp[0], temp[1]
        if action == 'Enter' or action == 'Change':
            dic[id] = temp[2]
            
    for r in record:
        temp = r.split()
        action, id = temp[0], temp[1]
        if action == 'Enter':
            result.append(dic[id]+'님이 들어왔습니다.')
        elif action == 'Leave':
            result.append(dic[id]+'님이 나갔습니다.')
        else:
            pass
    return result