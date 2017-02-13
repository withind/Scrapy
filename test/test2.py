from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

def getLinks(articleUrl):
    html = urlopen("http://desk.zol.com.cn/1440x900/")
    bsObj = BeautifulSoup(html)
    for link in bsObj.findAll("a"):
        if 'href' in link.attrs:
            print(link.attrs['href'])


