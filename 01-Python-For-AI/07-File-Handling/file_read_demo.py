# Reading file demonstration

f = open("demo.txt", "r")

print("Using read():")
print(f.read())

f.close()

f = open("demo.txt", "r")

print("\nUsing readline():")
print(f.readline())

f.close()

f = open("demo.txt", "r")

print("\nUsing readlines():")
print(f.readlines())

f.close()