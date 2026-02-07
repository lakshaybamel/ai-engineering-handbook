# Copy content from one file to another

source = input("Enter source file name: ")
destination = input("Enter destination file name: ")

with open(source, "r") as s:
    content = s.read()

with open(destination, "w") as d:
    d.write(content)

print("File copied successfully")
