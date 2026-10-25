from scrapy.http import HtmlResponse, Request

from src.items import QuoteItem
from src.spiders.quotes import QuotesSpider

URL = "https://quotes.toscrape.com/"
BODY = b"""
<div class="quote">
  <span class="text">Simplicity is prerequisite for reliability.</span>
  <small class="author">Edsger W. Dijkstra</small>
  <a class="tag">simplicity</a>
</div>
<ul class="pager"><li class="next"><a href="/page/2/">Next</a></li></ul>
"""


def test_parse_extracts_quotes_and_follows_next_page() -> None:
    response = HtmlResponse(url=URL, body=BODY, encoding="utf-8", request=Request(URL))

    item, next_request = QuotesSpider().parse(response)

    assert item == QuoteItem(
        text="Simplicity is prerequisite for reliability.",
        author="Edsger W. Dijkstra",
        tags=["simplicity"],
    )
    assert next_request.url == "https://quotes.toscrape.com/page/2/"
