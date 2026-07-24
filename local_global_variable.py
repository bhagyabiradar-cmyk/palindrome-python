# Global variable
message = "Welcome to Python"

def show_message():
    # Local variable
    name = input("Enter your name: ")

    print(message)      # Accessing global variable
    print("Hello,", name)

show_message()

print("Global variable:", message)

# print(name)   # This will cause an error because 'name' is a local variable.