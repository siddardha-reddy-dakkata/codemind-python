def is_prime(n):
    c = 0
    for i in range(1,n+1):
        if n % i == 0:
            c += 1
    return c == 2
n = int(input())
ans = False
if is_prime(n):
    ans = True
    while(n):
        if not is_prime(n % 10):
            ans = False
            break
        n //= 10
if(ans):
    print("Mega Prime")
else:
    print("Not Mega Prime")