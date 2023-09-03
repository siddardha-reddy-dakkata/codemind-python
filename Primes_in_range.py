def is_prime(n):
    c = 0
    if n < 2:
        return False
    for i in range(2, int( n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
    
n = int(input())
m = int(input())

primeCount = 0
for i in range(n, m + 1):
    if is_prime(i):
        primeCount += 1
print(primeCount)