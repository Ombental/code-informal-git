from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options

import time


def get_likers_div(username: str, user_password: str, url: str):
    options = Options()
    options.headless = False
    browser = webdriver.Firefox(options=options)
    browser.get(url)
    try:
        element_present = EC.presence_of_element_located((By.NAME, 'email'))
        email = WebDriverWait(browser, 5).until(element_present)
    except TimeoutException:
        print("Timed out waiting for page to load")
    finally:
        password = browser.find_element_by_name("pass")
        email.send_keys(username)
        password.send_keys(user_password)
        password.submit()


        try:
            logged_in = EC.presence_of_element_located((By.XPATH, '//span[@class="a8c37x1j ni8dbmo4 stjgntxs l9j0dhe7 ltmttdrg g0qnabr5"]'))
            element_present = EC.presence_of_element_located((By.XPATH, '//span[@class="gpro0wi8 pcp91wgn"]'))
            WebDriverWait(browser, 10).until(logged_in)
            likes_link = WebDriverWait(browser, 10).until(element_present)

        except TimeoutException:
            print("Timed out waiting for page to load")

        finally:
            time.sleep(5)
            likes_link.click()

            try:
                element_present = EC.presence_of_element_located((By.XPATH, '//div[@class="q5bimw55 rpm2j7zs k7i0oixp gvuykj2m j83agx80 cbu4d94t ni8dbmo4 eg9m0zos l9j0dhe7 du4w35lb ofs802cu pohlnb88 dkue75c7 mb9wzai9 l56l04vs r57mb794 kh7kg01d c3g1iek1 otl40fxz cxgpxx05 rz4wbd8a sj5x9vvc a8nywdso"]'))
                likers_div = WebDriverWait(browser, 10).until(element_present)
                return likers_div.get_attribute('innerHTML')

            except TimeoutException:
                print("Timed out waiting for page to load")



get_likers_div("noalfig6@gmail.com","a4b3c2d1","https://www.facebook.com/afula.live/photos/pcb.4032054813581135/4032054610247822/")
