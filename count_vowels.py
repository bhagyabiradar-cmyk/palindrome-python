text = input("Enter a word or sentence: ")

count = 0
vowels = "aeiouAEIOU"

for ch in text:
    if ch in vowels:
        count += 1

print("Number of vowels:", count)