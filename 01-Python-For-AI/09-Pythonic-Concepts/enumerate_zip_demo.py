# enumerate and zip demonstration

names = ["Lakshay", "Rahul", "Amit"]
marks = [95, 88, 76]

print("Using enumerate:")
for index, name in enumerate(names):
    print(index, name)

print("\nUsing zip:")
for name, mark in zip(names, marks):
    print(name, mark)