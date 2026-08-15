def student(name,age):
    print("Required Arguments:")
    print("Name:",name)
    print("Age:",age)
    print()
    
def employee(name,department):
    print("Keyword Arguements:")
    print("Name:",name)
    print("Department:",department)
    
def greet(name,message="Welcome!"):
    print("Default Arguements:")
    print(message,name)
    print()
    
def add_numbers(*numbers):
    total=sum(numbers)
    print("Variable Length Arguements:")
    print("Numbers:",numbers)
    print("Sum:",total)
    print()
    
student("Divy",19)

employee("Divy","CSE")

greet("Divy")
greet("Divy","Good Morning!")

add_numbers(10,30,50,60)
add_numbers(20,50)

    