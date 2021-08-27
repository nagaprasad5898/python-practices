#sthis is not working if letter is repeting more then 9times
a=input('enter')
b=0
c=0
for i in a:
    b=a.count(i)
    c=str(c)+str(b)
print(max(c))