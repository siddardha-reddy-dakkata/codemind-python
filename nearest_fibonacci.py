def is_fib(n):
    return (5*n*n+4)**0.5%1==0 or (5*n*n-4)**0.5%1==0
    
    #if 5n^2+4 or 5n^2-4 is a perfect square
    # then n is said to be fibronacci
    
a=int(input())
if is_fib(a):
    print(a)
    
else:
    f=b=a
    while(not is_fib(f)):
        f+=1
    while(not is_fib(b)):
        b-=1
    if(a-b==f-a):
        print(b,f)
    elif a-b>f-a:
        print(f)
    else:
        print(b)