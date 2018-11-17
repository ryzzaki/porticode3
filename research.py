import start
from bs4 import BeautifulSoup
import requests
import re

st = start.Start()

def download():
    site = 'https://google.com/search?q=' + st.topic + '&tbm=isch'

    response = requests.get(site)

    soup = BeautifulSoup(response.text, 'html.parser')
    img_tags = soup.find_all('img')

    urls = [img['src'] for img in img_tags]


    for url in urls:
        filename = re.search(r'/([\w_-]+[.](jpg|gif|png))$', url)
        with open(filename.group(1), 'wb') as f:
            if 'http' not in url:
                url = '{}{}'.format(site, url)
            response = requests.get(url)
            f.write(response.content)
