a=int(input())
while(a>9):
    b=str(a)
    c=0
    for i in b:
        c+=int(i)
    a=c
print(a)