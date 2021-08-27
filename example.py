a = "kanna is king"
b = 0
c = 0
d = 0
for i in a:
    if i in "aeiouAEIOU":
        b = b+1
    elif i.isspace():
        c = c+1
    elif i.isdigit():
        d = d+1
print("vowels:", b)
print("space:", c)
print("digit", d)
b = (reversed(a.split()))
c = " ".join(b)
print(" ".join(b))
