import scrapy

class UrlsspiderSpider(scrapy.Spider):
    name = 'dubsurlspider'
    start_urls = ['http://www.dublingaa.ie/results']

    def parse(self, response):
                for details in response.css('div.comp'):
                    yield { 
                        'Competition':details.css('a::text').get(),
                        'URL':details.css('a').attrib['href'],  
                    }        

                    next_page = response.css('a.next').attrib['href']
                    if next_page is not None:
                        yield response.follow(next_page, callback=self.parse)
