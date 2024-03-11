# * 웹 크롤링 동작
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
webdriver_manager_directory = ChromeDriverManager().install()
browser = webdriver.Chrome(service=ChromeService(webdriver_manager_directory))
# ChromeDriver 실행
# Chrome WebDriver의 capabilities 속성 사용
capabilities = browser.capabilities
# - 주소 https://www.w3schools.com/ 입력
browser.get("https://pages.coupang.com/p/106978")
# - 가능 여부에 대한 OK 받음
pass
# - html 파일 받음(and 확인)
html = browser.page_source

pass
from selenium.webdriver.common.by import By

## 여러개 elements 정보 가져오기
selector_value = "span.mnemitem_goods_tit"
elements_path = browser.find_elements(by=By.CSS_SELECTOR,value=selector_value)
type(elements_path)


for webelement in elements_path:
    title = webelement.text
    print("{}".format(title))
    pass
pass
# 브라우저 종료
browser.quit()