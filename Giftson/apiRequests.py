"""
Python program to create a simple API call request
using 'requests' library

Requirements:
requests library (pip install requests)

How to run?
just run the code and the value for activity key is printed

Sample Output:
Learn to play a new instrument
"""
# importing requests library
import requests

# using the get() function and the url as a parameter to get the data from the url
request = requests.get("https://www.boredapi.com/api/activity")

# storing the data as a dictionary using json() function
apiValues = request.json()

# printing the generated values
print(apiValues["activity"])

# printing specific key:value pair according to our needs (Not Necessary)
# print(apiValues[input(f"{list(apiValues.keys())} \nWhat key value pair do you want? Hint: Type one key from the above list\n")])
