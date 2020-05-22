"""

Exclusive Books is an Angular app, and some custom components like
`<product-price>` makes it easy to identify elements.

Because it's an SPA rendered using JavaScript on the client side, we cannot
scrape it without something like Selenium or Puppeteer.

"""
import scrapy

HOST = "https://www.exclusivebooks.co.za"
LIST_ITEM_SELECTOR = ".horizontal-product-list > .product-list"
LIST_THUMBNAIL_SELECTOR = "product-image img::attr(src)"
DETAIL_LINK_SELECTOR = "a.item-inner::attr(href)'"
TITLE_SELECTOR = ".product-name > p::text"
AUTHOR_SELECTOR = ".product-author > a::text"
PRICE_SELECTOR = "product-price > p::text"
FORMAT_SELECTOR = ".product-format > span::text"


def get_search_url_for_isbn(isbn: str):
    return f"{HOST}/search?expedite=&keyword={isbn}"


class ExclusiveBooksSearchSelenium:
    """
    This doesn't really work, I wrote it before I realized this would need selenium
    """

    name = "exclusive-books"

    def __init__(self, isbn: str, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.start_urls = [get_search_url_for_isbn(isbn)]

    def parse(self, response):
        for listing in response.css(LIST_ITEM_SELECTOR):
            breakpoint()
            yield {
                "title": listing.css(TITLE_SELECTOR).get(),
                "author": listing.css(AUTHOR_SELECTOR).get(),
                "price": listing.css(PRICE_SELECTOR).get(),
                "thumbnail": listing.css(LIST_THUMBNAIL_SELECTOR).get(),
            }
        #
        # next_page = response.css('li.next a::attr("href")').get()
        # if next_page is not None:
        #     yield response.follow(next_page, self.parse)
