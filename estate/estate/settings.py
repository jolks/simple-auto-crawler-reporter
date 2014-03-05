# Scrapy settings for estate project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'estate'

SPIDER_MODULES = ['estate.spiders']
NEWSPIDER_MODULE = 'estate.spiders'

ITEM_PIPELINES = [
    'estate.pipelines.EstatePipeline',
]

# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'jolks (+http://jolks.wordpress.com)'
