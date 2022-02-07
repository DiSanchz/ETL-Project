#Importing libraries and setting up the scrapping tools




import requests as req
from bs4 import BeautifulSoup as bs
import pandas as pd
import json
import time 
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import warnings  
warnings.simplefilter('ignore')

opciones=Options()

opciones.add_experimental_option('excludeSwitches', ['enable-automation'])
opciones.add_experimental_option('useAutomationExtension', False)
opciones.headless=False    
opciones.add_argument('--start-maximized')         
#opciones.add_argument('user-data-dir=selenium')   
#opciones.add_extension('driver_folder/adblock.crx')       
opciones.add_argument('--incognito')

driver = "./chromedriver.exe"
driver = webdriver.Chrome(driver,options = opciones)





#Scrapping




############
#Start (Germany)
############

#As many tables are being scrapped and converted into dataframes, with the objective of having just one
#dataframe in the end, a firs table (for germany in this case) is going to be scrapped outside the main
#scrapping loop so all dataframes extracted in the scrapping loop can be merged into it

url = 'http://www.gobiernodecanarias.org/istac/jaxi-istac/menu.do?uripub=urn:uuid:a19805e5-1674-4efd-b047-1ab0abac9c36'
driver.get(url)

print('Progress 0%')
print('Working on Germany....')  

#Getting data on imports

imports=driver.find_element_by_xpath('//*[@id="bloq_interior"]/div/div/div/ul/li[3]/ul/li[2]/a')
imports.click()

#Selecting data display options and country


valor=driver.find_element_by_xpath('//*[@id="tdSelect1"]/select/option[1]')
valor.click()
pais=driver.find_element_by_xpath('//*[@id="tabla"]/div/div/table[1]/tbody/tr/td[3]/fieldset/table/tbody/tr[1]/td/table/tbody/tr[3]/td[1]/div/input')
pais.send_keys('Alemania')
select=driver.find_element_by_xpath('//*[@id="tabla"]/div/div/table[1]/tbody/tr/td[3]/fieldset/table/tbody/tr[1]/td/table/tbody/tr[3]/td[1]/div/img[2]')
select.click()
tiempo=driver.find_element_by_xpath('//*[@id="tabla"]/div/div/table[2]/tbody/tr/td[1]/fieldset/table/tbody/tr[1]/td/table/tbody/tr[3]/td[2]/div/img[1]')
tiempo.click()
ver=driver.find_element_by_xpath('//*[@id="tabla"]/div/div/table[3]/tbody/tr[3]/td[2]/a/span')
ver.click()

#Rotate table so all the data can be scrapped

rotar=driver.find_element_by_xpath('//*[@id="seleccionModal"]/img')
rotar.click()
A=driver.find_element_by_xpath('//*[@id="tablaFormRotacionPost"]/table/tbody/tr/td/table/tbody/tr/td[2]/fieldset/table/tbody/tr[2]/td/select/option[2]')
A.click()
B=driver.find_element_by_xpath('//*[@id="tablaFormRotacionPost"]/table/tbody/tr/td/table/tbody/tr/td[3]/fieldset/table/tbody/tr[2]/td/img[1]')
B.click()
C=driver.find_element_by_xpath('//*[@id="tablaFormRotacionPost"]/table/tbody/tr/td/table/tbody/tr/td[4]/fieldset/table/tbody/tr[2]/td/select/option[1]')
C.click()
D=driver.find_element_by_xpath('//*[@id="tablaFormRotacionPost"]/table/tbody/tr/td/table/tbody/tr/td[3]/fieldset/table/tbody/tr[2]/td/img[3]')
D.click()
E=driver.find_element_by_xpath('//*[@id="tablaFormRotacionPost"]/div/a/span')
E.click()

figures = [e.text for e in driver.find_elements_by_class_name('dataCell')]
del figures[0]
timetags = [e.text for e in driver.find_elements_by_class_name('tableCellMed')]

df_base = pd.DataFrame(list(zip(timetags, figures)),
columns =['Time', 'Alemania'])

############
#Loop for the other countries' scrapping
############

