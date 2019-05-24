import scrapy



class ZhaiNanSpider(scrapy.Spider):
    name = "zhainan"
    allowed_domains = ['www.zhainanfu.com']
    start_urls = ['https://www.zhainanfu.com/tuku']

    def parse(self, response):
        pass