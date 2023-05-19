s=input()
lst=list(s)
lst.reverse()

s="".join(lst)

if s[-1]=='-':
    if s[0]=='0':
        print('-' + s[1:-1])
    else:
        print('-' + s[:-1])
else:
    if s[0]=='0':
        print(s[1:])
    else:
        print(s)