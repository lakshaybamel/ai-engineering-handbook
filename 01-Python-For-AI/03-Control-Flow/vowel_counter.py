# Count vowels in a string

text = input("Enter a word: ").lower()
count = 0

for ch in text:
    if ch in "aeiou":
        count += 1

print("Number of vowels:", count)
