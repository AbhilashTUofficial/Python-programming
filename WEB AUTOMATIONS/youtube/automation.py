from selenium import webdriver
import time
driver=webdriver.Chrome()
driver.get('https://www.google.com')
searchbox=driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[1]/div/div[2]/input')
searchbox.send_keys('youtube\n')
youtube_entry=driver.find_element_by_xpath('//*[@id="rso"]/div[1]/div/div/div[1]/a/div/cite')
youtube_entry.click()
youtube_search=driver.find_element_by_name('search_query')
youtube_search.send_keys('abhilash tu\n')
my_channel=driver.get('https://www.youtube.com/channel/UC8iP2LKB-V1g2jMTbe6Pb4Q')
driver.get('https://www.youtube.com/watch?v=SefRhmyjJD8')

