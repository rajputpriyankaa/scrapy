import scrapy


class ScraperSpider(scrapy.Spider):
    name = "scraper"
    allowed_domains = ["www.scrapingcourse.com"]
    start_urls = ["https://www.scrapingcourse.com/ecommerce/"]
    def start_requests(self):
        headers = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-US,en;q=0.9',
            'cache-control': 'no-cache',
            'pragma': 'no-cache',
            'priority': 'u=0, i',
            'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36',
        }
        for url in self.start_urls:
            yield scrapy.Request(url=url, headers=headers, callback=self.parse)

    def parse(self, response):
        for products in response.css('[data-products="item"]'):
            print('inside')
            url = products.css('a::attr(href)').get()
            title = products.css('h2.product-name.woocommerce-loop-product__title::text').get()
            img_url = products.css('img::attr(src)').get()
            price = products.css('span.product-price.woocommerce-Price-amount.amount bdi::text').get()
            product_dict = dict(url=url, title=title, image_url=img_url, price=price)
            self.log(f'product_dict : {product_dict}')
            yield product_dict

        next_page = response.css('a.next.page-numbers::attr(href)').get()
        print(f'page extraction : {next_page}', end='\n')
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)
            # yield url
