# _*_ coding: utf-8 _*_
#20170208
#20170209  增加1440*900特定壁纸
#20170212  补全一个系列的所有图片按指定尺寸下载

from scrapy.spiders import CrawlSpider
from scrapy.selector import Selector
from zolimg.items import ZolimgItem
from scrapy.http import Request
from urllib import request
import os
import re
import time


def download_pic(url):                                    #下载图片
    time_now=time.strftime('%Y_%m_%d',time.localtime(time.time()))
    first_name =time_now+'_'+url[-10:]
    path = '/Users/Air/Scrapy/zolimg/pics/'
    name = path + first_name

    if not os.path.exists(name):                    #判断文件路径是否存在
        request.urlretrieve(url,name)
    else:
        print ("this is exists error..........")


class Zolimg(CrawlSpider):
    name = "zolimg"                             #必备属性1
    start_urls = ['http://desk.zol.com.cn/']    #必备属性2

    url = 'http://desk.zol.com.cn'    #备用url
    url2 = 'http://desk.zol.com.cn/1440x900'
    need_FW='1440x900'


    def parse(self,response):
        item = ZolimgItem()
        myneed= Selector(response).xpath('//body')
        for eachimg in myneed:
            first_href = eachimg.xpath('//ul[@class="pic-list2 clearfix"]/li/a/@href').extract()[5]
            print (first_href)
            print ('1'*100)
            new_first_href= Zolimg.url+first_href   #二层图片链接
            print(new_first_href)
            print ('2'*100)
            yield Request(new_first_href,callback=self.parse2)


    def parse2(self,response):                 #二层爬虫
        item=ZolimgItem()
        myneed2=Selector(response).xpath('//body')
        for eachimg2 in myneed2:
            second_href=eachimg2.xpath('//dl[@class="model wallpaper-down clearfix"]/dd[@id="tagfbl"]/a/@href').extract()[0]
            second_href_limit=eachimg2.xpath('//ul[@id="showImg"]/li/a/@href').extract()
            #second_href_max=eachimg2.xpath('//ul[@id="showImg"]/li[@class="show1"]/i/*').extract()
            #print(second_href_limit)
            str=','.join(second_href_limit)
            new_str=re.findall("_(.*?)_",str)
            print(new_str)                                      #提取出该系列所有图片
                                                                #http://desk.zol.com.cn/showpic/1920x1080_86480_14.html

            for i in range(len(new_str)):
                new_second_href=Zolimg.url+second_href
                new2_second_href=new_second_href[:31]+self.need_FW+'_'+new_str[i]+'_'+new_second_href[47:-1]+'l'
                print(new2_second_href)
                i+=1
                yield Request(new2_second_href,callback=self.parse3)


    def parse3(self,response):                 #三层爬虫
        myneed3=Selector(response).xpath('//body')
        for eachimg3 in myneed3:
            third_href = eachimg3.xpath('//img/@src').extract()
            str_third_href=''.join(third_href)
            download_pic(str_third_href)













