n = input()
ans = 0
for i in range(len(n)):
    ans += int(n[i]) ** (i + 1)
print(ans == int(n))