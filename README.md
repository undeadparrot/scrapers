# scrapers
Scrapers for various things (some South African), some using Scrapy

![Python package](https://github.com/undeadparrot/scrapers/workflows/Python%20package/badge.svg)
[![PyPI version](https://badge.fury.io/py/shanes-scrapers.svg)](https://badge.fury.io/py/shanes-scrapers)

- These are *not* for crawling an entire catalogue or even many pages. 
- The intended usage is to check details for some specific products
 - for example, if I'm shopping for a book and want to compare offers
 - *obviously Takealot is probably best, so maybe you don't even need this?* 

## How to Scrapy?



## What is useful information to scrape?

- GTIN (Barcode or ISBN)
- Title
- Description? Author? maybe.
- Cover image
- Price
- Availability (in stock? leadtime?)

## On ISBNs

### When searching

Sites do not seem to have consistent ways of dealing with ISBNs. 
For example, our test book *The Italian Duke's Wife* by Penny Jordan, has these ISBNs on Amazon:
 - 0373125291 (ISBN-10)
 - 978-0373125296 (ISBN-13)
 
If I search for `0373125291` (ISBN-10) or `0373125296` (ISBN-13 without prefix) on Exclusive Books I get over 1,437,946 results, the first page
consisting primarily of books with numerical titles like *491 Days* and *1795*.

If I search for `978-0373125296` I get `The Diplomas of King Aethlred 'the Unready' 978-1016`
and 24 other books, none of which were penned by Penny Jordan.

If I search for `9780373125296` (by removing the dash) there is only one result: [The Italian DUke's Wife](https://www.exclusivebooks.co.za/product/9780373125296) . 

So we will need to transform ISBNs for searching.

### On Converting Between -10 and -13

> An ISBN-10 is converted to ISBN-13 by prepending "978" to the ISBN-10 and recalculating the final checksum digit using the ISBN-13 algorithm. The reverse process can also be performed, but not for numbers commencing with a prefix other than 978, which have no 10-digit equivalent.

This would explain why `0373125291` and `978-0373125296` differ in the last digit (1 vs 6).
 
### Structure of an ISBN

For ISBN-13 the prefix is always either `978` or `979`, which is a 
[GS1 Country Code](https://en.wikipedia.org/wiki/List_of_GS1_country_codes). 
In the case of books, the country code 978 refers to *Bookland*, and 979 was only for sheetmusic,
but now includes general books as well.

The last digit is a checksum.

Following these discoveries, the unique data in `978-0373125296` is actually just `037312529`.

![Labelled ISBN diagram from Wikipedia](https://upload.wikimedia.org/wikipedia/commons/thumb/8/84/ISBN_Details.svg/220px-ISBN_Details.svg.png)

### ISBN Suffixes

Takealot seems to have an additional suffix added onto their ISBNs for ebooks, 
such as `-002` or `-003` in the ISBNs 
[9781426842191-003](https://www.takealot.com/the-italian-duke-s-wife-ebook/PLID53640924/product-information) 
and 
[9784596647016-002](https://www.takealot.com/italian-duke-s-wife-ebook/PLID68442655/product-information) 
for various eBook editions of our romance novel.  

Presumably this is following some standard (Takealot does not issue ISBNs), but Googling does
not reveal how it works. According to [some publisher's guide to DOIs](http://www.wiki.degruyter.de/production/files/dg_variables_and_id.xhtml#doi-suffix-book-parts)
there can be a chapter suffix on a barcode like `-002` to indicate chapter 2,
and that certain publishing partnerships may include a suffix. 

Hitting an ISBN search like https://isbnsearch.org/search?s=9781426842191-002 does not match the
book, and seems to treat it as not being a proper ISBN (the URL changes from a direct ISBN lookup to a 
text search).

*I don't think this tool is even intended for finding eBooks, so this can be ignored.*
 
## Scrapers

![Exclusive Books](./shanes_scrapers/exclusive_books/__init__.py)

## Other Sites To Investigate

- [Takealot](https://www.takealot.com/)
- [Raru](https://www.raru.co.za/)
- [Loot](https://www.loot.co.za/)
