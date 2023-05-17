a=int(input())
b=len(str(a))
a1=a*a
b1=str(a1)
if(str(a)==b1[-b:]):
    print('Automorphic Number')
else:
    print('Not an Automorphic Number')