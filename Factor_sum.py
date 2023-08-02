lst = list(map(int,input().split(',')))
ans = []

def sum_of_factors(n):
    s = 0
    for i in range(1,n+1):
        if n%i==0:
            s+=i
    return s

for i in lst:
    if sum_of_factors(i) in lst:
        ans.append(i)
ans.sort()
if ans:
    print(*ans)
else:
    print(-1)