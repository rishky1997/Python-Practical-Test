#Given 2 strings, s1 and s2, create a new string by appending s2 in the middle of s1

s1=input("Enter String1:")
s2=input("Enter String2:")
def appendMiddle(str1, str2):
    sl=(len(str1)//2)-1
    fstr=str1[:sl]+str2+str1[sl:]
    print(fstr)
appendMiddle(s1,s2)
