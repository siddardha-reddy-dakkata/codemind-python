n = int(input())
lst = list(map(int,input().split()))
k = int(input())

while k > 0:
    temp = lst.pop()
    lst.insert(0,temp)
    k -= 1
print(*lst)