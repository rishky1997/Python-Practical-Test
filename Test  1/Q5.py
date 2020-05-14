#Given a two list. Create a third list by picking an odd-index element from the first list and even index elements from second.
listOne = [3, 6, 9, 12, 15, 18, 21]
listTwo = [4, 8, 12, 16, 20, 24, 28]
print("Element at odd-index positions from list one \n",listOne[1::2])
print("Element at even-index positions from list two \n",listTwo[::2])
print("Printing Final third list \n",listOne[1::2]+listTwo[::2])
