from itertools import permutations
def solution(numbers):
    answer = ''
    
    numbers = list(map(str, numbers))
    numbers.sort(key = lambda x: x * 3, reverse=True)
    answer = str(int(''.join(numbers)))


    
#     시간 초과
#     temp = list(permutations(numbers))
#     max = 0
#     for t in temp:
#         temp_str = ''
#         for tt in t:
#             temp_str += str(tt)
#         cur = int(temp_str)
#         if cur > max:
#             max = cur
    
#     answer = str(max)

            
    return answer