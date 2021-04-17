def solution(a, b):
  month_days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
  week_day = ['SUN','MON','TUE','WED','THU','FRI','SAT']
  answer = ''

  total_days = 0

  for i in range(a):
    if i + 1 == a : # 마지막 month이면 b-1를 더하기
      total_days += b-1
    else:
      total_days += month_days[i]
  
  final_index = (total_days + 5) % 7 # 더하기 5 해준 이유는 FRI부터 시작해서
  answer = week_day[final_index] 

  
  return answer

print(solution(5, 24))