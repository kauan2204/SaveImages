#---------- Create by Kauan Leandro ----------
#---- this code was based on the code of Christopher Zita ----

from selenium import webdriver #pip install selenium
from selenium.webdriver.common.keys import Keys
import time
import os

#input to do the research
search = str(input("você quer fotos sobre?: "))
search = search.lower()

#input to know the number of images
quat = int(input("quantas fotos você quer?: "))

#open google
driver = webdriver.Chrome("chromedriver.exe")
#go to google images
driver.get("https://www.google.com.br/imghp?hl=pt-BR&tab=ri&ogbl")

#click to search
xpath = '//*[@id="sbtc"]/div/div[2]/input'
box = driver.find_element_by_xpath(xpath)

#type the name to search the message
box.send_keys(search)
box.send_keys(Keys.ENTER)

#function that creates directory to keep
def createDIRECTORY(name):
    try:
        os.mkdir(f'C:/Users/Joseane/PycharmProjects/projects/{name}')
        print("diretorio criado")

    except os.error:
        print("n foi possivel criar o diretorio!")
        os.mkdir(f'C:/Users/Joseane/PycharmProjects/projects/directory')

up = 'up'
down = 'down'

#scroll down or up to load images
def rollWindows(up_or_down):
    a = ''
    if up_or_down == up:
        a = str('0,document.body.scrollHeight')

    if up_or_down == down:
        a = str('document.body.scrollHeight, 0')

    last_height = driver.execute_script('return document.body.scrollHeight')
    while True:
        driver.execute_script(f'window.scrollTo({a})')
        time.sleep(2)
        new_height = driver.execute_script('return document.body.scrollHeight')
        try:
            driver.find_element_by_xpath('//*[@id="islmp"]/div/div/div/div/div[5]/input').click()
            time.sleep(3)
        except:
            pass
        if new_height == last_height:
            break
        last_height = new_height

#print the images and save
def savedImg():
    for i in range(0, quat):
        i += 1
        xpathIMG = f'//*[@id="islrg"]/div[1]/div[{str(i)}]/a[1]/div[1]/img'
        try:
            driver.find_element_by_xpath(xpathIMG).screenshot(f'C:/Users/Joseane/PycharmProjects/projects/{search}/{str(i)}.png')

        except:
            pass


directory = createDIRECTORY(search)
rollWindows(up)
rollWindows(down)
savedImg()
driver.quit()