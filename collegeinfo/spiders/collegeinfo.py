from scrapy.spiders import Spider
#from scrapy.selector import Selector
import types
from collegeinfo.items import CollegeinfoItem
import scrapy


class collegeinfo(Spider):
    name = "collegeinfo"
    allowed_domains = ["ysu.edu.cn"]
    start_urls = [
       "http://mec.ysu.edu.cn/syscontent_show.aspx?cid=39"
    ]
   
    def parse(self, response):
        #urls=response.xpath('//table[@class="fortable_14"][2]/tbody/tr/td[4]/a/@href').extract()
        print(type(response))
        urls=response.xpath('//table[@class="fortable_14"][2]/tbody/tr').extract()
        for i  in range(len(urls)-1):
            item=CollegeinfoItem()
            item["researchdirection"]=str(response.xpath('//table[@class="fortable_14"][2]/tbody/tr['+str(i+2)+']/td[2]/text()').extract()[0]).strip()
            url=response.xpath('//table[@class="fortable_14"][2]/tbody/tr['+str(i+2)+']/td[4]/a/@href').extract()
            url4="http://mec.ysu.edu.cn/"+url[0]
            yield scrapy.Request(url4,meta={'item':item},callback=self.parse_detail)
    def parse_detail(self,response):
        item=response.meta["item"]
        urls1=response.xpath('//table[@id="dd"]/tr/td[7]/a/@href').extract()
        for url1 in urls1:
            rurl1="http://mec.ysu.edu.cn/mdt/"+url1
            yield scrapy.Request(rurl1,meta={'item':item},callback=self.parse_item)
        #nextpage=response.xpath('//*[@id="Ap1"]/a').extract()
        #print(nextpage[-2])
        #if nextpage is not None:
           # self.logging.info("下一夜不是空的")
            #next_page = response.urljoin(nextpage)
            #yield scrapy.Request(next_page,meta={'item':item},callback=self.parse_detail)
    def parse_item(self,response):
        item=response.meta["item"]
        item["name"]=response.xpath('//table[@class="tablestyle"]/tr[1]/td[1]/span/text()').extract()
        item["email"]=response.xpath('//table[@class="tablestyle"]/tr[6]/td[2]/span/text()').extract()
        item["college"]=response.xpath('//table[@class="tablestyle"]/tr[1]/td[2]/span/text()').extract()
        item["jobtitle"]=response.xpath('//table[@class="tablestyle"]/tr[3]/td[2]/span/text()').extract()
        if response.xpath('//table[@class="tablestyle"]/tr[3]/td[1]/span/text()').extract():
            item["age"]=2017-int(response.xpath('//table[@class="tablestyle"]/tr[3]/td[1]/span/text()').extract()[0].split('-')[0])
        yield item
    
        

