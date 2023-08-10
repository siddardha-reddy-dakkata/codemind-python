a = list(map(int,input().split()))
b = list(map(int,input().split()))
am = bm = 0
for i in range(3):
    if a[i] > b[i]:
        am += 1
    elif a[i] < b[i]:
        bm += 1
print(am,bm)