# * 웹 크롤링 동작
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
webdriver_manager_directory = ChromeDriverManager().install()
import time


# browser 열기
browser = webdriver.Chrome(service=ChromeService(webdriver_manager_directory))


# Chrome WebDriver의 capabilities 속성 사용
capabilities = browser.capabilities

# 주소 입력
browser.get("https://pedia.watcha.com/ko-KR/contents/mQO8b5R/comments/")

# - 가능 여부에 대한 OK 받음
pass

# - html 파일 받음(and 확인)
# html = browser.page_source
# print(html)

# - 정보 획득
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

## 한 페이지씩 이동
element_body = browser.find_element(by=By.CSS_SELECTOR, value="body")

previous_scrollHeight = 0
name_list = []
score_list = []
content_list = []

# while True :
for x in [1,2,3,4,5,6]:
    element_body.send_keys(Keys.END)

    # current_scrollHeight = browser.execute_script("return document.body.scrollHeight")
    # if previous_scrollHeight >= current_scrollHeight :
    #     break
    # else :
    #     previous_scrollHeight = current_scrollHeight
    # time.sleep(1)
    # pass
list_count_comments = browser.find_elements(by=By.CSS_SELECTOR, value="div.css-13j4ly.egj9y8a4")

# comment 개수만큼 for문 반복
for count_comment in list_count_comments :
    try :
        element_name = count_comment.find_element(by=By.CSS_SELECTOR, value="div.css-eldyae.e10cf2lr1")
        name = element_name.text
        name_list.append(name)
    except :
        name_list.append("")

    try :
        element_score = count_comment.find_element(by=By.CSS_SELECTOR, value="div.css-31ods0.egj9y8a0")
        score = element_score.text
        score_list.append(score)
    except :
        score_list.append("")
    try :
        element_content = count_comment.find_element(by=By.CSS_SELECTOR, value="div.css-10w4kfx.e1hvy88212")
        content = element_content.text
        content_list.append(content)
    except :
        content_list.append("")

for i in range(len(list_count_comments)) :
    print(name_list[i],score_list[i],content_list[i])
# mongodb에 접속하기 위한 function
def mongo_connect() :          
    from pymongo import MongoClient   
    mongoClient = MongoClient("mongodb://localhost:27017")     
    database = mongoClient["gatheringdatas"]     
    collection = database["watcha_comments"]         
    return collection 

watcha_comments=mongo_connect()
for i in range(len(list_count_comments)) :
    watcha_comments.insert_one({"name":name_list[i], "score":score_list[i], "content":content_list[i]})



# 브라우저 종료
browser.quit()


