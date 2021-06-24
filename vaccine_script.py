import selenium
from selenium import webdriver
from selenium.webdriver.firefox.options import Options 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time 

options = Options()
options.binary_location = r"---Your binary location here----\firefox.exe"
browser = webdriver.Firefox(options=options, executable_path=r'---Your binary location here---\geckodriver.exe')



#######################################define different functions for setting Bundesland and place to be vaccinated #################################################


def selectBundesland():
  browser.get("https://www.impfterminservice.de/impftermine")                                           #starts vaccine site 
  time.sleep(1)                                                                                         #sleep to load site
  ddBundesland = browser.find_elements_by_class_name("select2-selection.select2-selection--single")[0]  #select drop Down List
  ddBundesland.send_keys(Keys.RETURN)                                                                   #start drop Down List
  ddBundesland.send_keys(Keys.RETURN)                                                                   #choose Baden Württemberg


def submitEntries():
  submit = browser.find_element_by_class_name("btn.kv-btn.btn-magenta.text-uppercase.d-inline-block")
  submit.send_keys(Keys.RETURN)
  time.sleep(2)

  anspruchPruefen = browser.find_elements_by_xpath("/html/body/app-root/div/app-page-its-login/div/div/div[2]/app-its-login-user/div/div/app-corona-vaccination/div[2]/div/div/label[2]")
  if len(anspruchPruefen) > 0:                                                                           #checks if we are on the digital waiting room, if not we proceed to check for an appointment
    anspruchPruefen[0].click()
    keinErfolg = browser.find_elements_by_xpath("/html/body/app-root/div/app-page-its-login/div/div/div[2]/app-its-login-user/div/div/app-corona-vaccination/div[3]/div/div/div/div[2]/div/div/div")
    time.sleep(4)
    if len(keinErfolg) == 0:
       print("Found a Code for vaccination appointment")
       time.sleep(7200)    #sleep for 2h if appointment is found
  

def waiblingen():
  impfzentrum = browser.find_elements_by_class_name("select2-selection.select2-selection--single")[1]    #select drop down element for vaccine centre 
  impfzentrum.send_keys(Keys.RETURN)
  i = 0
  while i < 9:
    impfzentrum.send_keys(Keys.ARROW_DOWN)
    i += 1
  impfzentrum.send_keys(Keys.RETURN)
  time.sleep(1)


def stuttgartKlinikum():
  impfzentrum = browser.find_elements_by_class_name("select2-selection.select2-selection--single")[1]    #select drop down element for vaccine centre 
  impfzentrum.send_keys(Keys.RETURN)
  i = 0
  while i < 4:
    impfzentrum.send_keys(Keys.ARROW_DOWN)
    i += 1
  impfzentrum.send_keys(Keys.RETURN)
  time.sleep(1)  


def stuttgartRobertBosch():
  impfzentrum = browser.find_elements_by_class_name("select2-selection.select2-selection--single")[1]    #select drop down element for vaccine centre 
  impfzentrum.send_keys(Keys.RETURN)
  i = 0
  while i < 5:
    impfzentrum.send_keys(Keys.ARROW_DOWN)
    i += 1
  impfzentrum.send_keys(Keys.RETURN)
  time.sleep(1)


def ludwigsburg():
  impfzentrum = browser.find_elements_by_class_name("select2-selection.select2-selection--single")[1]    #select drop down element for vaccine centre 
  impfzentrum.send_keys(Keys.RETURN)
  i = 0
  while i < 10:
    impfzentrum.send_keys(Keys.ARROW_DOWN)
    i += 1
  impfzentrum.send_keys(Keys.RETURN)
  time.sleep(1)


def ilsfeld():
  impfzentrum = browser.find_elements_by_class_name("select2-selection.select2-selection--single")[1]    #select drop down element for vaccine centre 
  impfzentrum.send_keys(Keys.RETURN)
  i = 0
  while i < 20:
    impfzentrum.send_keys(Keys.ARROW_DOWN)
    i += 1
  impfzentrum.send_keys(Keys.RETURN)
  time.sleep(1)


def rotAmSee():
  impfzentrum = browser.find_elements_by_class_name("select2-selection.select2-selection--single")[1]    #select drop down element for vaccine centre 
  impfzentrum.send_keys(Keys.RETURN)
  i = 0
  while i < 22:
    impfzentrum.send_keys(Keys.ARROW_DOWN)
    i += 1
  impfzentrum.send_keys(Keys.RETURN)
  time.sleep(1) 


################################################################################## main loop ###################################################################################


while True:
  selectBundesland()
  waiblingen()
  submitEntries()
 

  selectBundesland()
  ludwigsburg()
  submitEntries()
 
  
  selectBundesland()
  ilsfeld()
  submitEntries()
  
  selectBundesland()
  rotAmSee()
  submitEntries()
 
