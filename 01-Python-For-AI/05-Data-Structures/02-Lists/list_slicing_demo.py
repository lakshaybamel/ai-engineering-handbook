# Demonstration of list slicing

numbers = [10, 20, 30, 40, 50, 60]

print("Original:", numbers)
print("Slice 1:4 ->", numbers[1:4])
print("Every second element ->", numbers[::2])
print("Reverse ->", numbers[::-1])

# copy vs reference
a = [1, 2, 3]
b = a
b[0] = 99
print("Reference change:", a)

c = a[:]
c[1] = 77
print("Copy change:", a)