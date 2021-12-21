# How to setup Scrapy in a virtual env

mkdir FOLDER
cd FOLDER 

python3 -m venv env
source env/bin/activate
pip install scrapy
scrapy startproject PROJECT_NAME
cd PROJECT_NAME
tree # view composition

scrapy shell
fetch('url') # make sure there's 200 response


fetch('https://www.ebay.com/sch/i.html?_from=R40&_trksid=m570.l1313&_nkw=computers&_sacat=0&LH_TitleDesc=0&_oac=1')

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


# run spyder
scrapy crawl ebay -O ebay.json