a=input("enter a string or number")
if a.isdecimal() and a.isalpha():
    print("it is decimal")
elif a.isalpha():
    print("it is an alphabit")
elif a.isdigit():
    print('it is digit')
elif a.isnumeric():
    print("is numaric")
elif a.isascii():