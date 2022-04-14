print("MANDAVA HARIPRASAD")
import requests
from pprint import pprint
username  = "HariprasadMandava"
url = f"https://api.github.com/users/{username}"
user_data = requests.get(url).json()
pprint(user_data)