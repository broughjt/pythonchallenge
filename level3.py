import urllib.request
import re


html = urllib.request.urlopen("http://www.pythonchallenge.com/pc/def/equality.html").read().decode()

pattern = re.compile(r"<!--(.*?)-->", re.DOTALL)
mess = pattern.findall(html)[-1]

key = re.findall(r"[^A-Z]+[A-Z]{3}([a-z])[A-Z]{3}[^A-Z]+", mess)
print("".join(key))
