def self_dividing(n):
    s = str(n)
    c = 0
    for i in s:
        if int(i) == 0:
            return False
        if n % int(i) == 0:
            c += 1
    return c == len(s) 



x = int(input())
y = int(input())
ans = []
for i in range(x,y+1):
    if self_dividing(i):
        ans.append(i)
print(*ans)