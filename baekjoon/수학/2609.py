a, b = map(int, input().split())

def get_yaksu(num):
    ans = set()
    for x in range(1, num+1):
        if num % x == 0:
            ans.add(x)
    
    return ans

max_yaksu = max(list(get_yaksu(a) & get_yaksu(b)))
min_baesu = max_yaksu * (a // max_yaksu) * (b // max_yaksu)
print(max_yaksu)
print(min_baesu)