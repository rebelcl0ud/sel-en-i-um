from selenium import webdriver

chrome_browser = webdriver.Chrome("C:/Windows/chromedriver")

# chrome_browser.maximize_window()
chrome_browser.get('https://www.seleniumeasy.com/test/basic-first-form-demo.html')

assert "Selenium Easy Demo" in chrome_browser.title

# other ways to snag elements
button = chrome_browser.find_element_by_class_name('btn-default').get_attribute('innerHTML')
button2 = chrome_browser.find_element_by_css_selector('.btn')
# print(button2)

assert "Show Message" in chrome_browser.page_source

user_message = chrome_browser.find_element_by_id("user-message")
user_message.clear()
user_message.send_keys('hebwoooo')
submit_show_message_button = chrome_browser.find_element_by_class_name('btn-default')
submit_show_message_button.click()
output_message = chrome_browser.find_element_by_id('display')
assert output_message

# will close window, if you use .quit() it will quit driver
chrome_browser.close()
