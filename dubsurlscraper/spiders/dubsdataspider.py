import scrapy


class DubsspiderSpider(scrapy.Spider):
    name = 'dubsdataspider'
    with open("U16urls", "rt") as f:
        start_urls = [url.strip() for url in f.readlines()]

    def parse(self, response):
        for quote in response.css('a.row.fixture_row'):
            yield {
                'Competition':response.css('h1::text').get(),
                'date':quote.css('div.date::text').get(),
                'time':quote.css('div.time::text').get(),
                'Venue':quote.css('div.venue::text').get(),
                'HomeTeam':quote.css('div.home::text').get(),
                'Home Score':quote.css('div.score span::text').get(),
                'Away Score':quote.css('div.score_a span::text').get(),
                'Away team':quote.css('div.away::text').get(),
                'Ref':quote.css('div.ref::text').get(),

                }


