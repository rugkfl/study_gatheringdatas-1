# * 웹 크롤링 동작
from selenium import webdriver 

# ChromeDriver 실행
# Chrome WebDriver의 capabilities 속성 사용
# capabilities = browser.capabilities

browser = webdriver.Chrome()                        # - chrome browser 열기

pass
browser.get("https://github.com/login")             # - 주소 입력

                                                    # - 가능 여부에 대한 OK 받음
pass
html = browser.page_source                          # - html 파일 받음(and 확인)
# print(html)

from selenium.webdriver.common.by import By          # - 정보 획득
# browser.save_screenshot('./formats.png')           
element_login_field = browser.find_element(by=By.CSS_SELECTOR,value="#login_field")
element_login_field.send_keys("njh2720@gmail.com")

element_password = browser.find_element(by=By.CSS_SELECTOR,value="#password")
password = input("비밀번호 : ")
element_password.send_keys(password)
element_login_button = browser.find_element(by=By.CSS_SELECTOR,value="div > input.btn.btn-primary.btn-block.js-sign-in-button")
element_login_button.click()
pass
browser.quit()                                      # - 브라우저 종료
