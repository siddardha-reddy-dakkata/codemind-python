def is_prime(n):
    c = 0
    if n < 2:
        return False
    for i in range(2, int( n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
 
def rev(n):
    rev = 0
    while n != 0:
        rev = rev * 10 + n%10
        n //= 10
    return rev


n = int(input())
reverse = rev(n)

a = b = False
if is_prime(n):
    a = True
if is_prime(reverse):
    b = True
    
if a and b:
    print("circular prime")
elif a:
    print("prime but not a circular prime")
else:
    print("not prime")