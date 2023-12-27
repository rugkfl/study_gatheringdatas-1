# * 웹 크롤링 동작
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
browser.get("https://www.11st.co.kr/products/pa/5872814954?inpu=&trTypeCd=22&trCtgrNo=895019")
# - 가능 여부에 대한 OK 받음
pass
# - 정보 획득
from selenium.webdriver.common.by import By
# 리뷰 버튼 클릭
elements_click = browser.find_element(by=By.CSS_SELECTOR, value="#tabMenuDetail2").click()
# iframe으로 전환
browser.switch_to.frame('ifrmReview')
time.sleep(2)
review_list = browser.find_elements(by=By.CSS_SELECTOR, value="li.review_list_element")
pass
# 사용자 이름
try :
    element_name = browser.find_elements(by=By.CSS_SELECTOR, value="ul.area_list > li.review_list_element >dl.c_product_reviewer >dt.name")
    name_list = []
    for i in range(len(review_list)):
        name_list.append(element_name[i].text)
except :
    name_list = []
    for i in range(len(review_list)):
        name_list.append("")
# 옵션 선택
try :
    element_option = browser.find_elements(by=By.CSS_SELECTOR, value="#review-list-page-area > ul > li > div > div > div.value")
    option_list = []
    for i in range(len(review_list)):
        option_list.append(element_option[i].text)
except :
    option_list = []
    for i in range(len(review_list)):
        option_list.append("")
# 별점
try :
    element_score = browser.find_elements(by=By.CSS_SELECTOR, value="li.review_list_element > div > p.grade > span > em")
    score_list = []
    for i in range(len(review_list)):
        score_list.append(element_score[i].text)
except :
    score_list = []
    for i in range(len(review_list)):
        score_list.append("")
# 내용 더보기 클릭 후 작성 내용 보기
content_list = []
for i in range(len(review_list)) :
    try :
        browser.find_element(by=By.CSS_SELECTOR, value="li.review_list_element  > div > div > div.cont_text_wrap > p.cont_btn.review-expand > button").click()  # 리뷰 내용 클릭(한번만 수행)
        element_content = browser.find_elements(by=By.CSS_SELECTOR, value= "div.cont_text_wrap") # 리뷰 내용 찾기
        # 현재 리뷰에 대한 내용을 리스트에 추가
        content_list.append(element_content[i].text)
    except :
           content_list.append("")
pass
# mongodb 접속하기 위한 function
def mongo_connect():
    from pymongo import MongoClient
    mongoClient = MongoClient("mongodb://localhost:27017")
    database = mongoClient["gatheringdatas"]
    collection = database["eleven_comments"]
    return collection
review_comments=mongo_connect()
for i in range(len(review_list)):
    review_comments.insert_one({"name":name_list[i], "option":option_list[i], "score":score_list[i], "content":content_list[i]})
    pass
# 브라우저 종료
browser.quit()