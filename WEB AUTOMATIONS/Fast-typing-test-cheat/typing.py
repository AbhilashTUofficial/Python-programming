import selenium
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

driver = webdriver.Chrome()
driver.get("https://10fastfingers.com/")


def logIn():
    try:
        logIn = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//*[@id=\"bs-example-navbar-collapse-1\"]/ul[4]/li[2]/a"))
        )
        logIn.click()


    except:
        print("the log in button is not found")



    try:
        google = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, "//*[@id=\"login-btns\"]/ul/li[3]/a"))
        )
        google.click()
    except:
        print("the google box is not found")




    try:
        emailBox = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, "//*[@id=\"identifierId\"]"))
        )
        emailBox.send_keys("abhilashstorm@gmail.com\n")


    except:
        print("error in email box")

    #
    time.sleep(10)
    try:

        nextButton = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, "//*[@id=\"passwordNext\"]/span/span"))
        )
        nextButton.click()
    except:
        print("button not found")


def Typing():
    try:
        inputBox = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, "//*[@id=\"inputfield\"]"))
        )
    except:
        print("the input box not found")

    try:
        for i in range(400):
            word = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.CLASS_NAME, "highlight"))
            )
            inputBox.send_keys(word.text)
            inputBox.send_keys(" ")
            print(word.text)
            time.sleep(0.25)
    except:
        # refresh
        try:
            refreshBotton = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.XPATH, "//*[@id=\"reload-btn\"]"))
            )
        except:
            print("the refresh button is not found")


def navigation():
    try:
        start = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//*[@id=\"sidebar\"]/div/a[2]"))
        )
        start.click()
    except:
        print("the button is not found")


def main():
    navigation()
    logIn()
    navigation()
    Typing()



main()
