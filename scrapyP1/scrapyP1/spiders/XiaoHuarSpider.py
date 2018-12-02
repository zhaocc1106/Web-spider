#
# Copyright (c) 2018 Baidu.com, Inc. All Rights Reserved
#
"""
The HTML spider by scrapy.

Authors: zhaochaochao(zhaochaochao@baidu.com)
Date:    2018/12/2 9:22
"""

# The common libs.
import os

# The 3rd-part libs.
import scrapy
import urllib.request
from scrapy.selector import HtmlXPathSelector
from scrapyP1 import *

class XiaoHuarSpider(scrapy.spiders.Spider):
    name = "xiaohuar"
    allowed_domains = ["xiaohuar.com"]
    start_urls = [
        "http://www.xiaohuar.com/hua/",
    ]

    def parse(self, response):
        # print("response :\n", response)
        # print("reponse body_as_unicode:\n", response.body_as_unicode())
        print("response url :\n", response.url)
        print("response headers :\n", response.headers)
        # print("reponse body:\n", response.body)

        hxs = HtmlXPathSelector(response)
        print("response url: \n", response.url)

        # from scrapy.http.cookies import CookieJar
        # cookieJar = CookieJar()
        # cookieJar.extract_cookies(response, response.request)
        # print("cookie :\n", cookieJar._cookies)

        # if re.match('http://www.xiaohuar.com/list-1-\d+.html', response.url):
        #     print("true")
        # else:
        #     print("false")

        items = hxs.select('//div[@class="item_list infinite_scroll"]/div')
        print("items lenth: \n", range(len(items)))
        for i in range(len(items)):
            # print("item: \n", item)
            src = hxs.select('//div[@class="item_list infinite_scroll"]/div[%d]//div[@class="img"]/a/img/@src'% (i)).extract()
            print(src)
            name = hxs.select('//div[@class="item_list infinite_scroll"]/div[%d]//div[@class="img"]/span/text()' % i).extract()
            print(name)
            school = hxs.select('//div[@class="item_list infinite_scroll"]/div[%d]//div[@class="img"]/div[@class="btns"]/a/text()' % i).extract()
            print(school)
            item = Scrapyp1Item()
            item['school'] = school
            item['name'] = name
            item['src'] = src
            yield item

            if src:
                ab_src = "http://www.xiaohuar.com" + src[0]
                file_name = "%s_%s.jpg" % (school[0], name[0])
                file_path = os.path.join("E:/Users/zhaocc/PycharmProjects/scrapyP1", file_name)
                urllib.request.urlretrieve(ab_src, file_path)
                print("save the img successfully!")
