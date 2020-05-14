#. Given a string, return the sum and average of the digits that appear in the string, ignoring all other characters
import re
s=input("Enter String:")
no=re.findall("[0-9]+",s)
sum=0
for i in no:
    sum=sum+int(i)
print("Sum:",sum)
print("Percentge is:",(sum*100)/(len(no)*100))
