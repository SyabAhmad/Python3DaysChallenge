print("Sets in Python")

newSet = {"apple", "mango", "oranges"}
print(type(newSet))

#to add Value to set
newSet.add("grapes")
print(newSet)

# to remove value from set
newSet.remove("apple")
print(newSet)

# to access using loop
for item in newSet:
    print(item)

# to join two sets
newSet1 = {"Banana", "PineApple"}

afterjoin = newSet.union(newSet1)
print(afterjoin)

# if you want to print specific item in set
print("Apple" in afterjoin)
# False due to case