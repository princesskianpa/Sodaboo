###Sodaboo 0.0.3
##
#

import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotInteractableException
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import TimeoutException
import time
from imgsearch import *
import sys


USERNAME = ""
PASSWORD = ""
SERVER = "de3"

driver = webdriver.Firefox()
driver.get("https://www.soldatenspiel.de/")

#driver.minimize_window()
#driver.maximize_window()

#Find & select Server
select = Select(driver.find_element_by_name('server'))
select.select_by_visible_text(SERVER)

#Type in Username
elem = driver.find_element_by_name("email")
elem.clear()
elem.send_keys(USERNAME)

#Type in password
passy = driver.find_element_by_name("password")
passy.clear()
passy.send_keys(PASSWORD)

#Send Enter
elem.send_keys(Keys.RETURN)
time.sleep(7)

#Things I might need somewhen...
#ausdauer = driver.find_element_by_id('stamina-bar-js').text.replace('/', '') #Stamina
#credits = driver.find_element_by_class_name('credits-js ').text.replace('.', '') #Credits
#cost = driver.find_element_by_css_selector('.content-stamina-credit-button > p:nth-child(3)').text.replace('.', '') #Stamina cost
#rage = driver.find_element_by_id('rage-bar-js').text.replace('/', '') #Rage
#freeticket = driver.find_element_by_class_name('freefight_count').text.replace('/', '') # Free Fight tickets

#Login check
try:
    name = driver.find_element_by_class_name("avatar-name").text
    print ("Sucessfull logged in as "+ name +".")
except :
    print("Cannot verify to be logged in.")


##Check for elements
def patro():
    try:
        patro = driver.find_element_by_css_selector('#progress-work-team-icon')
        if patro.is_displayed():
            pass
        else:
            print('Patrouille läuft noch nicht, wird gestartet...')
            patrouille()
    except NoSuchElementException:
        print('error patro')

def missi():
    try:
        missi = driver.find_element_by_css_selector('#progress-mission-icon')
        if missi.is_displayed():
            pass
        else:
            print('Mission läuft noch nicht, wird gestartet...')
            mission()
    except NoSuchElementException:
        print('error missi')

def daily():
    try:
        daily = driver.find_element_by_css_selector('#progress-dailybonus-icon')
        if daily.is_displayed():
            time.sleep(1.5)
            driver.find_element_by_css_selector('#progress-dailybonus-icon').click() #open daily
            time.sleep(1.5)
            driver.find_element_by_css_selector('.style-button-middle').click() #get it
            time.sleep(2.5)
            driver.find_element_by_css_selector('.style-button-confirm').click() #Click ok after recieved.
            time.sleep(1.5)
        else:
            pass
    except NoSuchElementException:
        print('Daily error.')

def train():
    try:
        train = driver.find_element_by_css_selector('#progress-drill-icon')
        if train.is_displayed():
            pass
        else:
            print('Training läuft noch nicht, wird gestartet...')
            training_wa()
    except NoSuchElementException:
        print('error train')

def popup():
    for x in range (3):
        try:
            driver.find_element_by_css_selector('.style-button-confirm').click()
            time.sleep(.1)
        except NoSuchElementException:
            pass
            #print("No popup found")
def close():
    for x in range (2):
        try:
            driver.find_element_by_css_selector('#modalbox-main > div:nth-child(1) > div:nth-child(4) > div:nth-child(2)').click()
            time.sleep(.1)
        except :
            pass
            #print("No Close button found")
def bombe():
    try:
        bombe = driver.find_element_by_css_selector('#progress-event-artillerie-icon')
        if bombe.is_displayed():
            bombenwetter()
    except NoSuchElementException:
        print('error bombenwetter event is not active.')

def compi():
    try:
        compi = driver.find_element_by_css_selector('#progress-companion-drill-icon')
        if compi.is_displayed():
            pass
        else:
            print('Companion Training läuft noch nicht, wird gestartet... :)')
            companion_train()
    except NoSuchElementException:
        print('error compi')

