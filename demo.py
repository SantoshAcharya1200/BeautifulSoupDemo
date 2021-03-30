from bs4 import BeautifulSoup as bs
import requests

url="https://www.jobsnepal.com/search?q=python"
req= requests.get(url)
soup= bs(req.text,"html.parser")
tags= soup.find_all('strong', abc="title tw-line-height-12")
print(tags)
