# * 웹 크롤링 동작
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time

# def function_name():
#     pass
#     return 0 

# 기능 function : 한 업무에 종속성이 없는것
def getBrowserFromURI(uri = "https://www.courtauction.go.kr/"):
    webdriver_manager_directory = ChromeDriverManager().install()
    # ChromeDriver 실행
    browser = webdriver.Chrome(service=ChromeService(webdriver_manager_directory))
    # Chrome WebDriver의 capabilities 속성 사용
    browser.get(uri)
    return browser 


def selectCourts(browser):
    # iframe 으로 전환
    browser.switch_to.frame('indexFrame')
    from selenium.webdriver.common.by import By
    # click menu : #menu > h1:nth-child(5) > a > img
    browser.find_element(by=By.CSS_SELECTOR, value="#menu > h1:nth-child(5) > a > img").click()
    from selenium.webdriver.support.ui import Select
    # 법원/소재지 리스트 : #idJiwonNm > option
    element_courts = browser.find_elements(by=By.CSS_SELECTOR, value="#idJiwonNm > option")
    for index in range(len(element_courts)) :
        select_court = Select(browser.find_element(by=By.CSS_SELECTOR, value="#idJiwonNm"))
        select_court.select_by_index(index)
        # 검색 클릭 : #contents > form > div.tbl_btn > a:nth-child(1) > img
        url = "#contents > form > div.tbl_btn > a:nth-child(1) > img"
        browser.find_element(by=By.CSS_SELECTOR, value=url).click()
        time.sleep(1)
        # 이전 화면 : #contents > div.table_contents > form:nth-child(1) > div > div > a:nth-child(5) > img
        url = "#contents > div.table_contents > form:nth-child(1) > div > div > a:nth-child(5) > img"
        browser.find_element(by=By.CSS_SELECTOR, value=url).click()
        time.sleep(3)
        pass
    pass
    return len(element_courts)

# 브라우저 종료
def quitBrowser(browser) :
    browser.quit()