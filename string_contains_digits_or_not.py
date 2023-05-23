for i in range(int(input())):
    s=input()
    ans='No'
    for i in s[::-1]:
        if i.isdigit():
            ans='Yes'
            break
    print(ans)