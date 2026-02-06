# Demonstration of common string methods

text = input("Enter a sentence: ")

print("Lowercase:", text.lower())
print("Uppercase:", text.upper())
print("Stripped:", text.strip())
print("Replace 'a' with '*':", text.replace("a", "*"))
print("First occurrence of 'a':", text.find("a"))
print("Count of 'a':", text.count("a"))

words = text.split()
print("Split words:", words)

joined = "-".join(words)
print("Joined with hyphen:", joined)
