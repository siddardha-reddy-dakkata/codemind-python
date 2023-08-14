def is_prime(n):
    c = 0
    for i in range(1,n+1):
        if n % i == 0:
            c += 1
    return c == 2
for i in range(int(input())):
    n = int(input())
    f,b = n,n-1
    while not is_prime(f):
        f += 1
    while not is_prime(b) and b != -1:
        b -= 1
    if n - b <= f - n:
        print(b)
    else:
        print(f)