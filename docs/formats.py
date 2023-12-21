# * 웹 크롤링 동작
from selenium import webdriver 

# ChromeDriver 실행
browser = webdriver.Chrome()
# Chrome WebDriver의 capabilities 속성 사용
# capabilities = browser.capabilities

browser = webdriver.Chrome()                        # - chrome browser 열기

browser.get("https://www.w3schools.com/")           # - 주소 https://www.w3schools.com/ 입력

                                                    # - 가능 여부에 대한 OK 받음
pass
html = browser.page_source                          # - html 파일 받음(and 확인)
print(html)
                                                    # - 정보 획득

browser.quit()                                      # - 브라우저 종료
