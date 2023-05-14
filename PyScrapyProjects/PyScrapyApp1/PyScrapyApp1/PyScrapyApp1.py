# current working directory is E:\PythonVSprojects\PyScrapyProjects\PyScrapyApp1\PyScrapyApp1
import scrapy
import subprocess
# import threading
import time
import os

from scrapy.crawler import CrawlerProcess

## Using os module:

# get the current working directory
current_working_directory = os.getcwd()
# print output to the console E:\PythonVSprojects\PyScrapyProjects\PyScrapyApp1\PyScrapyApp1
current_working_directory
print(current_working_directory)
## Using pathlib module:


if __name__ == "__main__": # This is to prevent errors when running with multiprocessing on Windows

# Open your terminal and activate your virtual environment with the command -E:\PythonVSprojects\PythonProjectsAllVirtualEnvironments\PyScrapyProjectsVenvs\PyScProApp1Venv\Scripts\activate.bat
 cmd = ['E:\PythonVSprojects\PythonProjectsAllVirtualEnvironments\PyScrapyProjectsVenvs\PyScProApp1Venv\Scripts\activate.bat']
 subprocess.run(cmd, shell=True)

 ## Using pathlib module:
from pathlib import Path
# get the current working directory
current_working_directory = Path.cwd()
# print output to the console
print(current_working_directory)

    # create new Scrapy project
    # Run the command  !scrapy startproject PyScrapyApp1ActiveProject
subprocess.run(["E:\PythonVSprojects\PythonProjectsAllVirtualEnvironments\PyScrapyProjectsVenvs\PyScProApp1Venv\Scripts\activate.bat", "&&", "scrapy", "startproject", "PyScrapyApp1ActiveProject"], shell=True)
    # generate new spider
    #!scrapy genspider SPDFinancial_spider https://www.valueresearchonline.com/stocks/41149/asian-paints-ltd#key-ratios,https://www.valueresearchonline.com/stocks/41149/asian-paints-ltd#peers,https://www.valueresearchonline.com/stocks/41149/asian-paints-ltd#financials,https://www.valueresearchonline.com/stocks/41149/asian-paints-ltd#overview,https://www.valueresearchonline.com/stocks/41149/asian-paints-ltd#ownership,https://www.valueresearchonline.com/stocks/41149/asian-paints-ltd#other-details

urls = [
    'https://www.valueresearchonline.com/stocks/41149/asian-paints-ltd#key-ratios',
    'https://www.valueresearchonline.com/stocks/41149/asian-paints-ltd#peers',
    'https://www.valueresearchonline.com/stocks/41149/asian-paints-ltd#financials',
    'https://www.valueresearchonline.com/stocks/41149/asian-paints-ltd#overview',
    'https://www.valueresearchonline.com/stocks/41149/asian-paints-ltd#ownership',
    'https://www.valueresearchonline.com/stocks/41149/asian-paints-ltd#other-details'
]

for url in urls:

     cmd = ["E:\PythonVSprojects\PythonProjectsAllVirtualEnvironments\PyScrapyProjectsVenvs\PyScProApp1Venv\Scripts\activate.bat", "&&", 'scrapy', 'genspider', 'SPDFinancial_spider', url]
     subprocess.run(cmd, shell=True)

## Using os module:

# get the current working directory
current_working_directory = os.getcwd()
current_working_directory
print(current_working_directory)

# Py Code for Waiting untill the scrapy project is created,wait for say 20 seconds, not suspending or stopping any thread current or previous other thread.

def wait_for_process(process, timeout):
    """Wait for a process to finish or raise an error after timeout."""
    start = time.time()
    while time.time() - start < timeout:
        if not process.is_alive():
            return
        time.sleep(20)
    raise RuntimeError("Process timed out")

def run_process(process):
    """Run a process and wait for it to finish or raise an error after timeout."""
    process.start()
    wait_for_process(process, 60)

# Navigate to the project directory: cd PyScrapyApp1ActiveProject
cmd = ["E:\PythonVSprojects\PythonProjectsAllVirtualEnvironments\PyScrapyProjectsVenvs\PyScProApp1Venv\Scripts\activate.bat", "&&", 'cd', 'PyScrapyApp1ActiveProject']
subprocess.run(cmd, shell=True)  

# Run the spider: scrapy crawl Financial_spider 
# Run the command to generate a new spider:- scrapy genspider Financial_spider www.valueresearchonline.com,www.valueresearchonline.com/stocks/41149/asian-paints-ltd#key-ratios,www.valueresearchonline.com/stocks/41149/asian-paints-ltd#peers,www.valueresearchonline.com/stocks/41149/asian-paints-ltd#financials,www.valueresearchonline.com/stocks/41149/asian-paints-ltd#overview,www.valueresearchonline.com/stocks/41149/asian-paints-ltd#ownership,www.valueresearchonline.com/stocks/41149/asian-paints-ltd#other-details
cmd = ["E:\PythonVSprojects\PythonProjectsAllVirtualEnvironments\PyScrapyProjectsVenvs\PyScProApp1Venv\Scripts\activate.bat", "&&", 'scrapy', 'genspider', 'SPDFinancial_spider', 'www.valueresearchonline.com','www.valueresearchonline.com/stocks/41149/asian-paints-ltd#key-ratios','www.valueresearchonline.com/stocks/41149/asian-paints-ltd#peers','www.valueresearchonline.com/stocks/41149/asian-paints-ltd#financials','www.valueresearchonline.com/stocks/41149/asian-paints-ltd#overview','www.valueresearchonline.com/stocks/41149/asian-paints-ltd#ownership','www.valueresearchonline.com/stocks/41149/asian-paints-ltd#other-details']
subprocess.run(cmd, shell=True)

