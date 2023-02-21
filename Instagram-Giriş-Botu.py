from İnstagramBilgi import kullanıcıadı,sifre
from selenium import webdriver
from selenium.webdriver.common.keys import Keys #klavye ile müdahele icin
from selenium.webdriver.common.by import By #find elementler icin
import time

driver=webdriver.Chrome("C:/Users/enes_/OneDrive/Masaüstü/Python Egitimleri/ChromeDriver/chromedriver.exe")

url="https://www.instagram.com/"

driver.get(url)
time.sleep(2)

ka=driver.find_element("xpath","//*[@id='loginForm']/div/div[1]/div/label/input") #instagram giris sitesi kullanıcı adının giris yapıldıgı input alanının xpath i
ka.send_keys(kullanıcıadı) #import ettıgımız İnstagramBilgi icinden kullanıcı adını sitedeki giris kısmına input ettık

ksifre=driver.find_element("xpath","//*[@id='loginForm']/div/div[2]/div/label/input") #instagram giris sitesi sifrenin giris yapıldıgı input alanının xpath i
ksifre.send_keys(sifre) #import ettıgımız İnstagramBilgi icinden sifreyi sitedeki sifre kısmına input ettık

ksifre.send_keys(Keys.ENTER)
time.sleep(2)
driver.maximize_window()
time.sleep(50) #giris yaptıktan sonra chrome kapanmasın diye

