# 웹 크롤링 동작
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
webdriver_manager_directory = ChromeDriverManager().install()
browser = webdriver.Chrome(service=ChromeService(webdriver_manager_directory))
import time

# ChromeDriver 실행

# Chrome WebDriver의 capabilities 속성 사용
capabilities = browser.capabilities

# - 주소 https://www.w3schools.com/ 입력
browser.get("https://www.courtauction.go.kr/")

# - 가능 여부에 대한 OK 받음
pass

# - html 파일 받음(and 확인)
html = browser.page_source
print(html)

# - 정보 획득
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

# iframe으로 전환
browser.switch_to.frame('indexFrame')

# 경매물건 버튼 클릭
elements_click_first = browser.find_element(by=By.CSS_SELECTOR, value="#menu > h1:nth-child(5) > a")
elements_click_first.click()

time.sleep(3)

# 법원 소재지 selectbox 선택
selector_element = '#idJiwonNm'
element_place = browser.find_element(by=By.CSS_SELECTOR, value=selector_element)
Select(element_place).select_by_index(3)

# 사건번호 selectbox 선택
selector_element = '#idSaYear'
element_num = browser.find_element(by=By.CSS_SELECTOR, value=selector_element)
Select(element_num).select_by_index(2)

# # iframe으로 전환
# browser.switch_to.frame('indexFrame')

# 검색 버튼 클릭
elements_click_second = browser.find_element(by=By.CSS_SELECTOR, value="#contents > form > div.tbl_btn > a:nth-child(1)")
elements_click_second.click()

# 한 페이지씩 이동
element_body = browser.find_element(by=By.CSS_SELECTOR, value="body")

# 스크롤 down
previous_scrollHeight = 0
while True :
    element_body.send_keys(Keys.END)

    current_scrollHeight = browser.execute_script("return document.body.scrollHeight")
    if previous_scrollHeight >= current_scrollHeight :
        break
    else :
        previous_scrollHeight = current_scrollHeight
    time.sleep(2)

# 물건상세검색 리스트
find_list = browser.find_elements(by=By.CSS_SELECTOR, value="#contents > div.table_contents")
# 사건번호
try :
    element_num = browser.find_elements(by=By.CSS_SELECTOR, value="#contents > div.table_contents > form:nth-child(1) > table > tbody > tr > td:nth-child(2)")

    num_list = []
    for i in range(len(find_list)) :
        num_list.append(element_num[i].text)
except :
    num_list = []
    for i in range(len(find_list)) :
        num_list.append("")

# 소재지 및 내역 
try :
    element_content = browser.find_elements(by=By.CSS_SELECTOR, value="#contents > div.table_contents > form:nth-child(1) > table > tbody > tr > td:nth-child(4)")
    
    content_list = []
    for i in range(len(find_list)) :
        content_list.append(element_content[i].text)
except :
    content_list = []
    for i in range(len(find_list)) :
        content_list.append("")


# 브라우저 종료
browser.quit()