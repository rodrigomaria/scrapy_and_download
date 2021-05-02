# import packages
import csv
from time import sleep

from selenium import webdriver

# constants
ADDRESS = "https://www.flickr.com/search/?text=food"
CSV_NAME = "urls.csv"
CHROME_DRIVER_PATH = "./chromedriver_linux64/chromedriver"

# file csv
writer = csv.writer(open(CSV_NAME, "w", encoding="utf-8"))
writer.writerow(["URLS"])

# chrome driver
options = webdriver.ChromeOptions()
options.add_argument("--headless")
driver = webdriver.Chrome(CHROME_DRIVER_PATH, options=options)
driver.maximize_window()

# access site
driver.get(ADDRESS)
sleep(1)

# access photos and extract each url
all_photos = driver.find_elements_by_xpath(
    '//div[@class="view photo-list-photo-view requiredToShowOnServer awake"]'
)
url_list = [url.get_attribute("style") for url in all_photos]

# write each url in csv
for url in url_list:
    final_url = url.split()[-1]
    final_url = f"https://{final_url[7:-3]}"
    writer.writerow([final_url])

# quit Chrome driver
driver.quit()
