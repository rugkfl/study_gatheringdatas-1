# * 웹 크롤링 동작
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
webdriver_manager_directory = ChromeDriverManager().install()
browser = webdriver.Chrome(service=ChromeService(webdriver_manager_directory))
import time

from selenium.webdriver.chrome.options import Options


# ChromeDriver 실행
browser = webdriver.Chrome(service=ChromeService(webdriver_manager_directory))
# Chrome WebDriver의 capabilities 속성 사용
capabilities = browser.capabilities

# - 주소입력

# page number
for page_number in range(1,11) :
    url = "https://www.coupang.com/np/campaigns/348?page={}".format(page_number)
    browser.get(url)
    time.sleep(3)
    # - html 파일 받음(and 확인)
    html = browser.page_source
    print(html)
    pass

# - 가능 여부에 대한 OK 받음
pass


# - 정보 획득
# browser.save_screenshot('./formats.png')

# 브라우저 종료
browser.quit()