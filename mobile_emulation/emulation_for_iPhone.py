from selenium import webdriver


mob = {"device_name": "your_device"}
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("mobileEmulation", mob)
driver = webdriver.Chrome(options=chrome_options)  # execution path

driver.get('https://www...')

# or

# for iphone [width:375, height:812, pixelRatio:3]
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


mob = {"deviceMetrics": { "width": 375, "height": 812, "pixelRatio": 3.0 },
       "userAgent": "Mozilla/5.0 (Linux; Android 4.2.1; en-us; Nexus 5 Build/JOP40D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Mobile Safari/535.19"
      }
chrome_options = Options()
chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
driver = webdriver.Chrome(executable_path="../chrome/chromedriver85", options=chrome_options)  # execution path
url = "https://www.../"
driver.get(url)

