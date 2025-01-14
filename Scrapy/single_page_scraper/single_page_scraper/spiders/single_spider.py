import scrapy

class BookSpider(scrapy.Spider):
    name = 'singlePageSpider'
    start_urls = ['https://books.toscrape.com/catalogue/category/books/mystery_3/index.html']

    def parse(self, response):
        page_title = response.css('h1::text').get()
        print(f'Page title: {page_title}')

        for book in response.css('article.product_pod'):
            title = book.css('h3 a::attr(title)').get()
            url = book.css('h3 a::attr(href)').get()  # Fixed typo here

            yield {
                'page_title': page_title,
                'title': title,
                'url': response.urljoin(url),
            }

        next_page = response.css('li.next a::attr(href)').get()
        if next_page is not None:
            next_page_url = response.urljoin(next_page)
            yield scrapy.Request(url=next_page_url, callback=self.parse)