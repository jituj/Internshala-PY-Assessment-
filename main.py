import re
import requests

def check_wordpress(domain):
    url = f"http://{domain}"
    try:
        response = requests.get(url)
    except:
        return False

    if response.status_code != 200:
        return False

    regex = re.compile("wp-content|wp-includes|wp-admin")
    # regex = re.compile(r"Version\s*(\d+\.\d+(\.\d+)?)")
    if regex.search(response.text):
        return True
    else:
        return False

# Example usage
domain = input("Enter domain name: ")
if check_wordpress(domain):
    print(f"{domain} is running on WordPress")
else:
    print(f"{domain} is not running on WordPress")








