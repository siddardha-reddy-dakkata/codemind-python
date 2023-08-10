n = int(input())
l = list(map(int,input().split()))

r = int ( n / 2 )
ans = []
for i in range(n-1 , r-1 , -1):
    ans.append(l[i])

for i in range( 0 , r ):
    ans.append(l[i])
    
print(*ans)