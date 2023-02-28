print("Dictionary in Python")
dict = {"apple": 2, "banana": 3, "grapes": 4, "mango": 5}
# type of dict
print(type(dict))
# to print dict keys and values
print(dict)
# return boolean if it exist or not
print("apple" in dict)
# printing specific item
print(dict["apple"])
# length of dict
print(len(dict))
# update
dict.update({"apple": 5})
print(dict)
#add item
dict["color"] = "red";
print(dict)
# remove item
dict.pop("apple")
print(dict)
# REMOVE LAST ITEM
dict.popitem()
print(dict)
# clear method will clear the dictionary
#----dict.clear()
#----print(dict)
# copy dictionary
dict2 = dict.copy()
print(dict2)

