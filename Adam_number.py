n = input()
n1 = str(int(n) **2)
n2 = str(int(n[-1::-1]) ** 2)
print(n1 == n2[-1::-1])