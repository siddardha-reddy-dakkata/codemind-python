def is_pal(n):
    s=str(n)
    lst=list(s)
    lst.reverse()
    s1="".join(lst)
    return s==s1

n=int(input())
i=n+1
j=n-1
while(True):
    if is_pal(i):
        break
    i+=1
while(True):
    if is_pal(j):
        break
    j-=1
    
if i-n == n-j:
    print(j,i)
elif i-n < n-j:
    print(i)
else:
    print(j)