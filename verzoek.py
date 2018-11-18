import time
import string
from selenium import webdriver
import random
from selenium.webdriver.common.keys import Keys

base_url = 'https://live.ntr.nl/nvdp/#/info/29ff494bd01a4d08c275ed40e3003ad5'
elem_class = 'btn btn-alt ng-scope'

def random_name(size=8, chars=string.ascii_lowercase + string.digits):
    random.seed()
    name = ''.join(random.choice(chars) for _ in range(size))
    email = name + '@gmail.com'
    text = """
    
    Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.
    
    """
    return name, email, text


x = 0
while x < 1000:

    # options = webdriver.ChromeOptions()
    # options.add_argument('headless')
    # driver = webdriver.Chrome(chrome_options=options)

    driver = webdriver.Chrome()
    driver.get(base_url)
    time.sleep(1)
    driver.find_element_by_xpath('//div[contains(text(), "Overslaan")]').click()
    time.sleep(0.2)
    driver.find_element_by_xpath('//div[contains(text(), "Doorgaan")]').click()

    name, email, text = random_name()

    # elem_class = "input ng-scope ng-pristine ng-valid-maxlength ng-valid-minlength ng-invalid ng-invalid-required"
    # name_field = driver.find_element_by_class_name(elem_class)
    name_field = driver.find_element_by_xpath(
        '//*[contains(@class, "input ng-scope ng-pristine ng-valid-maxlength ng-valid-minlength ng-invalid ng-invalid-required")]')
    name_field.send_keys(name)
    name_field.send_keys(Keys.ENTER)

    elem_class = 'input ng-scope ng-pristine ng-valid-email ng-valid-maxlength ng-valid-minlength ng-invalid ng-invalid-required'

    driver.find_element_by_xpath(
        '//*[contains(@class, "input ng-scope ng-pristine ng-valid-maxlength ng-valid-minlength ng-invalid ng-invalid-required")]')


    field = driver.find_element_by_class_name(elem_class)
    field.send_keys(email)
    field.send_keys(Keys.ENTER)


    # Check even welke je wilt (1 of 2, geen 0 index)
    # el = driver.find_element_by_xpath('//span[contains(text(), "Stemmen")][1]')
    #
    # driver.execute_script("arguments[0].click();", el)
    # driver.delete_all_cookies()
    driver.close()
    x += 1
    print('POST {}'.format(x))
