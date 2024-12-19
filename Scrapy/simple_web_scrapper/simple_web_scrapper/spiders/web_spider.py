import scrapy

class BookSpider(scrapy.Spider):
    name = 'webPageSpider'
    start_urls = ['https://books.toscrape.com/']

    def parse(self, response):
          link=response.css('a::attr(href)').getall()
          for l in link:
            yield {
                  'link': l,
            }

