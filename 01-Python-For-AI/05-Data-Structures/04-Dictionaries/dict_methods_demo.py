# Dictionary methods demo

student = {"name": "Lakshay", "age": 23}

print("Keys:", student.keys())
print("Values:", student.values())
print("Items:", student.items())

print("Get name:", student.get("name"))
print("Get marks:", student.get("marks"))

student.update({"city": "Delhi"})
print("After update:", student)

student.pop("age")
print("After pop:", student)

student.popitem()
print("After popitem:", student)

student.clear()
print("After clear:", student)
