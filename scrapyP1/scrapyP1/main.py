from scrapy.cmdline import execute
import os
import sys

# print(__file__ + "\n")
# print(os.path.abspath(__file__) + "\n")
# print(os.path.dirname(os.path.abspath(__file__)) + "\n")
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
# print(sys.path)
execute(["scrapy", "crawl", "xiaohuar", "--nolog"])

# from scrapy.selector import Selector
# from scrapy.http import HtmlResponse
# html = """<!DOCTYPE html>
# <html>
# <head lang="en">
#     <meta charset="UTF-8">
#     <title></title>
# </head>
# <body>
#     <li class="item-"><a href="link.html">first item</a></li>
#     <li class="item-0"><a href="link1.html">first item</a></li>
#     <li class="item-1"><a href="link2.html">second item</a></li>
# </body>
# </html>
# """
# response = HtmlResponse(url='http://example.com', body=html,encoding='utf-8')
# ret = Selector(response=response).xpath('//li[re:test(@class, "item-\d*")]//@href').extract()
# print(ret)