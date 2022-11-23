import requests
# import re # uncomment this for DVWA
from bs4 import BeautifulSoup as bs
from urllib.parse import urljoin
from pprint import pprint

s = requests.Session()
s.headers["User-Agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36"



# below code is for logging to your local DVWA
# uncomment it if you want to use this on DVWA

# login_payload = {
#     "username": "admin",
#     "password": "password",
#     "Login": "Login",
# }
# # change URL to the login page of your DVWA login URL
# login_url = "http://localhost:8080/DVWA-master/login.php"

# # login
# r = s.get(login_url)
# token = re.search("user_token'\s*value='(.*?)'", r.text).group(1)
# login_payload['user_token'] = token
# s.post(login_url, data=login_payload)




