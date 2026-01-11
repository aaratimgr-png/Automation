# POM=used to reduce redundancy
from Library.ConfigReader import ElementsRead
class RegistrationData:

    def __init__(self,obj):
         global driver
         driver=obj
    def enterFirstName(self,firstname):
         driver.find_element('name',ElementsRead('Registration','fname')).send_keys(firstname)
    def enterLastName(self,lastname):
         driver.find_element('name',ElementsRead('Registration','lname')).send_keys(lastname)
    def enterBirthMonth(self,birthMonth):
         driver.find_element('name',ElementsRead('Registration','month')).send_keys(birthMonth)
    def enterBirthDay(self,birthDay):
         driver.find_element('name',ElementsRead('Registration','day')).send_keys(birthDay)
    def enterBirthYear(self,birthYear):
         driver.find_element('name',ElementsRead('Registration','year')).send_keys(birthYear)
    def  clickGender(self,genderData):
         if genderData=='Male':
            driver.find_element('xpath',ElementsRead('Registration','gender_ypath')).click()
         elif genderData=='Female':
            driver.find_element('xpath',ElementsRead('Registration','gender_xpath')).click()
         else:
            driver.find_element('xpath',ElementsRead('Registration','gender_zpath')).click()
    def enterEmail(self,email):
         driver.find_element('xpath',ElementsRead('Registration','email')).send_keys(email)
    def enterPwd(self,password):
         driver.find_element('xpath',ElementsRead('Registration','pwd')).send_keys(password)
    def clickSubmit(self):
         driver.find_element('xpath',ElementsRead('Registration','submit')).click()
    
