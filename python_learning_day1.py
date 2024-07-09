import requests
import bs4

#python.exe -m pip list 可以查看python 目前的模組
res=requests.get("https://www.google.com/search?client=firefox-b-d&q=google")

soup=bs4.BeautifulSoup(res.text)
print(res)
print(soup)
print("hello world")
print("123")