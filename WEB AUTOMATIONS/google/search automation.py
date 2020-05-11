from selenium import webdriver
import time


driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://google.com")
searchbox = driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[1]/div/div[2]/input')
searchbox.send_keys('THIS BROWSER IS AUTOMATED BY ABHILASH TU ')
time.sleep(1)
searchbutton = driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[3]/center/input[1]')
searchbutton.click()
searchmessage = driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[2]/div/div[2]/input')
searchmessage.clear()
searchmessage.send_keys('I can make all sort of web based boring things exciting ')
time.sleep(2)
searchmessage.clear()
searchmessage.send_keys('For example ')
time.sleep(.5)

searchmessage.clear()
searchmessage.send_keys('login in the Gmail account ')
time.sleep(1)

searchmessage.clear()
searchmessage.send_keys('login in facebook account ')
time.sleep(1)

searchmessage.clear()
searchmessage.send_keys('the list go on!')
time.sleep(1)

searchmessage.clear()
searchmessage.send_keys('Not just login in and login out ')
time.sleep(1)

searchmessage.clear()
searchmessage.send_keys('Now i can automate all my daily web activities ')
time.sleep(2)

searchmessage.clear()
searchmessage.send_keys('it is fun and i can save lot of my time! ')
time.sleep(1.5)

searchmessage.clear()
searchmessage.send_keys('I can show you an example')
time.sleep(1)

searchmessage.clear()
searchmessage.send_keys('login in gmail each and every time you entered on the browser is boring ')
time.sleep(1)

searchmessage.clear()
searchmessage.send_keys('and also waste a lot of time ')
time.sleep(1)

searchmessage.clear()
searchmessage.send_keys('So let me show you how is done!')
time.sleep(1)

searchmessage.clear()
searchmessage.send_keys('gmail login \n')
gmail_login = driver.find_element_by_xpath('//*[@id="rso"]/div[1]/div/div[1]/a/div/cite')
gmail_login.click()
driver.get(
    "https://accounts.google.com/signin/v2/identifier?continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&service=mail&sacu=1&rip=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin")
driver.find_element_by_name("identifier").send_keys('abhilashstorm@gmail.com')
time.sleep(1)

driver.get("https://google.com")
searchbox2 = driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[1]/div/div[2]/input')
time.sleep(.5)

searchbox2.send_keys('Automation is faster ')
time.sleep(.5)

searchbox2.clear()
searchbox2.send_keys('Efficient ')
time.sleep(.5)

searchbox2.clear()
searchbox2.send_keys('And awesome!')
time.sleep(10)
