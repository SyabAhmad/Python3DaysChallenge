print("classes and objects in python")
class student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("Name: " + self.name)
        print("Age: " + str(self.age))

std1 = student("de Developer", 23)
print(std1.display())