def is_prime(n):
    c = 0
    if n < 2:
        return False
    for i in range(2, int( n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
    
def is_pal(n):
    temp = n
    rev = 0
    while temp != 0:
        rev = rev * 10 + temp%10
        temp //= 10
    return rev == n
    
    
n = int(input()) + 1

while True:
    if is_prime(n) and is_pal(n):
        break
    n += 1
print(n)