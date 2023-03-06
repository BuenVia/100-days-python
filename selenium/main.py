from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# options = Options()
# options.add_experimental_option('detach', True)

# driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()

driver.get("https://www.amazon.co.uk/Cabin-Max-Travel-Luggage-Backpack/dp/B072KKHPGX?th=1")
price = driver.find_element("id", "mbc-price-1")

print(price.text)
print(price.size)

new = driver.find_element(By.xpath('//*[@id="qpe-title-tag_feature_div"]/div'))
print(new)