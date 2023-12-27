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
browser.get("https://www.11st.co.kr/products/5462977259?&trTypeCd=PW24&trCtgrNo=1001480&lCtgrNo=1001336&mCtgrNo=1001480")                                     # - 주소 입력

                                                    # - 가능 여부에 대한 OK 받음
pass
html = browser.page_source                          # - html 파일 받음(and 확인)
# print(html)
from selenium.webdriver.common.by import By          # - 정보 획득
# browser.save_screenshot('./formats.png')           
from selenium.webdriver.common.keys import Keys
browser.switch_to.frame('ifrmReview')                                                       # ifrmReview frame으로 변경
element_body = browser.find_element(by=By.CSS_SELECTOR,value="body")
previous_scrollHeight = 0                                                                   # 기본 브라우저 높이 변수 지정
time.sleep(3)
while True:
    try:                                                                                                         # 더보기 버튼 클릭 시도
        element_click = browser.find_element(by=By.CSS_SELECTOR,value = "#review-list-page-area > div > button") # 더보기 버튼 정보 추출
        element_click.click()                                                                                    # 더보기 버튼 클릭
        current_scrollHeight = browser.execute_script("return document.body.scrollHeight")
    except:                                                                                                      # 더보기 버튼 없을 시 반복문 종료
        break
    time.sleep(3)
    pass
pass
from pymongo import MongoClient                                                                                     # DB에 접속
mongo_client = MongoClient("mongodb://localhost:27017")
database = mongo_client["gatheringdatas"]
collection = database["11st_comments"]                                                                             
collection.delete_many({})                                                                                      
element_box = browser.find_elements(by=By.CSS_SELECTOR,value="#review-list-page-area > ul > li")                    # 리뷰 박스 추출
for elements in element_box:                                                                                        
    try:                                                                                                            # 내용 더보기 버튼이 있을 경우 클릭
        more_contents = elements.find_element(by=By.CSS_SELECTOR,value="#review-list-page-area > ul > li > div > div > div.cont_text_wrap > p.cont_btn.review-expand > button.c_product_btn.c_product_btn_more6.review-expand-open-text")
        more_contents.click()
    except:                                                                                                         # 없을 경우 패스
        pass
    try:                                                                                                            # 입력자 이름 추출
        user_name = elements.find_element(by=By.CSS_SELECTOR,value="#review-list-page-area > ul > li > dl > dt")
        user_name = user_name.text
    except:                                                                                                         # 없을 경우 공백 입력
        user_name = ""
    try:                                                                                                            # 선택 사항 추출
        choice_option = elements.find_element(by=By.CSS_SELECTOR,value="#review-list-page-area > ul > li > div > dl > div > dd")
        choice_option = choice_option.text
    except:                                                                                                         # 없을 경우 공백 입력
        try: 
            choice_option = elements.find_element(by=By.CSS_SELECTOR,value="#review-list-page-area > ul > li > div > p.option")
            str_choice_option = choice_option.text
            choice_option = str_choice_option.replace("선택 옵션 ","")      
        except:
            choice_option = ""                                                                                          
    try:                                                                                                            # 평점 추출
        rating = elements.find_element(by=By.CSS_SELECTOR,value="#review-list-page-area > ul > li > div > p.grade > span > em")
        rating = rating.text
    except:                                                                                                         # 없을 경우 공백 입력
        rating = ""                                                                                                 
    try:                                                                                                            # 내용 추출
        content = elements.find_element(by=By.CSS_SELECTOR,value="#review-list-page-area > ul > li > div > div > div.cont_text_wrap > p")
        content = content.text      
    except:                                                                                                         # 없을 경우 공백 입력
        content = ""                                                                                                
    pass
    collection.insert_one({"작성자": user_name,                                                                     # db에 전송
                           "선택 옵션": choice_option,
                           "별점": rating,
                           "내용": content})
    pass
pass
browser.quit()                                      # - 브라우저 종료
