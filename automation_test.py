from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
from appium.webdriver.common.touch_action import TouchAction


capabilities = {
    "platformName": "Android",
    "deviceName": "19301FDEE00AQ8",
    "platformVersion": "14",
    "appPackage": "org.mozilla.firefox",
    "appActivity": "org.mozilla.firefox.App",
}

appium_server_url = 'http://localhost:4723/wd/hub'
driver = webdriver.Remote(appium_server_url, capabilities)
wait = WebDriverWait(driver, 10)

# 開啟官網
driver.get("https://cathaybk.com.tw/cathaybk/")
time.sleep(5)
# 官網截圖
screenshot_path = "HomePage.png"
driver.save_screenshot(screenshot_path)

# 進入信用卡列表
menuList = WebDriverWait(driver, 20).until(EC.presence_of_element_located
    ((By.XPATH, '//android.webkit.WebView[@text="國泰世華銀行"]/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.view.View[1]')))
menuList.click()

menuList_select1 = WebDriverWait(driver, 20).until(EC.presence_of_element_located
    ((By.XPATH, '//android.webkit.WebView[@text="國泰世華銀行"]/android.view.View/android.view.View[2]/android.view.View/android.view.View[3]/android.view.View[2]/android.view.View')))
menuList_select1.click()

menuList_selectVisa = WebDriverWait(driver, 20).until(EC.presence_of_element_located
    ((By.XPATH, '//android.webkit.WebView[@text="國泰世華銀行"]/android.view.View/android.view.View[2]/android.view.View/android.view.View[3]/android.view.View[3]/android.view.View')))
menuList_selectVisa.click()

# 信用卡列表截圖
screenshot_path = "CreditCard.png"
driver.save_screenshot(screenshot_path)

# 計算數量
xpath = '//android.view.View[@content-desc="卡片介紹"]/*'
elements = driver.find_elements(By.XPATH, xpath)
element_count = len(elements)
print(f"項目數量: {element_count}")

# 進入停用卡列表
cardInfo = WebDriverWait(driver, 20).until(EC.presence_of_element_located
                      ((By.XPATH, '//android.view.View[@content-desc="卡片介紹"]')))
cardInfo.click()
time.sleep(3)

start_x = 1000
start_y = 1300
end_x = 100
end_y = 1300
driver.swipe(start_x, start_y, end_x, end_y, 500)

width = driver.get_window_size()['width']
height = driver.get_window_size()['height']
touch_action = TouchAction(driver)
touch_action.tap(x=1000, y=1300).perform()
time.sleep(3)

# 停用卡截圖
screenshot_path = "SuspendCard.png"
driver.save_screenshot(screenshot_path)