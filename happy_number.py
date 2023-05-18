a=int(input())
while(a>9):
    ans=0
    for i in str(a):
        ans+=int(i)**2
    a=ans
if a==1 or a==7:
    print('True')
else:
    print('False')