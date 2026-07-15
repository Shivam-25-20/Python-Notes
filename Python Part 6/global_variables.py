message = "Welcome to Python!"

def greet():
    print(message)

greet()
print(message)

language = "Python"

def show_language():
    print("Inside Function:", language)

show_language()

print("Outside Function:", language)

print("-------------------------------------------------")
name = "Alice"

def display():
    name = "Bob"
    print("Inside Function:", name)

display()

print("Outside Function:", name)