Countries_exc_ger = ['Reino Unido', 'Países Bajos', 'Irlanda', 'Suecia', 'Dinamarca', 'Bélgica', 'Italia', 'Francia', 'Suiza', 'Chequia', 'Polonia']
Countries_exc_ger_eng = ['United Kingdom', 'The Netherlands', 'Ireland', 'Sweden', 'Denmark', 'Belgium', 'Italy', 'France', 'Switzerland', 'Czechia', 'Poland']
#countires' names in the first list are in Spanish as is the language of the source webpage
#the second list is used solely for progress tracking purposes

counter = 0


#Declaring a loop that iterates over the list above and scraps the data for all intended countries
#The structure is the same as in the code above for the first country scrapped (Germany) 
#The main addition is that at the end of each iteration the obtained df is merged to the base one

for i in Countries_exc_ger:
    print(f'Progress {round(((counter + 1)/12)*100,2)}%')
    print(f'Working on {Countries_exc_ger_eng[counter]}....')
    counter += 1

    url = 'http://www.gobiernodecanarias.org/istac/jaxi-istac/menu.do?uripub=urn:uuid:a19805e5-1674-4efd-b047-1ab0abac9c36'
    driver.get(url)

    imports=driver.find_element_by_xpath('//*[@id="bloq_interior"]/div/div/div/ul/li[3]/ul/li[2]/a')
    imports.click()
    valor=driver.find_element_by_xpath('//*[@id="tdSelect1"]/select/option[1]')
    valor.click()
    pais=driver.find_element_by_xpath('//*[@id="tabla"]/div/div/table[1]/tbody/tr/td[3]/fieldset/table/tbody/tr[1]/td/table/tbody/tr[3]/td[1]/div/input')
    pais.send_keys(f'{i}')
    select=driver.find_element_by_xpath('//*[@id="tabla"]/div/div/table[1]/tbody/tr/td[3]/fieldset/table/tbody/tr[1]/td/table/tbody/tr[3]/td[1]/div/img[2]')
    select.click()
    tiempo=driver.find_element_by_xpath('//*[@id="tabla"]/div/div/table[2]/tbody/tr/td[1]/fieldset/table/tbody/tr[1]/td/table/tbody/tr[3]/td[2]/div/img[1]')
    tiempo.click()
    ver=driver.find_element_by_xpath('//*[@id="tabla"]/div/div/table[3]/tbody/tr[3]/td[2]/a/span')
    ver.click()
    
    rotar=driver.find_element_by_xpath('//*[@id="seleccionModal"]/img')
    rotar.click()
    A=driver.find_element_by_xpath('//*[@id="tablaFormRotacionPost"]/table/tbody/tr/td/table/tbody/tr/td[2]/fieldset/table/tbody/tr[2]/td/select/option[2]')
    A.click()
    B=driver.find_element_by_xpath('//*[@id="tablaFormRotacionPost"]/table/tbody/tr/td/table/tbody/tr/td[3]/fieldset/table/tbody/tr[2]/td/img[1]')
    B.click()
    C=driver.find_element_by_xpath('//*[@id="tablaFormRotacionPost"]/table/tbody/tr/td/table/tbody/tr/td[4]/fieldset/table/tbody/tr[2]/td/select/option[1]')
    C.click()
    D=driver.find_element_by_xpath('//*[@id="tablaFormRotacionPost"]/table/tbody/tr/td/table/tbody/tr/td[3]/fieldset/table/tbody/tr[2]/td/img[3]')
    D.click()
    E=driver.find_element_by_xpath('//*[@id="tablaFormRotacionPost"]/div/a/span')
    E.click()

    figures = [e.text for e in driver.find_elements_by_class_name('dataCell')]
    del figures[0]
    timetags = [e.text for e in driver.find_elements_by_class_name('tableCellMed')]

#Merging this iteration's DF with the base one
    
    df = pd.DataFrame(list(zip(timetags, figures)),
    columns =['Time', f'{i}'])
    df_base = df.merge(df_base, on='Time')
    display(df_base)

#Saving the data into a CSV file after all the data has been scrapped and the loop ends   
    
print('Progress 99%')    
print('Saving data....')
df_base.to_csv('data/canary_imports_dirty.csv') 
print('Progress 100%')
print('Task accomplished')

#In this particular case the loop is told to display the database with each iteration as due 
#to the relatively moderate size of the "final product" this not unfeasible, but for larger
#scrapping excercises or dataframes this will be totally unpractical.
