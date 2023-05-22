s=input()
v='aeiou'
ans='F'
for i in s:
    if i in v and ans!='V':
        ans='V'
        print(ans,end="")
    elif i not in v and ans!='C':
        ans='C'
        print(ans,end="")