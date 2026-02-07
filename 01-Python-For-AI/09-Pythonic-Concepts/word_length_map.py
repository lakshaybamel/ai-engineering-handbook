# Map words to their lengths using dictionary comprehension

words = input("Enter words: ").split()

length_map = {word: len(word) for word in words}

print(length_map)