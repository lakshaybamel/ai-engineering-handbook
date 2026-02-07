# Writing to file demonstration

# write mode
f = open("demo2.txt", "w")
f.write("This is a new file\n")
f.close()

# append mode
f = open("demo2.txt", "a")
f.write("Appending a second line\n")
f.close()

# verify content
f = open("demo2.txt", "r")
print(f.read())
f.close()
