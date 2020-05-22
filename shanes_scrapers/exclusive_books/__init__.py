"""

Exclusive Books is an Angular app and isn't rendered on the server,
so the HTML is not useful for scraping. Instead, there is a JSON blob
with data that can be read. This is hokey!

Check out ./example_json.py for an example.

"""
import json
import re
import scrapy

HOST = "https://www.exclusivebooks.co.za"
JS_SELECTOR = "body > script"
JSON_PATTERN = r"searchData',\s*({.*})\);"


def get_search_url_for_isbn(isbn: str):
    return f"{HOST}/search?expedite=&keyword={isbn}"


def get_author(data: dict):
    for contributor in data["contributor"]:
        if contributor["contributorRole"] == "Author":
            return contributor["contributorName"]
    return "Unknown"


def transform_data(data: dict):
    return [
        {
            "title": product["itemPrimaryName"],
            "author": get_author(product),
            "format": product["formatText"],
            "barcode": product["eanCode"],
            "price": product.get("bestAvailability", {}).get("websitePrice", 0),
            "leadtime": product.get("bestAvailability", {}).get("leadTimeDays", 0),
            "available": product.get("bestAvailability", {}).get("availabilityFlag")
            == "Y",
        }
        for product in data["products"]
    ]


class ExclusiveBooksSearchSpider(scrapy.Spider):
    name = "exclusive-books"

    def __init__(self, isbn: str, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.start_urls = [get_search_url_for_isbn(isbn)]

    def parse(self, response):
        for script in response.css(JS_SELECTOR):
            body = script.get()
            matches = re.findall(JSON_PATTERN, body)
            if matches:
                data = json.loads(matches[0])
                for product in transform_data(data):
                    yield product
        #
        # next_page = response.css('li.next a::attr("href")').get()
        # if next_page is not None:
        #     yield response.follow(next_page, self.parse)
