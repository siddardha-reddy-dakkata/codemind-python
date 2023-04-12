n=int(input())
even=0
odd=0
s=input()
lst=[int(i) for i in s.split()]
for i in range(n):
    if i % 2 ==0:
        even+=lst[i]
    else:
        odd+=lst[i]
diff=even-odd if even>odd else odd-even
print(diff)