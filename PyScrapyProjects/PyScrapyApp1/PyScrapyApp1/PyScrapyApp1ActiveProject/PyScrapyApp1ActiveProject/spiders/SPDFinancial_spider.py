import scrapy
from scrapy.crawler import CrawlerProcess
class FinancialSpider(scrapy.Spider):
    name = "SPDFinancial_spider"

    def start_requests(self):
        urls = ["https://www.moneycontrol.com/",
        "https://www.valueresearchonline.com/stocks/41149/asian-paints-ltd#key-ratios", "https://www.valueresearchonline.com/stocks/41149/asian-paints-ltd#peers", "https://www.valueresearchonline.com/stocks/41149/asian-paints-ltd#financials", "https://www.valueresearchonline.com/stocks/41149/asian-paints-ltd#overview", "https://www.valueresearchonline.com/stocks/41149/asian-paints-ltd#ownership", "https://www.valueresearchonline.com/stocks/41149/asian-paints-ltd#other-details"
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

def parse(self, response):
    # extract data here using scrapy selectors
    data = {}
    data['basic_eps'] = response.xpath("//li[contains(., 'Basic EPS')]/span/text()").get()
    data['book_value'] = response.xpath("//li[contains(., 'Book Value')]/span/text()").get()
    data['dividend'] = response.xpath("//li[contains(., 'Dividend')]/span/text()").get()
    data['revenue'] = response.xpath("//li[contains(., 'Revenue')]/span/text()").get()
    data['pbdit'] = response.xpath("//li[contains(., 'PBDIT')]/span/text()").get()
    data['net_profit'] = response.xpath("//li[contains(., 'Net Profit')]/span/text()").get()
    data['pbdit_margin'] = response.xpath("//li[contains(., 'PBDIT Margin')]/span/text()").get()
    data['net_profit_margin'] = response.xpath("//li[contains(., 'Net Profit Margin')]/span/text()").get()
    data['debt_equity'] = response.xpath("//li[contains(., 'Total Debt')]/span/text()").get()
    data['current_ratio'] = response.xpath("//li[contains(., 'Current Ratio')]/span/text()").get()
    data['dividend_payout_ratio'] = response.xpath("//li[contains(., 'Dividend Payout Ratio')]/span/text()").get()
    data['earnings_retention_ratio'] = response.xpath("//li[contains(., 'Earnings Retention Ratio')]/span/text()").get()
    data['market_cap'] = response.xpath("//strong[contains(., 'Market cap')]/following-sibling::text()").get().strip()
    data['earnings_ttm'] = response.xpath("//strong[contains(., 'Earnings (TTM)')]/following-sibling::text()").get().strip()
    data['liquidity'] = response.xpath("//strong[contains(., 'Liquidity')]/following-sibling::text()").get().strip()
    data['52_week_range'] = response.xpath("//strong[contains(., '52 Week range')]/following-sibling::text()").get().strip()
    data['face_value'] = response.xpath("//strong[contains(., 'Face value')]/following-sibling::text()").get().strip()
    data['cfo'] = response.xpath("//strong[contains(., 'CFO')]/following-sibling::text()").get().strip()
    data['ebitda'] = response.xpath("//strong[contains(., 'EBITDA')]/following-sibling::text()").get().strip()
    data['net_profit_10y_agg'] = response.xpath("//strong[contains(., 'Net Profit')]/parent::p/following-sibling::p//text()").getall()
    yield data
