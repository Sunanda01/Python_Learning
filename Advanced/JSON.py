import json
data = {
    "name": "Alice",
    "age": 25,
    "is_student": False,
    "skills": ["Python", "ML"],
    "address": {"city": "Delhi", "pin": 110001}
}

# Converting Python → JSON (Serialization)
json_data=json.dumps(data,indent=4)
print(json_data)

# Save to a file
with open("data.json","w") as f:
    json.dump(data,f,indent=4)

# JSON → Python (Deserialization)
py_data=json.loads(json_data)
print(f"Name is {py_data['name']} Age is {py_data['age']} Skills are {py_data['skills'][0]} and {py_data['skills'][1]}")
