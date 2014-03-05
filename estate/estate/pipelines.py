# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/topics/item-pipeline.html

from scrapy.mail import MailSender
import re, json

class EstatePipeline(object):
    def __init__(self):
        self.message = ''
        self.target_list = []

    def close_spider(self, spider):
        potential = ''
        for i in self.target_list:
            potential = potential + "\n"
            for j in i.keys():
                potential = potential + "\n" + str(j) + ": " + str(i[j])

        MailSender(mailfrom="necro_john@hotmail.com").send(to=["john.phi85@gmail.com"], subject=spider.name, body=potential)

    def process_item(self, item, spider):
        self.target_list.append(item)
        bain_place = re.search('bain', item['address'], re.I) # match case insensitive to bain street place
        if bain_place:
            for field in item.keys():
                self.message = self.message + "\n" + field + ": " + item[field]

            unavailable = re.search('1231397', item['url'])
            if not unavailable:
                MailSender(mailfrom="necro_john@hotmail.com").send(to=["arifin@gmail.com", "john.phi85@gmail.com"], subject=item['name'], body=self.message)
        return item
