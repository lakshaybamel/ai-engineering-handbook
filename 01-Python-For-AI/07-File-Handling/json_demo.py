# JSON demonstration

import json

# writing JSON
data = {
    "name": "Lakshay",
    "course": "AI",
    "marks": 95
}

with open("student.json", "w") as f:
    json.dump(data, f)

# reading JSON
with open("student.json", "r") as f:
    loaded = json.load(f)

print("Loaded Data:", loaded)