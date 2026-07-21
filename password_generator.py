import random
import string


def generate_password(length):
    characters = (
        string.ascii_letters +
        string.digits +
        string.punctuation
    )

    password = ""

    for _ in range(length):
        password += random.choice(characters)

    return password


print("=== Password Generator ===")

length = int(input("Enter password length: "))

password = generate_password(length)

print("\nGenerated Password:")
print(password)

print("\nPassword Details")
print("Length:", len(password))
print("Contains Letters:", any(c.isalpha() for c in password))
print("Contains Digits:", any(c.isdigit() for c in password))
print("Contains Symbols:", any(c in string.punctuation for c in password))