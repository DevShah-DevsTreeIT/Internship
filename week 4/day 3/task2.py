#Package Installation Practice:- 


#  matplotlib
import matplotlib.pyplot as plt

x = [1, 2, 3, 4,5]
y = [10, 20, 25, 30,35]

plt.plot(x, y)
plt.title("Line Chart")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()



# request
# pip install requests



import requests

# 1. Make a GET request with query parameters
get_url = 'https://httpbin.org/get'
params = {'search': 'python', 'page': 2}

response_get = requests.get(get_url, params=params)
print("GET Request:")
print("Status Code:", response_get.status_code)
print("Response JSON:", response_get.json())
print()

# 2. Make a POST request with form data
post_url = 'https://httpbin.org/post'
data = {'username': 'john', 'password': 'secret'}

response_post = requests.post(post_url, data=data)
print("POST Request:")
print("Status Code:", response_post.status_code)
print("Response JSON:", response_post.json())
print()

# 3. Sending headers
headers = {'User-Agent': 'MyPythonApp/1.0'}
response_headers = requests.get(get_url, headers=headers)
print("GET with Headers:")
print("Headers Sent:", response_headers.request.headers)
print("Response JSON:", response_headers.json())
