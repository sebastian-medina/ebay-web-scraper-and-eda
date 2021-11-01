fetch('https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2380057.m570.l1312&_nkw=rolex')

# full container
response.xpath('//*[@id="srp-river-results"]').get()

# first product in search
response.xpath('//div/div/ul/li[contains(@class, "s-item" )]').get()

# save variable to all items
products = response.xpath('//div/div/ul/li[contains(@class, "s-item" )]')

# get 1st name
# //*[@id="srp-river-results"]/ul/li[1]/div/div[2]/a/h3
# //*[@id="srp-river-results"]/ul/li[2]/div/div[2]/a/h3
products.xpath('.//*[@class="s-item__title"]//text()').get()

# price
products.xpath('.//*[@class="s-item__price"]//text()').get()
