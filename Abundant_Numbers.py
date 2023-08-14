n = int(input())
fSum = 0
for i in range(1, n):
    if n % i == 0:
        fSum += i
print(fSum > n)