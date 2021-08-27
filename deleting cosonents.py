a = input("enter full name")
b = " "
for i in a:
    if i in "aeiouAEIOU":
        b = b+i
    elif i.isspace():
        b = b+i
    elif i is ",":
        b = b+i
print(b)

for i in a:
    if i not in "bcdfghjklmnpqrstvwxyz":
        b = b+i
print(b)
