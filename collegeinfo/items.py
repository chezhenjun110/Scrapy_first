# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CollegeinfoItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    email=scrapy.Field()
    college=scrapy.Field()
    jobtitle=scrapy.Field()
    age=scrapy.Field()
    researchdirection=scrapy.Field()


