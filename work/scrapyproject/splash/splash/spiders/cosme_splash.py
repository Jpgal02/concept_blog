import scrapy


class CosmeSplashSpider(scrapy.Spider):
    name = 'cosme_splash'
    allowed_domains = ['www.cosme.net']
    start_urls = ['http://www.cosme.net/']

    def parse(self, response):
        pass