##Patrouille & Mission & Training
def patrouille():
    time.sleep(2)
    driver.find_element_by_css_selector('div.control-icon:nth-child(4)').click() #click @ your troop
    time.sleep(2)
    driver.find_element_by_css_selector('.patrouille').click() #click @ building
    time.sleep(2)
    driver.find_element_by_css_selector('.style-button-middle').click() #start patrouille button
    #Possible Captcha solve
    try:
        if driver.find_element_by_css_selector('.content-captcha-image-wrapper > img:nth-child(2)'):
            driver.maximize_window()
            time.sleep(.5)
            captcha = region_grabber(region=(909, 609, 991, 656))   
            captcha.save('captcha.png')
            pos = imagesearcharea('captcha.png', 0, 0, 1216, 544)
            if pos[0] != -1:
                print("Patro Captcha Position : ", pos[0], pos[1])
                pyautogui.moveTo(pos[0], pos[1])
                pyautogui.click()
                #driver.minimize_window()
                time.sleep(2)
                driver.find_element_by_css_selector('#modalbox-main > div:nth-child(1) > div:nth-child(4) > div:nth-child(2)').click() #close patrouille
                time.sleep(2)
                driver.find_element_by_css_selector('div.control-icon:nth-child(4)').click() #back to main menu
                time.sleep(2)
    except NoSuchElementException:
        time.sleep(2)
        driver.find_element_by_css_selector('#modalbox-main > div:nth-child(1) > div:nth-child(4) > div:nth-child(2)').click() #close patrouille
        time.sleep(2)
        driver.find_element_by_css_selector('div.control-icon:nth-child(4)').click() #back to main menu
        time.sleep(2)

