import urllib.request
import pickle


data = pickle.load(urllib.request.urlopen("http://www.pythonchallenge.com/pc/def/banner.p"))

for line in data:
    print("".join([k * v for k, v in line]))
