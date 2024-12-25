import scrapy


class SpiderStarbucksSpider(scrapy.Spider):
    name = "spider_starbucks"
    allowed_domains = ["www.starbucks.com"]
    start_urls = ["https://www.starbucks.com/store-locator?place=North Carolina"]

    def parse(self, response):
                # Extract store information using Scrapy's selectors
        stores = response.xpath('//div[@data-e2e="location-card-details"]')
        print(stores)
        for store in stores:
            yield {
                "name": store.xpath('.//h3/text()').get(),
                "address": store.xpath('.//p[@data-e2e="address"]/text()').get(),
            }
