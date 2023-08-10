n = int(input())
l = list(input().split())

s = "".join(l)
n = int(s) + 1
s = str(n)
for i in s:
    print(i,end=" ")