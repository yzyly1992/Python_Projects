from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome(r'/Users/davidyang/bin/chromedriver')
wait = WebDriverWait(browser, 10)
def openFrame():
    browser.get('https://max.book118.com/html/2017/0805/126138112.shtm')
    submit = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#full > img')))
    submit.click()
def scollDown():
    print('正在下滚')
    iframe = wait.until(EC.presence_of_element_located(('#layer_view_iframe')))
    while True:
        try:
            
            browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')
        except TimeoutException:
            scollDown()
        
        
def main():
    openFrame()
    scollDown()


if __name__ == '__main__':
    main()
