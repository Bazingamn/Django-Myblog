# -*- coding: utf-8 -*-
import scrapy
from DoubanScrapy.items import DoubanscrapyItem


class DoubanbookSpider(scrapy.Spider):
    name = 'doubanbook'
    # allowed_domains = ['doubanbook.com']
    #     # start_urls = ['http://doubanbook.com/']
    def start_requests(self):
        for a in range(10):
            url = 'https://book.douban.com/top250?start={}'.format(a * 25)
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        items = []
        for book in response.xpath('//*[@id="content"]/div/div[1]/div/table'):
            item = DoubanscrapyItem()
            item['title'] = book.xpath("./tr/td[2]/div[1]/a/@title").extract_first().replace('\n', '').strip()
            item['score'] = book.xpath("./tr/td[2]/div[2]/span[2]/text()").extract_first().replace('\n', '').strip()
            item['scrible'] = book.xpath("./tr/td[2]/p[2]/span/text()").extract_first().replace('\n', '').strip()
            item['num'] = book.xpath("./tr/td[2]/div[2]/span[3]/text()").extract_first().strip("(").strip(")").replace(
                '\n', '').strip()
            item['img'] = book.xpath("./tr/td[1]/a/img/@src").extract_first().replace('\n', '').strip()
            items.append(item)

        print(items)
        return items
