# * 웹 크롤링 동작
from selenium import webdriver 

# ChromeDriver 실행
# Chrome WebDriver의 capabilities 속성 사용
# capabilities = browser.capabilities

browser = webdriver.Chrome()                                                 # - chrome browser 열기

pass
browser.get("https://www.jobplanet.co.kr/users/sign_in?_nav=gb")             # - 주소 입력

                                                                             # - 가능 여부에 대한 OK 받음
pass
html = browser.page_source                                                  # - html 파일 받음(and 확인)
# print(html)

from selenium.webdriver.common.by import By                                 # - 정보 획득
# browser.save_screenshot('./formats.png')           
element_login_field = browser.find_element(by=By.CSS_SELECTOR,value="#user_email")                                                                  # 이메일 입력란 정보 수집
email = input("E-MAIL : ")
element_login_field.send_keys(email)                                                                                                  # 이메일 웹페이지에 전송

element_password = browser.find_element(by=By.CSS_SELECTOR,value="#user_password")                                                                  # 비밀번호 입력란 정보 수집
password = input("PASSWORD : ")                                                                                                                      # 비밀번호 입력
element_password.send_keys(password)                                                                                                                # 웹페이지에 전송
element_login_button = browser.find_element(by=By.CSS_SELECTOR,value=" div > section.section_email.er_r > fieldset > button")                       # 로그인 버튼 정보 수집
element_login_button.click()                                                                                                                        # 로그인 버튼 클릭
pass
browser.quit()                                      # - 브라우저 종료
 