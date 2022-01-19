import re

def isValidURL(url):
    if re.search("(^(https:))|^(http:)",url):
        print("valid")

URL = 'https://www.w3schools.com'
isValidURL(URL)