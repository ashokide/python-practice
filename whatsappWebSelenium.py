import time

from selenium import webdriver as wd
from selenium.webdriver.common.keys import Keys
root = wd.Chrome(executable_path=r'F:\pythonProjects\projects\chromedriver.exe')

root.get('https://web.whatsapp.com/')
root.maximize_window()
time.sleep(10)
name = ''
msg = 'Hello.......'

user = root.find_element_by_xpath('//span[@title="{}"]'.format(name))
user.click()

for i in range(1,1001):
    msg_box = root.find_element_by_xpath('/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[2]/div/div[2]')
    msg_box.send_keys(msg)
    msg_box.send_keys(Keys.RETURN)
    time.sleep(2)

root.close()
