
import requests
import time
import webbrowser
import datetime
import json

time.sleep(3)  # Sleep for 3 seconds to avoid hitting the API rate limit

'''
webbrowser.open("https://www.srholdings.in/")
output = requests.get("https://www.google.com")
print(output)
'''
date = datetime.datetime.now()
print("Current date and time:", date)

json_data = {
    "name": "Saravanan",
    "age": 25,
    "city": "Chennai"}

print("JSON data:", json.dumps(json_data, indent=4))



print("JSON data:", json.dumps(json_data))

python_dict=json.loads(json.dumps(json_data))
print("Python dictionary:", python_dict)