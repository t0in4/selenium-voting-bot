# -*- coding:utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.proxy import *
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager
import time
from random import randrange



def proxy():
    with open("data.txt","r") as file:
    # data.txt proxies written like that 120.0.0.1:8080
        
        for _ in file:
            z = _[:-1].split(':') #deleting new line sybmol after split the proxy address ["120.0.0.1","8080\n"]
            profile = webdriver.FirefoxProfile()
            profile.set_preference("network.proxy.type",1)
            profile.set_preference("network.proxy.http",z[0])
            profile.set_preference("network.proxy.http_port",int(z[1]))
            profile.set_preference("network.proxy.ssl",z[0])
            profile.set_preference("network.proxy.ssl_port",int(z[1]))
            profile.update_preferences()
            options = Options()
            options.headless = False # you can change it to True if you launch bot on the server
            driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(),options=options,firefox_profile=profile)
            
            try:
                driver.get("http://voting")
                print("Headless " + _ + " initialized")
                driver.find_element_by_id("vote-325").click()
                if driver.find_element_by_id("vote-325").get_attribute("type") == "checkbox":
                    print("Element is a checkbox")
                else:
                    print("Element is not a checkbox")
                isChecked = driver.find_element_by_id("vote-325").get_attribute("checked")
                if isChecked is not None:
                    print("Element checked - ", isChecked)
                else:
                    print("Element checked - false")
                NEXT_BUTTON_XPATH = '//button[@alt="vote"]'# find vote button
                button = driver.find_element_by_xpath(NEXT_BUTTON_XPATH)
                button.click()
                print("Button clicked in try block")
            except Exception: # usually it is timeout exception, bcz proxies are slow and probably down
                time.sleep(randrange(180))
                print("Button not clicked")
                print("deleting " + _)
                
                deleting()
def deleting(): #deleting used proxies from data.txt
    with open("data.txt","r") as fin:
        data = fin.read().splitlines(True)
    with open("data.txt","w") as fout:
        fout.writelines(data[1:])
    time.sleep(randrange(180)) # making bot work slightly random
    proxy()
    
proxy()
