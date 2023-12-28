# * 웹 크롤링 동작
from selenium import webdriver 
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
webdriver_manager_directory = ChromeDriverManager().install()
import time
# ChromeDriver 실행
from selenium.common.exceptions import NoSuchElementException
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
url = 'https://www.11st.co.kr/browsing/DealBest.tmall?method=getShockingDealBestMain'
browser.get(url)                                     # - 주소 입력

                                                    # - 가능 여부에 대한 OK 받음
pass
html = browser.page_source                          # - html 파일 받음(and 확인)
# print(html)
from pymongo import MongoClient
mongoclient = MongoClient('mongodb://localhost:27017')
database = mongoclient["gatheringdatas"]
collection_item = database["11st_item"]
collection_item.delete_many({})
collection_comments = database["11st_item_comments"]
collection_comments.delete_many({})

from selenium.webdriver.common.by import By          # - 정보 획득
for i in range(4):
    companies = browser.find_elements(by=By.CSS_SELECTOR, value= "div.viewtype.catal_ty > ul > li > div > a")                   # 제품 찾기
    company = companies[i]
    company.click()                                                                                                             # 제품 클릭
    time.sleep(2)
    try:
        element_title = browser.find_element(by=By.CSS_SELECTOR,value = "div.l_product_side_info > div> h1").text              # 제품명 찾기
    except NoSuchElementException:
        element_title = "" 
    try:
        img_element = browser.find_element(by=By.CSS_SELECTOR,value = "#productImg > div > img")                               # 제품 사진 링크 찾기
        element_img = img_element.get_attribute('src')
    except NoSuchElementException:
        element_img = ""
    try:
        element_price_regular = browser.find_element(by=By.CSS_SELECTOR,value = "div:nth-child(1) > dd > del").text           # 원가 찾기
    except NoSuchElementException:
        element_price_regular = ""
    try:
        str_element_price_sale = browser.find_element(by=By.CSS_SELECTOR,value = "div.price_info > dd.price > strong > span.value").text  # 판매가 찾기
        element_price_sale = ("{}원".format(str_element_price_sale))
    except NoSuchElementException:
        element_price_sale = ""
    try:
        element_item_content_name = browser.find_elements(by=By.CSS_SELECTOR,value = "#tabpanelDetail1 > table > tbody > tr > th")  # 상품정보 제목 찾기
        element_item_content = browser.find_elements(by=By.CSS_SELECTOR,value = "#tabpanelDetail1 > table > tbody > tr > td")  # 상품정보 내용 찾기
        element_item_contents={}
        for j in range(len(element_item_content_name)):                                                                         # 상품 정보의 제목과 내용을 dictionary 지정
            element_item_contents[element_item_content_name[j].text] = element_item_content[j].text
        pass
    except NoSuchElementException:
        element_price_content = ""
    collection_item.insert_one({"상품명": element_title,                                                                        # DB 전송
                           "이미지 링크": element_img,
                           "원가": element_price_regular,
                           "판매가": element_price_sale})
    collection_item.update_one({"상품명": element_title},{"$set":element_item_contents},upsert=True)                        # 상품 정보 dictionary DB에 추가
    pass
    browser.switch_to.frame('ifrmReview')                                                       # ifrmReview frame으로 변경
    element_body = browser.find_element(by=By.CSS_SELECTOR,value="body")
    previous_scrollHeight = 0                                                                   # 기본 브라우저 높이 변수 지정
    time.sleep(3)
    # while True:
    for j in range(1):
        try:                                                                                                         # 더보기 버튼 클릭 시도
            element_click = browser.find_element(by=By.CSS_SELECTOR,value = "#review-list-page-area > div > button") # 더보기 버튼 정보 추출
            element_click.click()                                                                                    # 더보기 버튼 클릭
            current_scrollHeight = browser.execute_script("return document.body.scrollHeight")
        except:                                                                                                      # 더보기 버튼 없을 시 반복문 종료
            break
        time.sleep(3)
        pass
    pass
                                                                      
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
        element_id = collection_item.find({},{"_id":1})[i]["_id"]                                                    # 상품 id 가져오기

        pass

        collection_comments.insert_one({"상품 ID": element_id,                                                           # db에 전송
                                        "상품명": element_title,
                                        "작성자": user_name,                                                                    
                            "선택 옵션": choice_option,
                            "별점": rating,
                            "내용": content})
    pass
    browser.back()                  # 제품 리스트로 이동
    time.sleep(2)                      # 
    pass
pass

browser.quit()                                      # - 브라우저 종료
