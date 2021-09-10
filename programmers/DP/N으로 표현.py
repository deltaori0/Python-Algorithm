def solution(N, number):
    dp_table = [set()]
    
    for i in range(1, 9):
        temp = []
        temp.append(int(str(N) * i))
        
        for j in range(1, i):
            for x in dp_table[j]:
                for y in dp_table[i-j]:
                    temp.append(x + y)
                    temp.append(x - y)
                    temp.append(x * y)
                    if y != 0:
                        temp.append(x // y)
        
        for t in temp:
            if t == number:
                return i
        
        dp_table.append(set(temp))
    
    return -1