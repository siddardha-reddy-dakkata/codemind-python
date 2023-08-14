def is_prime(n):
    c = 0
    for i in range(1,n+1):
        if n % i == 0:
            c += 1
    return c == 2
n = int(input())
b,f = n-1,n
while not is_prime(f):
    f += 1
while not is_prime(b):
    b -= 1
if f - n <= n - b:
    print(f - n)
else:
    print(n - b)