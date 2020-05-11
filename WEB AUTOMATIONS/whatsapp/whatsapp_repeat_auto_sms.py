from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://web.whatsapp.com/')
input("enter : ")
group = driver.find_element_by_xpath('//*[@id="pane-side"]/div[1]/div/div/div[1]/div/div')
group.click()
for i in range(1000):
    smsbox = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
    smsbox.send_keys("no more nabeel no more emojis \n")
