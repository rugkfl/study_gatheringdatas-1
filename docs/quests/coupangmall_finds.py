# * 웹 크롤링 동작
from selenium import webdriver 

# ChromeDriver 실행
browser = webdriver.Chrome()                        # - chrome browser 열기

pass
browser.get("https://www.coupang.com/np/categories/317778?traid=home_CategoryBest_quick_link")           # - 주소 입력

pass
html = browser.page_source                          # - html 파일 받음(and 확인)

from selenium.webdriver.common.by import By
selector_value = "div.name"
elements_path = browser.find_elements(by=By.CSS_SELECTOR,value = selector_value)            # - 정보 획득

for webelement in elements_path:
    title = webelement.text
    print("{}".format(title))


browser.quit()                                      # - 브라우저 종료
