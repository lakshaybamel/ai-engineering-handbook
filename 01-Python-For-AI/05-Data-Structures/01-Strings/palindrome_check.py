# Check if a string is palindrome

text = input("Enter a word: ").lower()

if text == text[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")
