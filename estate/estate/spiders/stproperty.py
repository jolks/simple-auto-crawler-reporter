from scrapy.selector import HtmlXPathSelector
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule
from estate.items import EstateItem

class STPropertySpider(CrawlSpider):
    site_prefix = "http://www.stproperty.sg"
    name = 'stproperty'
    allowed_domains = ['www.stproperty.sg']
    start_urls = [
        'http://www.stproperty.sg/property-for-rent/region/city-south-west-d01-08/max-rent-price-4000/min-bedroom-3',
        'http://www.stproperty.sg/property-for-rent/region/orchard-holland-d09-10/max-rent-price-4000/min-bedroom-3'
        ]

    rules = (
        Rule(SgmlLinkExtractor(allow=r'/page\d+'), follow=True), 
        Rule(SgmlLinkExtractor(allow=(r'www.stproperty.sg/condo-for-rent/')), callback='parse_item', follow=False),
        Rule(SgmlLinkExtractor(allow=(r'www.stproperty.sg/hdb-for-rent/')), callback='parse_item', follow=False),
        Rule(SgmlLinkExtractor(deny=(
            r'/property-for-rent',
            r'/search',
            r'/property-agent'
            )), follow=False),
        )

    def parse_item(self, response):
        hxs = HtmlXPathSelector(response)
        item = EstateItem()

        item['url'] = response.url
        has_name = hxs.select('//h1/a/text()').extract()
        if not has_name:
            item['name'] = ''
        else:
            item['name'] = has_name[0]

        has_price = hxs.select('//div[contains(@class, "ad-main-col1")]/h3/text()').extract()
        if not has_price:
            item['price'] = ''
        else:
            item['price'] = has_price[0].strip()

        #has_address = hxs.select('//div[contains(@class, "ad-main-col1")]/p').re(r'<p>(\.*)>(.+)</a>')
        has_address = hxs.select('//div[contains(@class, "ad-main-col1")]/p').re(r'<p>(.*)<a href=.*>(.+)</a></p>')
        if not has_address:
            item['address'] = ''
        else:
            item['address'] = ' '.join(has_address)

        has_bed_bath = hxs.select('//div[contains(@class, "ad-main-bedbath")]').re(r'<strong>(\d+)</strong>')
        if not has_bed_bath:
            item['bedroom'] = 0
            item['bathroom'] = 0
        else:
            if len(has_bed_bath) > 1:
                item['bedroom'] = has_bed_bath[0]
                item['bathroom'] = has_bed_bath[1]
            else:
                item['bedroom'] = has_bed_bath[0]
                item['bathroom'] = 0

        has_furnished = hxs.select('//ul[contains(@class, "ad-details")]/li').re(r'\s+(.*furnished)</')
        if not has_furnished:
            item['furnished'] = ''
        else:
            item['furnished'] = has_furnished[0]
 
        return item


