from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException


class Automation(object):
    def __init__(self):
        self.option = Options()
        self.chrome_driver_path = '/users/Stanley/Downloads/chromedriver-mac-x64/chromedriver'
        chrome_service = ChromeService(executable_path=self.chrome_driver_path)
        self.driver = webdriver.Chrome(service=chrome_service, options=self.option)
        self.wait = WebDriverWait(self.driver, 20)
    
    def visitHomePage(self):
        self.driver.get("https://www.cathaybk.com.tw/cathaybk/")          
        try:
            self.wait.until(EC.visibility_of_element_located((By.XPATH, '//div[contains(@class, "cubre-o-indexKv__wrap")]')))
            print("HomePage is loading successfully")
            self.driver.save_screenshot('HomePage.png')
        except TimeoutException:
            print("Timeout for loading Homepage")
    
    def countCardList(self):
        self.wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@class="cubre-a-menuSortBtn -l1" and text()="產品介紹"]'))).click()
        try:
            self.wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@class="cubre-a-menuSortBtn" and text()="信用卡"]')))
            print("CreditCard page is loading successfully")
        except TimeoutException:
            print("Timeout for loading CreditCard page")
        cardList = self.wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@class="cubre-a-menuSortBtn" and text()="信用卡"]/../following-sibling::div')))
        countCardList = cardList.find_elements(By.XPATH,'a')
        print(f"信用卡選單下面總共有：{len(countCardList)} 個項目")
        
    def countSuspendCard(self):
        self.wait.until(EC.visibility_of_element_located((By.XPATH, '//a[@class="cubre-a-menuLink" and text()="卡片介紹"]'))).click()
        try:
            self.wait.until(EC.visibility_of_element_located((By.XPATH, '//a[@class="cubre-m-anchor__btn swiper-slide"]/p[text()="停發卡"]')))
            print("SuspendCard is loading successfully")
        except TimeoutException:
            print("Timeout for loading SuspendCard")
        cardList = self.wait.until(EC.visibility_of_element_located((By.XPATH, '//section[@data-anchor-block="blockname06"]/div/div[@class="cubre-o-block__component"]/div/div[@class="swiper-wrapper"]')))
        countSuspendCards = cardList.find_elements(By.XPATH, '*')
        print(f"(停發)信用卡數量：{len(countSuspendCards)} 張")

if __name__ == "__main__":
    autotest = Automation()
    autotest.visitHomePage()
    autotest.countCardList()
    autotest.countSuspendCard()
    
    autotest.driver.quit()