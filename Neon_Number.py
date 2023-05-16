num=int(input())
num_sq=num*num
s=0
temp=0
while(num_sq):
    temp=num_sq%10
    s+=temp
    num_sq//=10
if(s==num):
    print('Neon Number')
else:
    print('Not Neon Number')