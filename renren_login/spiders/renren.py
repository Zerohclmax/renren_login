# -*- coding: utf-8 -*-
import scrapy


class RenrenSpider(scrapy.Spider):
    name = 'renren'
    allowed_domains = ['renren.com']
    start_urls = ['http://renren.com/']

    # def parse(self, response):
    #     pass
    def start_requests(self):##重写
        url = "http://www.renren.com/Plogin.do"
        data={"email":"970138074@qq.com",'password':"pythonspider"}
        request = scrapy.FormRequest(url,formdata=data,callback=self.parse_page)##post请求
        yield request
    def parse_page(self,response):
        with open("reren.html",'w',encoding='utf-8')as fp:
            fp.write(response.text)



