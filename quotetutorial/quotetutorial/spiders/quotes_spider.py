import scrapy
from ..items import QuotetutorialItem


class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    start_urls = [
        'https://quotes.toscrape.com/'
    ]

    def parse(self, response, **kwargs):
        items = QuotetutorialItem()
        all_div_quotes = response.css('div.quote')

        for quotes in all_div_quotes:

            items['title'] = quotes.css('span.text::text').extract_first()
            items['author'] = quotes.css('.author::text').extract()
            items['tags'] = quotes.css('.tag::text').extract()

            yield items
