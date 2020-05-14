#. Given a number count the total number of digits in a number
no=int(input("Enter no.:"))
n=no
c=0
while n!=0:
    c+=1
    n=n//10
print("No. of digits are:",c)


#Reverse the following list using for loop
list1 = [10, 20, 30, 40, 50]
list2=[]
for i in range(len(list1)-1,-1,-1):
    list2.append(list1[i])
for i in list2:
    print(i)