# Write a Py code to  Locate the spider file Financial_spider.py located in the spiders directory whos relative path is \spiders\Financial_spider.py' inside of PyScrapyApp1ActiveProject project and Replace/Overwrite the code you previously written in the Financial_spider.py spider file with the Py code below

#def parse(self, response):
#        # extract data here using scrapy selectors
#        data = {}

        
#        data['basic_eps'] = response.xpath("//li[contains(., 'Basic EPS')]/span/text()").get()
#        data['book_value'] = response.xpath("//li[contains(., 'Book Value')]/span/text()").get()
#        data['dividend'] = response.xpath("//li[contains(., 'Dividend')]/span/text()").get()
#        data['revenue'] = response.xpath("//li[contains(., 'Revenue')]/span/text()").get()
#        data['pbdit'] = response.xpath("//li[contains(., 'PBDIT')]/span/text()").get()
#        data['net_profit'] = response.xpath("//li[contains(., 'Net Profit')]/span/text()").get()
#        data['pbdit_margin'] = response.xpath("//li[contains(., 'PBDIT Margin')]/span/text()").get()
#        data['net_profit_margin'] = response.xpath("//li[contains(., 'Net Profit Margin')]/span/text()").get()
#        data['debt_equity'] = response.xpath("//li[contains(., 'Total Debt')]/span/text()").get()
#        data['current_ratio'] = response.xpath("//li[contains(., 'Current Ratio')]/span/text()").get()
#        data['dividend_payout_ratio'] = response.xpath("//li[contains(., 'Dividend Payout Ratio')]/span/text()").get()
#        data['earnings_retention_ratio'] = response.xpath("//li[contains(., 'Earnings Retention Ratio')]/span/text()").get()

#        yield data

# Define the relative path to the Financial_spider.py file
rel_path = "spiders/Financial_spider.py"

# Get the absolute path to the project directory
proj_path = os.path.abspath("PyScrapyApp1ActiveProject")

# Combine the project path and relative path to get the full path to the spider file
file_path = os.path.join(proj_path, rel_path)

# Open the spider file for writing
with open(file_path, "w") as file:
    # Overwrite the spider file with the new code
    file.write("""import scrapy
                  from scrapy.crawler import CrawlerProcess
class FinancialSpider(scrapy.Spider):
    name = "financial"

    def start_requests(self):
        urls = ["https://www.moneycontrol.com/financials/tataconsultancyservices-ratiosVI/tcs",
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
        yield data""")

# Py code for autopep8 --in-place --aggressive --aggressive <path_to_Financial_spider.py>   you should replace <path_to_Financial_spider.py> with the actual path to your Financial_spider.py file

# Define the relative path to the Financial_spider.py file
rel_path = "spiders/Financial_spider.py"
# Py code for autopep8 --in-place --aggressive --aggressive <rel_path = "spiders/Financial_spider.py"> 
cmd = [ "E:\PythonVSprojects\PythonProjectsAllVirtualEnvironments\PyScrapyProjectsVenvs\PyScProApp1Venv\Scripts\activate.bat", "&&", f"autopep8 --in-place --aggressive --aggressive {rel_path}"]
subprocess.run(cmd, shell=True)



# Print a confirmation message
print(f"{file_path} saved successfully.")

# run spider and save data to JSON file

    ## run spider and save data to JSON file
    #process = CrawlerProcess()
    #process.crawl(FinancialSpider)
    #process.start(output_file="financial_data.json")

    # run spider and save data to JSON file

process = CrawlerProcess(settings={
    'FEED_FORMAT': 'json',
    'FEED_URI': '.\financial_data.json'
})



process.crawl(FinancialSpider)
process.stop()  # explicitly stop the reactor
process.start()
    # Do other stuff here while the thread is running
# ...
# Wait for the thread to finish
process.join()

    # scrapy genspider example example.com
# scrapy genspider -t crawl example example.com
 # scrapy genspider -l
# scrapy genspider -t crawl example example.com


# run spider and save data to CSV file
    # run spider and save data to CSV file
process = CrawlerProcess(settings={ 'FEED_FORMAT': 'csv', 'FEED_URI': '.\financial_data.csv' })
process.crawl(FinancialSpider)
process.stop()  # explicitly stop the reactor
process.start()
# Do other stuff here while the thread is running
# ...
# Wait for the thread to finish
process.join()
