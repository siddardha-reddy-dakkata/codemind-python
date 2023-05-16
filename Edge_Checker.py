num1,num2=input().split()
a,b=int(num1),int(num2)
if abs(a-b)==9 or a==b+1 or a+1==b:
    print('Yes')
else:
    print('No')