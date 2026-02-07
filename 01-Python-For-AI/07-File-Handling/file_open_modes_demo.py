# Demonstrate file modes

# write mode
f = open("demo.txt", "w")
f.write("Hello Lakshay\n")
f.close()

# append mode
f = open("demo.txt", "a")
f.write("Learning File Handling\n")
f.close()

# read mode
f = open("demo.txt", "r")
content = f.read()
print(content)
f.close()