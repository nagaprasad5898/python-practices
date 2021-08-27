a=input("enter full name")
d=a.split()
b=''
for i in a.title():
    if i.isupper():
        b=b+i
c='.'.join(b)
print(c[:len(c)-1]+d[len(d)-1])