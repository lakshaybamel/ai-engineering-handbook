# Count words in a file

filename = input("Enter file name: ")

with open(filename, "r") as f:
    text = f.read()

words = text.split()
print("Word count:", len(words))
