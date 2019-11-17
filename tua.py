import time

from selenium import webdriver

base_url = 'https://live.ntr.nl/nvdp/#/d221e0e86edd4ad8d140035f89004697'
elem_class = 'btn btn-alt ng-scope'

x = 0
while x < 1000:
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    driver = webdriver.Chrome(chrome_options=options)
    # driver = webdriver.Chrome()
    driver.get(base_url)
    time.sleep(0.8)
    driver.find_element_by_xpath('//div[contains(text(), "Overslaan")]').click()
    time.sleep(0.2)
    driver.find_element_by_xpath('//div[contains(text(), "Doorgaan")]').click()
    time.sleep(0.1)
    # Check even welke je wilt (1 of 2, geen 0 index)
    el = driver.find_element_by_xpath('//p[contains(text(), "ARTIS-NAME")]/following-sibling::span')
    driver.execute_script("arguments[0].click();", el)
    driver.delete_all_cookies()
    driver.close()
    x += 1
    print('POST {}'.format(x))