def mission():
    ausdauer = driver.find_element_by_id('stamina-bar-js').text.replace('/', '') #Ausdauer
    credits = driver.find_element_by_class_name('credits-js ').text.replace('.', '') #Find Credits
    if int(ausdauer) >= 20100:
        time.sleep(1.5)
        driver.find_element_by_css_selector('.mission').click() # click on building
        time.sleep(1.5)
        try:
            geschenk = driver.find_element_by_xpath("/html/body/div/div[1]/div/div[5]/div[12]/div[1]/div[2]/div[2]/div[2]/div[1]/div/div[5]/div/div/div[1]/div/img")
            if geschenk.is_displayed():
                time.sleep(2)
                driver.find_element_by_xpath('/html/body/div/div[1]/div/div[5]/div[12]/div[1]/div[2]/div[2]/div[2]/form/div/div[2]/p').click() #start mission button
                ###Captcha###
                try:
                    if driver.find_element_by_css_selector('.content-captcha-image-wrapper > img:nth-child(2)'):                                    ######## EDIT CONTENT
                        driver.maximize_window()
                        time.sleep(.5)
                        captcha = region_grabber(region=(909, 609, 991, 656))   #Get small Captcha
                        captcha.save('captcha.png')
                        pos = imagesearcharea('captcha.png', 0, 0, 1216, 544)
                        if pos[0] != -1:
                            print("Mission Captcha Position : ", pos[0], pos[1])
                            pyautogui.moveTo(pos[0], pos[1])
                            pyautogui.click()
                            #driver.minimize_window()
                            time.sleep(2)
                            driver.find_element_by_xpath('/html/body/div/div[1]/div/div[5]/div[12]/div[1]/div[4]/div[2]').click() # Close Mission
                            time.sleep(2)
                except NoSuchElementException:
                    time.sleep(2)
                    driver.find_element_by_xpath('/html/body/div/div[1]/div/div[5]/div[12]/div[1]/div[4]/div[2]').click() # Close Mission
                    time.sleep(2)

        except NoSuchElementException:
            time.sleep(1)
            driver.find_element_by_css_selector('div.content-mission-switch-right:nth-child(3) > img:nth-child(1)').click() #Contine button
        
            try:
                geschenk = driver.find_element_by_xpath("/html/body/div/div[1]/div/div[5]/div[12]/div[1]/div[2]/div[2]/div[2]/div[1]/div/div[5]/div/div/div[1]/div/img")
                if geschenk.is_displayed(): #check for Geschenk
                    time.sleep(2)
                    driver.find_element_by_xpath('/html/body/div/div[1]/div/div[5]/div[12]/div[1]/div[2]/div[2]/div[2]/form/div/div[2]/p').click() #start mission button
                    ###Captcha###
                    try:
                        if driver.find_element_by_css_selector('.content-captcha-image-wrapper > img:nth-child(2)'):                                    ######## EDIT CONTENT
                            driver.maximize_window()
                            time.sleep(.5)
                            captcha = region_grabber(region=(909, 609, 991, 656))   #Get small Captcha
                            captcha.save('captcha.png')
                            pos = imagesearcharea('captcha.png', 0, 0, 1216, 544)
                            if pos[0] != -1:
                                print("Mission Captcha Position : ", pos[0], pos[1])
                                pyautogui.moveTo(pos[0], pos[1])
                                pyautogui.click()
                                #driver.minimize_window()
                                time.sleep(2)
                                driver.find_element_by_xpath('/html/body/div/div[1]/div/div[5]/div[12]/div[1]/div[4]/div[2]').click() # Close Mission
                                time.sleep(2)
                    except NoSuchElementException:
                        time.sleep(2)
                        driver.find_element_by_xpath('/html/body/div/div[1]/div/div[5]/div[12]/div[1]/div[4]/div[2]').click() # Close Mission
                        time.sleep(2)

            except NoSuchElementException:
                time.sleep(1)
                driver.find_element_by_css_selector('#mission-text-js > div:nth-child(1) > div:nth-child(2) > img:nth-child(1)').click() #Contine button
                try:
                    geschenk = driver.find_element_by_xpath("/html/body/div/div[1]/div/div[5]/div[12]/div[1]/div[2]/div[2]/div[2]/div[1]/div/div[5]/div/div/div[1]/div/img")
                    if geschenk.is_displayed(): #check for Geschenk
                        time.sleep(2)
                        driver.find_element_by_xpath('/html/body/div/div[1]/div/div[5]/div[12]/div[1]/div[2]/div[2]/div[2]/form/div/div[2]/p').click() #start mission button
                        ###Captcha###
                        try:
                            if driver.find_element_by_css_selector('.content-captcha-image-wrapper > img:nth-child(2)'):                                    ######## EDIT CONTENT
                                driver.maximize_window()
                                time.sleep(.5)
                                captcha = region_grabber(region=(909, 609, 991, 656))   #Get small Captcha
                                captcha.save('captcha.png')
                                pos = imagesearcharea('captcha.png', 0, 0, 1216, 544)
                                if pos[0] != -1:
                                    print("Mission Captcha Position : ", pos[0], pos[1])
                                    pyautogui.moveTo(pos[0], pos[1])
                                    pyautogui.click()
                                    #driver.minimize_window()
                                    time.sleep(2)
                                    driver.find_element_by_xpath('/html/body/div/div[1]/div/div[5]/div[12]/div[1]/div[4]/div[2]').click() # Close Mission
                                    time.sleep(2)
                        except NoSuchElementException:
                            time.sleep(2)
                            driver.find_element_by_xpath('/html/body/div/div[1]/div/div[5]/div[12]/div[1]/div[4]/div[2]').click() # Close Mission
                            time.sleep(2)

                except NoSuchElementException:
                    time.sleep(1)
                    driver.find_element_by_xpath('/html/body/div/div[1]/div/div[5]/div[12]/div[1]/div[2]/div[2]/div[2]/form/div/div[2]/p').click() #start mission button
                    time.sleep(2)
                    ###Captcha###
                    try:
                        if driver.find_element_by_css_selector('.content-captcha-image-wrapper > img:nth-child(2)'):                                    ######## EDIT CONTENT
                                driver.maximize_window()
                                time.sleep(.5)
                                captcha = region_grabber(region=(909, 609, 991, 656))   #Get small Captcha
                                captcha.save('captcha.png')
                                pos = imagesearcharea('captcha.png', 0, 0, 1216, 544)
                                if pos[0] != -1:
                                    print("Mission Captcha Position : ", pos[0], pos[1])
                                    pyautogui.moveTo(pos[0], pos[1])
                                    pyautogui.click()
                                    #driver.minimize_window()
                                    time.sleep(2)
                                    driver.find_element_by_xpath('/html/body/div/div[1]/div/div[5]/div[12]/div[1]/div[4]/div[2]').click() # Close Mission
                                    time.sleep(2)
                    except NoSuchElementException:
                        time.sleep(2)
                        driver.find_element_by_xpath('/html/body/div/div[1]/div/div[5]/div[12]/div[1]/div[4]/div[2]').click() # Close Mission
                        time.sleep(2)

    if int(ausdauer) <= 19100:
        driver.find_element_by_css_selector('.add-stamina').click() #click on ausdauer +
        time.sleep(2)
        cantreload = driver.find_element_by_class_name('content-stamina-remain').text.replace("Du kannst heute noch mal deine Ausdauer aufladen.", " ")
        if cantreload == 0:
            driver.find_element_by_css_selector('#modalbox-sub > div:nth-child(1) > div:nth-child(4) > div:nth-child(2)').click() # close window
        else:
            cost = driver.find_element_by_css_selector('.content-stamina-credit-button > p:nth-child(3)').text.replace('.', '') #Find Cost

            if int(cost) <= int(credits):
                driver.find_element_by_css_selector('.content-stamina-credit-button').click() #Click on recharge
                time.sleep(2)
                mission()
            if int(cost) > int(credits):
                driver.find_element_by_css_selector('#modalbox-sub > div:nth-child(1) > div:nth-child(4) > div:nth-child(3)').click() #Close not enough money
            time.sleep(2)
