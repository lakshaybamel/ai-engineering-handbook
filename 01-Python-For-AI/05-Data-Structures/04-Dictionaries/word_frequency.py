# Count frequency of words in a sentence

text = input("Enter a sentence: ").lower().split()

freq = {}

for word in text:
    if word in freq:
        freq[word] += 1
    else:
        freq[word] = 1

print("Word Frequency:")
for word, count in freq.items():
    print(word, ":", count)
