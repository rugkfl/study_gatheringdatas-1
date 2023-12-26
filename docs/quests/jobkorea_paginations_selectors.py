# * 웹 크롤링 동작
from selenium import webdriver 
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
webdriver_manager_directory = ChromeDriverManager().install()
import time
# ChromeDriver 실행

from selenium.webdriver.chrome.options import Options

# Chrome 브라우저 옵션 생성
chrome_options = Options()

# User-Agent 설정
chrome_options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36")

# WebDriver 생성
webdriver_manager_dricetory = ChromeDriverManager().install()

browser = webdriver.Chrome(service = ChromeService(webdriver_manager_directory), options=chrome_options)                        # - chrome browser 열기

# Chrome WebDriver의 capabilities 속성 사용
capabilities = browser.capabilities

pass
browser.get("https://www.jobkorea.co.kr/recruit/joblist?menucode=local&localorder=1#anchorHRCnt_4")                                     # - 주소 입력

                                                    # - 가능 여부에 대한 OK 받음
pass
html = browser.page_source                          # - html 파일 받음(and 확인)
# print(html)

from selenium.webdriver.common.by import By          # - 정보 획득
# browser.save_screenshot('./formats.png')           
region_choice1_button = browser.find_element(by=By.CSS_SELECTOR,value="#devSearchForm > div.detailArea > div > div:nth-child(1) > dl.loc.circleType.dev-tab.dev-local.on > dd.ly_sub > div.ly_sub_cnt.colm2-ty2.clear > dl.detail_sec.barType > dd > div.nano-content.dev-main > ul > li:nth-child(1)")                       # 로그인 버튼 정보 수집
region_choice1_button.click()          
region_choice1_button = browser.find_element(by=By.CSS_SELECTOR,value="#devSearchForm > div.detailArea > div > div:nth-child(1) > dl.loc.circleType.dev-tab.dev-local.on > dd.ly_sub > div.ly_sub_cnt.colm2-ty2.clear > dl.detail_sec.barType > dd > div.nano-content.dev-main > ul > li:nth-child(2)")                       # 로그인 버튼 정보 수집
region_choice1_button.click()          
region_choice1_button = browser.find_element(by=By.CSS_SELECTOR,value="#devCndtDispArea > div > dl.listWrap.clear > dd.btnSet")                       # 로그인 버튼 정보 수집
region_choice1_button.click()          
time.sleep(5)
for i in range():
    pass

browser.quit()                                      # - 브라우저 종료
