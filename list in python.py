
print("List in Python")
myList = [1, 2, 3, 4, 5, 6, 7, 8, 8, 9]
# will display all items in the list
print(myList)
# will display items at some range
print(myList[1:4])
print(myList[4:6])

# also in reverse direction
print(myList[:-1])
print(myList[4:-1])

# to update the value of specific item
myList[2] = 99
print(myList)

# to add new value at the end
myList.append(1002)
print(myList)
# to remove item
print(myList)
myList.remove(8)  # will remove first occurrence of 8
print(myList)

# to sort list
myList.sort()
print(myList)

# to reverse list
myList.reverse()
print(myList)

abc = ["abc", "Hello", "between"]
# to check if something is in the list or not
print(999 in myList)
print(4 in myList)
print(6 in myList)
print(2 in myList)
print("Hello" in abc)

