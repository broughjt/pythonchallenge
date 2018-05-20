import urllib.request
import re


html = urllib.request.urlopen("http://www.pythonchallenge.com/pc/def/ocr.html").read().decode()
mess = re.findall(r"<!--(.*?)-->", html, re.DOTALL)[-1]

count = {}

for i in mess:
    count[i] = count.get(i, 0) + 1

print("".join(re.findall("[A-Za-z]", mess)))
