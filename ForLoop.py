print("this tutorial is about for loop in python")

fruits = {"apple", "mango", "oranges", "banana", "grapes"}
for items in fruits:
    print(items, " are some fruits for you")


def welcome():
    print("Welcome Dude")


def error(index):
    if index < 3:
        authentication()
    else:
        print("Out of Moves")


def authentication():
    indexvalue = 0
    pincode = int(input("Pin COde: "))

    if pincode == 1234:
        welcome()
        # print("incorrect Pin Code")
    else:
        indexvalue = indexvalue + 1
        error(indexvalue)

name = input("Name: ")
authentication()