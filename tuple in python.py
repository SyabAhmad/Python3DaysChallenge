print("Tuple in Python")
myTuple = ("grapes", "banana", "apple", "mango") # simple tuple
print(myTuple)  # to display simple tuple

# to display tuple to some range
print(myTuple[1:4])
print(myTuple)

print(myTuple.count("apple"))
print(myTuple.index("apple"))

# searching in tuple
print("banana" in myTuple)

# we can also concatenate tuple
newTuple = ("oranges", "pineapple")
concatenation = myTuple+newTuple
print(concatenation)

# we can also assign dferent variables to diferent values in tuple
#like this one
a, b, c, e = myTuple
print(a)
print(b)
print(c)
print(e)


# and as we can also return multiple values from function we can store them in tuples
# see below

def tupleValues():
    return (1,2,3,4,5,6,7,8,9)

myNewTuple = tupleValues()
print(myNewTuple)
print(type(myNewTuple))


