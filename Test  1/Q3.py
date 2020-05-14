#Arrange String characters such that lowercase letters should come first
string=input("input_String=")
lstr=""
ustr=""
for i in string:
    if i.islower():
        lstr+=i
    else:
        ustr+=i
print("arranging characters giving precedence to lowercase letters:")
print(lstr+ustr)
