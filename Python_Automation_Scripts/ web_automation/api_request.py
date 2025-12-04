import requests

def get_api(url):
    response = requests.get(url)
    if response.status_code == 200:
        print("API Data:", response.json())
    else:
        print("Request Failed:", response.status_code)

# Example
get_api("https://api.github.com/users/octocat")
