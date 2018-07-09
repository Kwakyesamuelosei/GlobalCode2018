def get_age():
    age = int(input("Enter your age: \n"))
    return age

age = get_age()

def get_name():
    name = str(input("Enter your name: \n"))
    return name

name = get_name()

print("Your name : {0}\nYour age : {1}".format(name,age))

