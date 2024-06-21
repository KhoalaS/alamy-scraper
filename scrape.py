from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import re
import random

options = webdriver.ChromeOptions()
options.add_argument("--headless=new")
# driver = webdriver.Chrome(options=options)
driver = webdriver.Chrome()

try:
    driver.get(
        "https://www.alamy.com/stock-photo/?name=H.+ARMSTRONG+ROBERTS&pseudoid=CEA9A46E-33B4-4443-8B6A-26377F61F632&sortBy=relevant")
    time.sleep(8)
    accept = driver.find_element(
        by=By.CSS_SELECTOR, value="button[data-tid='banner-accept']")
    accept.click()

    for i in range(1, 183):
        gallery = driver.find_element(
            by=By.CSS_SELECTOR, value=".image-gallery > div > div > div > div > div")
        groups = gallery.find_elements(by=By.CLASS_NAME, value="group")
        
        images = []

        for group in groups:
            id = ""
            try:
                strong = group.find_element(by=By.TAG_NAME, value="strong")
                id = strong.get_attribute("innerText")
            except:
                continue

            name = group.find_element(
                by=By.CSS_SELECTOR, value="span[itemprop='name']").get_attribute("innerText")
            licenseUrl = group.find_element(
                by=By.CSS_SELECTOR, value="span[itemprop='acquireLicensePage']").get_attribute("innerText")
            r = re.compile("searchId=(\w+)")
            matches = r.findall(licenseUrl)


            if len(matches) > 0:
                searchId = matches[0]
                img = "https://c7.alamy.com/zooms/15/{}/{}.jpg|{}".format(
                    searchId, id.lower(), name)
                images.append(img)

        print(len(images))
        
        out = open("images.txt", "a")
        for img in images:
            out.write(img + "\n")

        nextButton = driver.find_element(
            by=By.CSS_SELECTOR, value="nav > a[data-testid='next']")
        nextButton.click()

        time.sleep(5+random.randint(0,3))


finally:
    driver.quit()
