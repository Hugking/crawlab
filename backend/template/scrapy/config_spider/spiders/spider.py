# -*- coding: utf-8 -*-
import scrapy
import re
from config_spider.items import Item
from urllib.parse import urljoin, urlparse

def get_real_url(response, url):
    if re.search(r'^https?', url):
        return url
    elif re.search(r'^\/\/', url):
        u = urlparse(response.url)
        return u.scheme + ":" + url
    return response.urljoin(url)

class ConfigSpider(scrapy.Spider):
    name = 'config_spider'
    source = '###SOURCES###'
    crawler_name = '###CRAWLER_NAME###'

    @classmethod
    def update_settings(cls, settings):
        if settings.get("check_url"):
            # bloomfilter
            settings.setdict(cls.custom_settings or {
                "SCHEDULER": "scrapy_redis_bloomfilter.scheduler.Scheduler",
                "SCHEDULER_DUPEFILTER_KEY":"crawlab_spider:bloomfilter",
                "DUPEFILTER_CLASS":"scrapy_redis_bloomfilter.dupefilter.RFPDupeFilter",
                "DUPEFILTER_DEBUG": True
            }, priority='spider')

    def start_requests(self):
        yield scrapy.Request(url='###START_URL###', callback=self.###START_STAGE###)

###PARSERS###
