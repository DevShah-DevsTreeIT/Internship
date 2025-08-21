# JSON Data Processor: Read, modify, and write JSON files with complex nested structures
import os
import json

# Step 1: Load JSON data from file
with open("employees.json", "r") as f:
    loaded_data = json.load(f)

# Step 2: Modify the data
for employee in loaded_data["employees"]:
    if employee["id"] == 1:
        # Increase age by 1
        employee["details"]["age"] += 1

        # Add a new skill
        employee["skills"].append("Teamwork")

        # Uppercase the department
        employee["department"] = employee["department"].upper()

        # Add a new key-value pair
        employee["active"] = True

# Step 3: Save the modified data to a new JSON file
with open("updated_employees.json", "w") as file:
    json.dump(loaded_data, file, indent=4)

# Step 4: Print path to the saved file
print(f"Data saved to {os.path.abspath('updated_employees.json')}")
