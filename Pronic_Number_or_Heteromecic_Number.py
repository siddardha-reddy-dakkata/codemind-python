a=int(input())
ans='NO'
for i in range(1,a):
    if i*(i+1)==a:
        ans='YES'
print(ans)