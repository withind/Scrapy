# _*_ coding:=utf-8 _*_
#20170208
#yield item   yield返回一个生成器,可用for循环print出来

from scrapy.spiders import CrawlSpider
from scrapy.selector import Selector
from scrapy.http import Request
from img_spider.items import ImgSpiderItem
import os
import re
import urllib
import time

next_page_link = []

def download_pic(url):      #下载图片
    first_name = url[-10:]
    path = '/Users/Air/Scrapy/zolimg/pics/'
    name = path+first_name.replace('/','.')

    if not os.path.exists(name):  #判断文件路径是否存在
        date = urllib.urlretrieve(url,name)
    else:
        print ("this is exists error..........")


class Deskspider(CrawlSpider):
    name = "desk"                                  #定义爬虫的名字
    url = 'http://desk.zol.com.cn/'      #定义好爬虫网站

    start_urls = [
        'http://desk.zol.com.cn/1440x900/'
    ]                                             #定义好爬虫初始范围


    def parse(self,response):
        item = ImgSpiderItem()                  #parse是回调函数
        for href in response.xpath('//div[@class="main"]/ul/li/a/img/@herf').extract()
        yield scrapy.Request('http://desk.zol.com.cn'+herf,callback=parse_url)

        page_link = response.xpath('//div[@class="page"]/a/@herf').extract()
        full_page_link ='http://desk.zol.com.cn'+page_link[-1]
        if full_page_link not in next_page_link:
            yield scrapy.Request(full_page_link,callback=parse)

    def parse_url(self,response):
        imglist = response.xpath('//ul[@id="showImg"]/li/a/img').extract()
        reg = (r'http:.*?\.jpg')
        for i in imglist:
            img = re.findall(reg,i)
            item['img'] = img
            yield item

            for url in item['img']:
                download_pic(url)
                print('='*20)





