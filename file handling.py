print("File Handling in Python")

# opening file if exist
try:
    file = open("data.txt", "r")
except:
    print("file not found: ")

# writing to file and creating
try:
    file1 = open("data.txt", "w")
    file1.write("Hey, this is de Developer \n")
    file1.write("You can follow me on Github \n")
    file1.write("Link to my Github is \n")
    file1.write("[github.com/SyabAhmad] \n")
except:
    print("Some Error")

# reading file

try:
    file3 = open("data.txt", "r")
    a = file3.read()
    print(a)
except:
    print("File not Found")
