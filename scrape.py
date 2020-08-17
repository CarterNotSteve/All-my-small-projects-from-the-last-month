import requests
import scrapy

class spiderman(scrapy.Spider):
    def __init__(self, names, allowed_domainse, scp):
        name = names
        allowed_domains = allowed_domainse
        start_urls = [
            'http://www.scp-wiki.net/scp-'+scp
        ]

        def parse(self, response):
            self.logger.info('A response from %s arrived', response.url)


yes = spiderman('spiderman',["scp-wiki.net"], "173")
yes.parse()
