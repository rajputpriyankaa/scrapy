# scrapy
Web scraping with Scrapy

# For starting the project, use command:
scrapy startproject <ProjectName>
Ex: scrapy startproject scrapingcourse

# Go to the created directory
cd scrapingcourse

# Generate a spider file
scrapy genspider scraper <URL>
Ex: scrapy genspider scraper https://www.scrapingcourse.com/ecommerce/ 
It will create the scraper.py under spiders folder

# To run the scraper:
scrapy crawl scraper

# To output the data in json file:
scrapy crawl scraper -o json 

# To output the data in csv file:
scrapy crawl scraper -o scraper.csv
