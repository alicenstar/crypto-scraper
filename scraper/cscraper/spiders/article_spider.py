import scrapy
from cscraper.items import ArticleItem

class ArticleSpider(scrapy.Spider):
    name = "articles"
    start_urls = ["https://www.reddit.com/r/CryptoCurrency/"]

    def parse(self, response):
        data = response.css("h3")

        for line in data:
            item = ArticleItem()
            item["header"] = line.css("h3::text").extract_first()
            print("item", item)
            yield item
