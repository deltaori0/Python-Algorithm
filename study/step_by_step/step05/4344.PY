import sys
C = int(input())
for i in range(C):
  info = list(map(int, sys.stdin.readline().split()))
  num = info[0]
  scores = info[1:]
  avg = sum(scores) / num
  good_students = list(filter(lambda s: s > avg, scores))
  perc = len(good_students)/num*100
  # list comprehension 방법
  # good_students = [s for s in scores if s > avg]
  print("%.3f%%" % (perc))
