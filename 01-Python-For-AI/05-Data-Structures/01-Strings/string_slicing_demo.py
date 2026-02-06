# Demonstrating string slicing

text = input("Enter a word: ")

print("First 3 characters:", text[:3])
print("Last 3 characters:", text[-3:])
print("Reversed:", text[::-1])
print("Every second character:", text[::2])