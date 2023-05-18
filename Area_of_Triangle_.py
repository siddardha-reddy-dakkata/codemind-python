a,b,c=map(int,input().split())
s=(a+b+c)/2
ans=(s*(s-a)*(s-b)*(s-c))**0.5
print(f'{ans:.2f}')