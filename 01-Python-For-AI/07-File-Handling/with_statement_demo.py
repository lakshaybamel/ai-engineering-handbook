# Using with statement

# writing
with open("safe.txt", "w") as f:
    f.write("File handled safely\n")

# reading
with open("safe.txt", "r") as f:
    print(f.read())