from collections.abc import AsyncIterator, Iterator

import scrapy
from scrapy.http import Response

from src.items import QuoteItem


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    allowed_domains = ["quotes.toscrape.com"]

    async def start(self) -> AsyncIterator[scrapy.Request]:
        yield scrapy.Request("https://quotes.toscrape.com/")

    def parse(self, response: Response) -> Iterator[QuoteItem | scrapy.Request]:
        for quote in response.css("div.quote"):
            yield QuoteItem(
                text=quote.css("span.text::text").get(default=""),
                author=quote.css("small.author::text").get(default=""),
                tags=quote.css("a.tag::text").getall(),
            )

        next_page = response.css("li.next a::attr(href)").get()
        if next_page:
            yield response.follow(next_page, callback=self.parse)
