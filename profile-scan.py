from bs4 import BeautifulSoup
import requests
from collections import Counter

content = ""
with open('html-body.html', encoding="utf8") as f:
    content = f.read()
soup = BeautifulSoup(content,'html.parser')
find_link = soup.find('a')
link = find_link.get('href').split('?')[0]
#r = requests.get(link+'/about')
with open('nitzan-about.html', encoding="utf8") as f:
    content = f.read()
soup2 = BeautifulSoup(content, 'html.parser')
soup2_images = soup2.find_all('img')
home_image_src = 'https://static.xx.fbcdn.net/rsrc.php/v3/yS/r/poZ_P5BwYaV.png'
location = ''
for image in soup2_images:
    print(image.attrs.get('src'))
    if image.attrs.get('src') == home_image_src:
        location = image.parent.parent.find('span').text

def get_locations(html):
    location_list = []
    soup = BeautifulSoup(html, 'html.parser')
    for link in soup.find_all('a'):
        location = find_location(link)
        location_list.append(location)
    return Counter(location_list)

def find_location(link):
    home_image_src = 'https://static.xx.fbcdn.net/rsrc.php/v3/yS/r/poZ_P5BwYaV.png'
    r = requests.get(link + '/about')
    soup = BeautifulSoup(r.content, 'html.parser')
    soup_images = soup.find_all('img')
    for image in soup_images:
        print(image.attrs.get('src'))
        if image.attrs.get('src') == home_image_src:
            return image.parent.parent.find('span').text






