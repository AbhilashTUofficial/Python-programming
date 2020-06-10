from selenium import webdriver
import time
import javascript

username=['_broken_excalibur_','__','e']
password='password'
driver = webdriver.Chrome()
finish = False
firstTime=True
i=0
while not finish:

    driver.get("https://www.instagram.com/?hl=en")
    time.sleep(2)
    enterUserName = driver.find_element_by_xpath(
        '//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[2]/div/label/input')
    enterUserName.send_keys(username[i])
    enterPassword = driver.find_element_by_xpath(
        '//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[3]/div/label/input')
    enterPassword.send_keys(password)

    logIn = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[4]')
    logIn.click()
    time.sleep(2)
    if firstTime:
        exitPopup = driver.find_element_by_xpath('/html/body/div[4]/div/div/div[3]/button[2]')
        exitPopup.click()
    enterProfile = driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[5]/a/img')
    enterProfile.click()

    time.sleep(2)

    """
    
    
    
    enterFolowersLists=driver.find_elements_by_xpath('/html/body/div[4]/div/div[2]')
    driver.execute_script('arguments[0].scrollIntoView()',enterFolowersLists)
    ScrollTime=1
    while True:
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    
    # Wait to load page
    time.sleep(ScrollTime)
    
    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
    break
    last_height = new_height
    
    """
    post = driver.find_element_by_xpath(
        '//*[@id="react-root"]/section/main/div/div[3]/article/div[1]/div/div[1]/div[1]/a/div/div[2]')
    post.click()
    time.sleep(1)
    like = driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[2]/section[1]/span[1]/button')
    like.click()
    time.sleep(1)
    exit = driver.find_element_by_xpath('/html/body/div[4]/div[3]/button')
    exit.click()
    settings = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/div[1]/div/button')
    settings.click()
    time.sleep(1)
    enterProfile = driver.find_element_by_xpath(
        '/html/body/div[4]/div/div/div/button[9]')
    enterProfile.click()
    firstTime=False
    x = i + 1
    i+=1
    if username[x] == username[2]:
        finish = True

time.sleep(3)