#training contains messy code
def training_wa():
    time.sleep(2)
    try:
        miss = driver.find_element_by_css_selector('#progress-mission-icon')  # Checks if Mission is already running
        if miss.is_displayed():
            print('Kann nicht Trainieren, Mission läuft schon..')
        else:
            driver.find_element_by_xpath('/html/body/div/div[1]/div/div[5]/div[24]/div').click() #click on Übungsplatz
            time.sleep(2)
            driver.find_element_by_xpath('/html/body/div/div[1]/div/div[5]/div[24]/div').click() #click on HIBA
            time.sleep(2)
            driver.find_element_by_xpath('/html/body/div/div[1]/div/div[5]/div[12]/div[1]/div[2]/div[2]/div[1]/div[2]/div[4]/div[3]').click() #click Wachausbildung +
            time.sleep(2)
            driver.find_element_by_xpath('/html/body/div/div[1]/div/div[5]/div[12]/div[1]/div[2]/div[2]/div[2]/form/div/div[2]').click() #click Ausbildung starten
            time.sleep(2)
            driver.find_element_by_xpath('/html/body/div/div[1]/div/div[5]/div[12]/div[1]/div[4]/div[2]').click() #click dismiss
            time.sleep(2)
            driver.find_element_by_xpath('//*[@id="element_0005"]').click() #click back to main menu
            time.sleep(2)
    except NoSuchElementException:
        driver.find_element_by_xpath('/html/body/div/div[1]/div/div[5]/div[24]/div').click() #click on Übungsplatz
        time.sleep(2)
        driver.find_element_by_xpath('/html/body/div/div[1]/div/div[5]/div[24]/div').click() #click on HIBA
        time.sleep(2)
        driver.find_element_by_xpath('/html/body/div/div[1]/div/div[5]/div[12]/div[1]/div[2]/div[2]/div[1]/div[2]/div[4]/div[3]').click() #click Wachausbildung +
        time.sleep(2)
        driver.find_element_by_xpath('/html/body/div/div[1]/div/div[5]/div[12]/div[1]/div[2]/div[2]/div[2]/form/div/div[2]').click() #click Ausbildung starten
        time.sleep(2)
        driver.find_element_by_xpath('/html/body/div/div[1]/div/div[5]/div[12]/div[1]/div[4]/div[2]').click() #click dismiss
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="element_0005"]').click() #click back to main menu
        time.sleep(2)

