import os
import json
import requests
from datetime import datetime



# ############################    Request    ############################
# response = requests.get("https://api.github.com")
# print(response.status_code)      # 200 means OK
# print(response.text)             # Raw text data
# print(response.json())           # Converts JSON response into a Python dictionary
# ################# example
# payload = {'username': 'John', 'password': '1234'}
# response = requests.post('https://httpbin.org/post', data=payload)
# print(response.json())


############################    json – Working with JSON Data    ############################

### Convert Python dictionary → JSON string
# data = {'name': 'Ramanlal', 'age': 12}
# json_string = json.dumps(data)
# print(json_string)  # Output: {"name": "Alice", "age": 25}


### Convert JSON string → Python dictionary
# json_data = '{"name": "Alice", "age": 12}'
# parsed_data = json.loads(json_data)
# print(parsed_data['name'])  # Output: Alice


### Save and load JSON to/from file
# Save to file
# with open("data.json", "w") as f:
    # json.dump(data, f)

# Load from file
# with open("data.json", "r") as f:
    # loaded_data = json.load(f)
# 
# print(loaded_data)



# ############################    datetime – Dates and Times in Python    ############################
# now = datetime.now()
# print(now)

# # Format the date and time

# formatted = now.strftime("%Y-%m-%d %H:%M:%S")
# print(formatted)  # e.g., 2025-08-21 14:30:45

# # Parse a date string into a datetime object
# date_str = "2025-08-21"
# date_obj = datetime.strptime(date_str, "%Y-%m-%d")
# print(date_obj)

# # Add or subtract days
# from datetime import timedelta

# yesterday = now - timedelta(days=1)
# today = datetime.now()
# tomorrow = now + timedelta(days=1)
# print("Yesterday:", yesterday)
# print("Today:", today)
# print("Tomorrow:", tomorrow)





############################    os – Interacting with Your Operating System    ############################
# print(os.getcwd())  # Shows where your Python script is running


# List all files and folders in a directory
# files = os.listdir(".")
# print(files)


### os.mkdir("new_folder")
# os.rmdir("new_folder")

##Read environment variables
# home = os.getenv("HOME")  # or USERPROFILE on Windows
# print("Home directory:", home)





# Step 1: Make a request to an API
url = "https://api.github.com"
response = requests.get(url)
data = response.json()

# Step 2: Prepare filename using datetime
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
filename = f"github_data_{timestamp}.json"

# Step 3: Save data to a file
with open(filename, "w") as file:
    json.dump(data, file, indent=4)

# Step 4: Print where file is saved
print(f"Data saved to {os.path.abspath(filename)}")
