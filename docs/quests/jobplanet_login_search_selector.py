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
browser.get("https://www.jobplanet.co.kr/users/sign_in?_nav=gb")

# - 가능 여부에 대한 OK 받음
pass

# - html 파일 받음(and 확인)
html = browser.page_source


# - 정보 획득
from selenium.webdriver.common.by import By

# 로그인 이메일
element_login_field = browser.find_element(by=By.CSS_SELECTOR, value="#user_email")
element_login_field.send_keys("kimgyoungha61@gmail.com")

# 로그인 비밀번호
element_password_field = browser.find_element(by=By.CSS_SELECTOR, value="#user_password")
element_password_field.send_keys("") # 브레이크 걸고 직접 넣어서 실행함

# 로그인 버튼
element_login_button = browser.find_element(by=By.CSS_SELECTOR, value="  div > section.section_email.er_r > fieldset > button")
element_login_button.click()

# 브라우저 종료
browser.quit()