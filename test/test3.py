# _*_ coding: utf-8 _*_
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import os

#{"href":re.compile("\/bizhi\/*[0-9]*\_*[0-9]*\_*[0-9]*\.html")}
#<li class="photo-list-padding">
html = urlopen("http://desk.zol.com.cn/1440x900/")
bsObj = BeautifulSoup(html,"lxml")
for link in bsObj.find("ul",{"class":"pic-list2 clearfix"}).findAll("li"):
    print(link)
