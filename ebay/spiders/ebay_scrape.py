import scrapy

class EbayWebSpider(scrapy.Spider):
    name = "ebay"
    domain = ["ebay.com"]
    start_urls = ["https://www.ebay.com/sch/i.html?_from=R40&_trksid=m570.l1313&_nkw=computers&_sacat=0&LH_TitleDesc=0&_oac=1"]

    def parse(self, response):
        products = response.xpath('//div/div/ul/li[contains(@class, "s-item" )]')
        for product in products:            
            name = product.xpath('.//*[@class="s-item__title"]//text()').get()
            if name == 'New Listing':
                name = product.xpath('.//*[@class="s-item__title"]//text()').extract()[1]
            
            price = product.xpath('.//*[@class="s-item__price"]//text()').get().replace('$','')
            geo = product.xpath('.//*[@class="s-item__location s-item__itemLocation"]//text()').get().replace('from ','')
            condition_items = product.xpath('.//*[@class="s-item__subtitle"]//text()').get()
            product_url = product.xpath('.//a[@class="s-item__link"]/@href').get()

            try:
                if len(condition_items) == 1:
                    condition = product.xpath('.//*[@class="s-item__subtitle"]//text()').get()
                elif len(condition_items) > 1:
                    condition = product.xpath('.//*[@class="SECONDARY_INFO"]//text()').get()
            except Exception as e:
                print(f"product condition not found - due to {e}")
                condition = 'not found'

            yield {
                'product_name': name,
                'price': price,
                'country': geo,
                'condition': condition,
                'url': product_url
            }

        """adding code for going into next urls"""
        
        # next_page = response.xpath('//*/a[@class="x-pagination__control"][2]/@href').extract_first()

        # if next_page == None or str(next_page).endswith('#'):
        #     self.log("products collected successfully")
        # else:
        #     yield scrapy.Request(next_page, callback=self.parse)
