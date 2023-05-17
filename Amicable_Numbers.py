def factors(n):
    c=0
    for i in range(1,n):
        if n%i==0:
            c+=i
    return c

a=int(input())
b=int(input())

af=factors(a)
bf=factors(b)
if bf==a and af==b:
    print('Amicable')
else:
    print('Not Amicable')