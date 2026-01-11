from Base.InitiateDriver import startBrowser, closeBrowser
from Library.ConfigReader import ElementsRead
from Pages.RegistrationPage import RegistrationData

def test_InvalidateRegistration():
    
    driver=startBrowser()
    register=RegistrationData(driver)
    register.enterFirstName('@#$')
    register.enterLastName("Yo!@")
    register.enterBirthMonth("09")
    register.enterBirthDay("13")
    register.enterBirthYear("2003")
    register.clickGender()
    register.enterEmail("9809569428")
    register.enterPwd("Umanga1234")
    register.clickSubmit()
    # driver.find_element('xpath',"//input[@name='firstname']").send_keys('@#$$%^^^')
    # driver.find_element('xpath',"//input[@name='lastname']").send_keys('23456')
    # driver.find_element('name','birthday_month').send_keys("66")
    # driver.find_element('name','birthday_day').send_keys("abc")
    # driver.find_element('name','birthday_year').send_keys("2002")
    # driver.find_element('xpath',"//input[@value='1']").click()
    # driver.find_element('xpath',"//input[@name='reg_email__']").send_keys("9847828584")
    # driver.find_element('xpath',"//input[@aria-label='New password']").send_keys("Arati@1234")
    # driver.find_element('xpath',"//button[@name='websubmit']").click()
    # driver.find_element('link text','Already have an account?').click()
    closeBrowser()

   