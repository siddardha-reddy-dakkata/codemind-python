n=int(input())
if n<3 or n>100:
    print('The pattern is not possible')
else:
    for i in range(1,n+1):
        print('*'*i)
    for i in range(n-1,0,-1):
        print('*'*i)