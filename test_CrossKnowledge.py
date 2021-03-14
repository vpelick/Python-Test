from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
import unittest


class TestingLogin(unittest.TestCase):
   
#setup for preparing all needed data before any test case
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("https://teamshift-qa.crossknowledge.com/")
        #user and password for acessing the teamshift
        self.username = "viniciuspelick@gmail.com"
        self.password = "WLS2020qa"

#test case for logging in the theamshift
    def test_login_with_email_and_password(self):
        #loading page objects for each page
        login_page = LoginCrossKnowledgePage()
        home_page = HomePage()
        #Clicking enter button for login
        login_page.click_element(self.driver,login_page.enter_button)
        #Fill data for user email
        login_page.fill_input_box(self.driver,login_page.email_field,self.username)
        #Clicking next
        login_page.click_element(self.driver,login_page.next_button)
        #Fill data for password
        login_page.fill_input_box(self.driver,login_page.password_field,self.password)
        #Click login button
        login_page.click_element(self.driver,login_page.login_button)
        #Checking if user name element is displayed on the home page
        self.assertTrue(home_page.check_if_element_is_displayed(self.driver,home_page.member_name))


    def tearDown(self):
        self.driver.close()

#commom page object model
class PageObject():

    def __init__(self):
        pass

    #common method for clicking elements    
    def click_element(self,driver,by):
        element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(by))
        element.click()

    #common method for filling inputboxes
    def fill_input_box(self,driver,by,text):
        element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(by))
        element.clear()
        element.send_keys(text)

    #common method for checking if element is being displayed on screen
    def check_if_element_is_displayed(self,driver,by):
        try:
            element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(by))
            return element.is_displayed()
        except:
            return False
        
#page object model for Login page
class LoginCrossKnowledgePage(PageObject):
    
    def __init__(self):
        self.__enter_button = (By.XPATH,"//nav//button[contains(text(),'Entrar')]")
        self.__email_field = (By.XPATH,"//input[@name='member_login']")
        self.__next_button = (By.XPATH,"//button[contains(text(),'Próximo')]")
        self.__password_field = (By.XPATH,"//input[@name='member_password']")
        self.__login_button = (By.XPATH,"//button[contains(text(),'Login')]")

    @property
    def enter_button(self):
        return self.__enter_button
        
    @property
    def email_field(self):
        return self.__email_field

    @property
    def next_button(self):
        return self.__next_button  

    @property
    def password_field(self):
        return self.__password_field     

    @property
    def login_button(self):
        return self.__login_button  

#page object model for homepage
class HomePage(PageObject):
    
    def __init__(self):
        self.__member_name = (By.XPATH,"//span[@class='header__menu-text header__menu-member-name']")


    @property
    def member_name(self):
        return self.__member_name


if __name__ == '__main__':
    unittest.main()