##Events
def bombenwetter():
    rage = driver.find_element_by_id('rage-bar-js').text.replace('/', '')
    if int(rage) == 100100:
        time.sleep(2)
        driver.find_element_by_css_selector('#progress-event-artillerie-icon').click() #click @ bombenwetter icon
        time.sleep(2)
        driver.find_element_by_css_selector('.teamevent-mission').click() # click @ munition herstellen

        for x in range (5):
            time.sleep(2)
            driver.find_element_by_css_selector('div.style-button-wrapper:nth-child(3) > div:nth-child(2)').click() #click 5x @ herstellen

        time.sleep(1)
        driver.find_element_by_css_selector('#modalbox-main > div:nth-child(1) > div:nth-child(4) > div:nth-child(2)').click() #click @ close
        time.sleep(2)
        driver.find_element_by_css_selector('#progress-event-artillerie-icon').click() #click @ bombenwetter icon
        time.sleep(2)
    else:
        pass

##Companion
#companion_attack not implemented (Doesn't work...)
def companion_attack():
    driver.find_element_by_css_selector('.companionarena').click() #click on arena
    time.sleep(2)
    freeticket = driver.find_element_by_class_name('freefight_count').text.replace("/", "") # get free fights
    for x in range (6):
        if int(freeticket) >= 15:
            select = Select(driver.find_element_by_name('filter'))
            select.select_by_value(1)
            driver.find_element_by_css_selector('.style-button-filter') #click on filter
            time.sleep(2)
            driver.find_element_by_css_selector('.style-button-middle') #click on attack
            time.sleep(1)
            driver.find_element_by_css_selector('.fight-force-js > div:nth-child(2)') #click on überspringen
            time.sleep(2)
            driver.find_element_by_css_selector('.div.style-contentbox-child:nth-child(3) > form:nth-child(2) > div:nth-child(1) > div:nth-child(2)') #click on continue
            time.sleep(2)
            driver.find_element_by_css_selector('.style-button-confirm') # click on Ok
        else:
            driver.find_element_by_css_selector('#modalbox-main > div:nth-child(1) > div:nth-child(4) > div:nth-child(2)') # click on close
            time.sleep(2)

def companion_train():
    time.sleep(2)
    driver.find_element_by_css_selector('div.control-icon:nth-child(6)').click() #click @ companion
    time.sleep(2)
    driver.find_element_by_css_selector('.companiondrill').click() #click @ building
    time.sleep(2)
    driver.find_element_by_css_selector('.style-button-middle').click() #start companion training button
    #Possible Captcha solve
    try:
        if driver.find_element_by_css_selector('.content-captcha-image-wrapper > img:nth-child(2)'):
            driver.maximize_window()
            time.sleep(.5)
            captcha = region_grabber(region=(909, 609, 991, 656))   
            captcha.save('captcha.png')
            pos = imagesearcharea('captcha.png', 0, 0, 1216, 544)
            if pos[0] != -1:
                print("Companion Training Captcha Position : ", pos[0], pos[1])
                pyautogui.moveTo(pos[0], pos[1])
                pyautogui.click()
                #driver.minimize_window()
                time.sleep(2)
                driver.find_element_by_css_selector('#modalbox-main > div:nth-child(1) > div:nth-child(4) > div:nth-child(2)').click() #close companion training
                time.sleep(2)
                driver.find_element_by_css_selector('div.control-icon:nth-child(6)').click() #back to main menu
                time.sleep(2)
    except NoSuchElementException:
        time.sleep(2)
        driver.find_element_by_css_selector('#modalbox-main > div:nth-child(1) > div:nth-child(4) > div:nth-child(2)').click() #close companion training
        time.sleep(2)
        driver.find_element_by_css_selector('div.control-icon:nth-child(6)').click() #back to main menu
        time.sleep(2)

if __name__=='__main__':
    while 1:
        try:
            popup()
            daily()
            missi()
            #patro()
            train()
            bombe()
            compi()
            print("sleeping for 450sec")
            time.sleep(450)
        except (ElementNotInteractableException, ElementNotInteractableException, TimeoutException, ElementClickInterceptedException):
            print("ElementNotInteractableException or ElementNotInteractableException or TimeoutException, running pop and continue..")
            try:
                popup()
                time.sleep(1)
                close()
            except (ElementNotInteractableException, ElementNotInteractableException, TimeoutException, ElementClickInterceptedException):
                print("Another Error, =/")
                close()