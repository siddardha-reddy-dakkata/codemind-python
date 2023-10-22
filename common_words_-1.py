s1 = input()
s2 = input()
s1 = s1.lower()
s2 = s2.lower()
l1 = list(s1.split(" "))
l2 = list(s2.split(" "))

c = 0
for i in l1:
    if i in l2:
        c += 1
print(c)
