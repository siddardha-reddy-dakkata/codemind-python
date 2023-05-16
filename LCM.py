num1,num2=input().split()
a,b=int(num1),int(num2)
gcd=0
i=1
while(i<=a and i<=b):
    if a%i==0 and b%i==0:
        gcd=i
    i+=1
print((a*b)//gcd)