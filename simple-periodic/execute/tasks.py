from __future__ import absolute_import

from execute.celery import celery
import sh

@celery.task
def crawl(path, target):
    sh.cd(path)
    sh.scrapy('crawl', target)

