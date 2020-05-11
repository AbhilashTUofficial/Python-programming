from selenium import webdriver
import time
enterLastName=['four','five']
i=0
driver=webdriver.Chrome()
driver.get('https://accounts.google.com/signup/v2/webcreateaccount?flowName=GlifWebSignIn&flowEntry=SignUp')
time.sleep(1)
firstName=driver.find_element_by_xpath('//*[@id="firstName"]')
firstName.send_keys('abhilash')
lastName=driver.find_element_by_xpath('//*[@id="lastName"]')
lastName.send_keys(enterLastName[i])
enterUsername=driver.find_element_by_xpath('//*[@id="username"]')
enterUsername.send_keys('abhilash'+enterLastName[i])
enterPassword=driver.find_element_by_xpath('//*[@id="passwd"]/div[1]/div/div[1]/input')
enterPassword.send_keys('zv51yf30bj')
confirmPassword=driver.find_element_by_xpath('//*[@id="confirm-passwd"]/div[1]/div/div[1]/input')
confirmPassword.send_keys('zv51yf30bj\n')
clickNext=driver.find_element_by_xpath('//*[@id="accountDetailsNext"]/div[2]')
clickNext.click()
