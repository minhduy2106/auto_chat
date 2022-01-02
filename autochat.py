from selenium import webdriver
from time import sleep
from selenium.webdriver import Keys

#1. khai bao trinh duyet
browser = webdriver.Chrome(executable_path="chromedriver.exe")

#2. Mo thu 1 trang web
browser.get("https://www.messenger.com/")
sleep(5)

#2a. Dien thong tin
txtUser = browser.find_element_by_xpath("/html/body/div/div/div/div[1]/div/div/div/div[1]/div/div[2]/div/div[7]/div[1]/div/div[2]/div[1]/div/form/div/input[6]")
txtUser.send_keys("minhduy.working@gmail.com")

txtPass = browser.find_element_by_xpath("/html/body/div/div/div/div[1]/div/div/div/div[1]/div/div[2]/div/div[7]/div[1]/div/div[2]/div[1]/div/form/div/input[7]")
txtPass.send_keys("duyprocute12")

#2b. Submit form
txtPass.send_keys(Keys.ENTER)
sleep(100)

#2c. Write a messenger
def sendMess():
    send_mess = browser.find_element_by_xpath("/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div[2]/div/form/div/div[3]/div[2]/div[1]/div/div/div[2]/div/div[2]/div/div/div/div")
    send_mess.send_keys("Duy đẹp trai nhất quả đất nhá")
    send_mess.send_keys(Keys.ENTER)

for i in range(30):
    sendMess()
#3. Dung chuong trinh 5s
sleep(100)

#4. Dong trinh duyet
browser.close()