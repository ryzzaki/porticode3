from bs4 import BeautifulSoup
import requests
import re
import sys
import os
import http.cookiejar
import json
import urllib.request, urllib.error, urllib.parse
import json

name_array = []

def get_soup(url,header):
    return BeautifulSoup(urllib.request.urlopen(
        urllib.request.Request(url,headers=header)), 'html.parser')

query = input("Enter the query: ").lower().strip()
search_word = query.replace(" ", "_")
url="http://www.bing.com/images/search?q=" + search_word + "&FORM=HDRSC2"
DIR='Pictures'
header={'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36"}
soup = get_soup(url,header)
ActualImages=[]

for a in soup.find_all("a",{"class":"iusc"}):
    mad = json.loads(a["mad"])
    turl = mad["turl"]
    m = json.loads(a["m"])
    murl = m["murl"]
    image_name = urllib.parse.urlsplit(murl).path.split("/")[-1]
    print(image_name)
    name_array.append(image_name)
    ActualImages.append((image_name, turl, murl))

with open('nameray.json', 'w') as outfile:
    json.dump(name_array, outfile)

print("there are total" , len(ActualImages),"images")

if not os.path.exists(DIR):
    os.mkdir(DIR)

DIR = os.path.join(DIR, search_word.split()[0])

if not os.path.exists(DIR):
    os.mkdir(DIR)

for i, (image_name, turl, murl) in enumerate(ActualImages):
    try:
        raw_img = urllib.request.urlopen(turl).read()
        cntr = len([i for i in os.listdir(DIR) if image_name in i]) + 1
        f = open(os.path.join(DIR, image_name), 'wb')
        f.write(raw_img)
        f.close()
    except Exception as e:
        print("could not load : " + image_name)
        print(e)
