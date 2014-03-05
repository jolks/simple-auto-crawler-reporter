# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html

from scrapy.item import Item, Field

class EstateItem(Item):
    # define the fields for your item here like:
    url = Field()
    name = Field()
    address = Field()
    price = Field()
    furnished = Field()
    bedroom = Field()
    bathroom = Field()
