a=int(input())
i=1
ans=False
while(i<=a*0.5):
    if i*i==a:
        ans=True
        break
    i+=1
print(ans)