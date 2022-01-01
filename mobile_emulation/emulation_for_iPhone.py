from selenium import webdriver


mob = { "deviceName": "your device" }
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("mobileEmulation", mob)
driver = webdriver.Chrome(options=chrome_options)  # execution path

driver.get('https://www...')
