# * 웹 크롤링 동작
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
webdriver_manager_directory = ChromeDriverManager().install()
browser = webdriver.Chrome(service=ChromeService(webdriver_manager_directory))
import time


# - 주소 입력
url = "https://deal.11st.co.kr/browsing/DealAction.tmall?method=getShockingDealMain"
browser.get(url)


from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# click product

for i in [1,2,4] :
    browser.find_element(by=By.CSS_SELECTOR, value="#layBody > section:nth-child(3) > div.c_list_card.c_list_card_collection.col_4 > ul > li:nth-child({}) > div > a".format(i+1)).click()

    # 제품명
    element_product_name = browser.find_element(by=By.CSS_SELECTOR, value="#layBodyWrap > div > div.s_product.s_product_detail > div > div > div.l_product_view_wrap > div.l_product_summary.l_product_summary_amazon.notranslate > div.l_product_side_info > div.c_product_info_title > h1").text
    print(element_product_name)

    # 이미지 링크
    element_image = browser.find_element(by=By.CSS_SELECTOR, value="#layBodyWrap > div > div.s_product.s_product_detail > div > div > div.l_product_view_wrap > div.l_product_summary.l_product_summary_amazon.notranslate > div.l_product_side_view > div.c_product_view_img > div.img_full.img_full_height > img").get_attribute('src')
    print(element_image)

    # 상품 판매 원가
    element_old_price = browser.find_element(by=By.CSS_SELECTOR, value="#layBodyWrap > div > div.s_product.s_product_detail > div > div > div.l_product_view_wrap > div.l_product_summary.l_product_summary_amazon.notranslate > div.l_product_side_info > div.b_product_info_price.b_product_info_price_style2 > div.c_prd_price.c_product_price_basic > div.price_block > dl > div:nth-child(1) > dd > del").text
    print(element_old_price)

    # 상품 변경가격
    element_new_price = browser.find_element(by=By.CSS_SELECTOR, value="#layBodyWrap > div > div.s_product.s_product_detail > div > div > div.l_product_view_wrap > div.l_product_summary.l_product_summary_amazon.notranslate > div.l_product_side_info > div.b_product_info_price.b_product_info_price_style2 > div.c_prd_price.c_product_price_basic > div.price_block > dl > div:nth-child(2) > dd.price > strong").text
    print(element_new_price)

    # 상품 설명
    element_product_content = browser.find_element(by=By.CSS_SELECTOR, value="#tabpanelDetail1 > div.prodc_cont_amazon > div.cont_detail > div:nth-child(4)").text
    print(element_product_content)

        # # iframe 으로 전환
    element_body = browser.find_element(by=By.CSS_SELECTOR, value="body")
    # element_body.send_keys(Keys.END)
    # element_body.send_keys(Keys.PAGE_UP)
    element_body.send_keys(Keys.PAGE_DOWN)
    element_body.send_keys(Keys.PAGE_DOWN)

    pass
    
    pass
    time.sleep(2)
    browser.find_element(by=By.CSS_SELECTOR, value="#tabMenuDetail2").click()
    browser.switch_to.frame("ifrmReview")
    pass
    
    time.sleep(3)
    browser.find_element(by=By.CSS_SELECTOR, value="body")
    # 더보기 클릭
    # while True :
    for i in range(4):
        try :
            browser.find_element(by=By.CSS_SELECTOR, value="#review-list-page-area > div > button").click()
            time.sleep(2)
        except :
            break


    review_list = browser.find_elements(by=By.CSS_SELECTOR, value="#review-list-page-area > ul.area_list>li.review_list_element")

    # 리스트
    option_list = []
    name_list = []
    score_list = []
    content_list = []


    # for i in review_list:
    # 사용자 이름
    try :
        element_name = browser.find_elements(by=By.CSS_SELECTOR, value="ul.area_list > li.review_list_element >dl.c_product_reviewer >dt.name")
        for j in element_name:
            name=j.text

            name_list.append(name)
    except :      
        name_list.append("")
    pass


    # 옵션 선택
    try:
        element_option = browser.find_elements(by=By.CSS_SELECTOR, value="div.c_product_review_cont > dl.option_set > div.option")
        for j in element_option :
            option=j.text

            option_list.append(option)
        pass
    except:
        option_list.append("")
        pass            
    try:
        element_option = browser.find_elements(by=By.CSS_SELECTOR, value="div.c_product_review_cont > p.option")
        for j in element_option :
            option=j.text
        
            option_list.append(option)
    except:
        option_list.append("")
        pass


    # 별점
    try :
        element_score = browser.find_elements(by=By.CSS_SELECTOR, value="li.review_list_element > div > p.grade > span > em")
        for j in element_score :
            score = j.text
            score_list.append(score)
    except :
        score_list.append("")
    
    
    # 리뷰 내용
    try :
        element_content = browser.find_elements(by=By.CSS_SELECTOR, value="div > div > div.cont_text_wrap>p")
        for j in element_content :
            content = j.text
            content_list.append(content)
    except :
        content_list.append("")
    print(name_list)
    print(option_list)
    print(score_list)
    print(content_list)

    browser.get(browser.current_url)
    browser.find_element(by=By.CSS_SELECTOR, value="#gnb > div > div.b_header_util > div > div.c_util_servicelink > ul:nth-child(2) > li:nth-child(2) > a").click()

    
    time.sleep(3)

    # mongodb 접속하기 위한 function
    def mongo_connect():
        from pymongo import MongoClient
        mongoClient = MongoClient("mongodb://localhost:27017")     
        database = mongoClient["gatheringdatas"]     
        collection = database["review_comments"]         
        return collection 

    item_comments=mongo_connect()
    for i in range(len(review_list)):
        try:
            data={"name":name_list[i], "option":option_list[i], "score":score_list[i], "content":content_list[i]}
        except:
            data={"name":name_list[i], "option":" ", "score":score_list[i], "content":content_list[i]}

        item_comments.insert_one(data)
        pass

    def mongo_connect_second():
        from pymongo import MongoClient
        mongoClient = MongoClient("mongodb://localhost:27017")     
        database = mongoClient["gatheringdatas"]     
        collection = database["item_comments"]         
        return collection

    review_comments=mongo_connect_second()
    review_comments.insert_one({"product_name":element_product_name, "image_link":element_image, "old_price":element_old_price, "new_price":element_new_price, "product_content":element_product_content})


pass 
# 브라우저 종료
browser.quit()