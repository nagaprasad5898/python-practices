a=input('enter anything')
b=0
c=0
d=0
f=0
for i in a:
    if i in 'aeiouAEIOU':
        b=b+1
    elif i.isdigit():
        c=c+1
    elif i.isspace():
        d=d+1
    else:
        f=f+1
print("voles:",b,"digit:",c,'spaces:',d,'cosonant:',f)