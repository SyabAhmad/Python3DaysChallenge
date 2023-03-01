print("Objects and Classes in Python")
class student:
    def __init__(self, name, age):
        self.name = name
        self.age = age


# now we create new instent of student class
std1 = student("de Developer", 23)

print(std1.age)
print(std1.name)