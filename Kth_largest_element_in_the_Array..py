n = int(input())
lst = list(map(int,input().split()))
k = int(input())
lst = list(set(lst))
lst.sort()
print(lst[-k])