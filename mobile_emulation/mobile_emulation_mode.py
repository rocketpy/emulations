# https://chromedriver.chromium.org/mobile-emulation

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


mob = {
    "deviceMetrics": { "width": 360, "height": 640, "pixelRatio": 3.0 },
    "userAgent": "Mozilla/5.0 (Linux; Android 4.2.1; en-us; Nexus 5 Build/JOP40D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Mobile Safari/535.19" }

chrome_options = Options()
chrome_options.add_experimental_option("mobile_emulation", mob)
driver = webdriver.Chrome(chrome_options=chrome_options)

#  or
from selenium import webdriver


mobile_emulation = { "device_name": "Nexus 5" }
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
driver = webdriver.Remote(command_executor='http://127.0.0.1:4444/wd/hub',
                         desired_capabilities = chrome_options.to_capabilities())

"""
Specifying Individual Device Attributes

It is also possible to enable Mobile Emulation by specifying individual attributes.
To enable Mobile Emulation this way, the “mobileEmulation” dictionary can contain a “deviceMetrics” dictionary and a “userAgent” string.
The following device metrics must be specified in the “deviceMetrics” dictionary:

        “width” - the width in pixels of the device’s screen

        “height” - the height in pixels of the device’s screen

        “pixelRatio” - the device’s pixel ratio

        "touch" - whether to emulate touch events (defaults to true, usually does not need to be set)

The phones and tablets that are available under the Mobile Emulation panel can be found in the:
https://chromium.googlesource.com/chromium/src/+/167a7f5e03f8b9bd297d2663ec35affa0edd5076/third_party/WebKit/Source/devtools/front_end/emulated_devices/module.json
"""
