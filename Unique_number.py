a=input()
lst=list(a)
my_set=set(lst)
if(len(lst)==len(my_set)):
    print('Unique Number')
else:
    print('Not Unique Number')