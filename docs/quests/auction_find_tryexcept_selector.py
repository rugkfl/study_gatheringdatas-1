# 상품 item: #itembest_T > ul.uxb-img.first > li.first > div > div.info
# 상품 제목: #itembest_T > ul.uxb-img.first > li.first > div > div.info > em > a
# 판매원가: #itembest_T > ul.uxb-img.first > li.first > div > div.info > ul > li.c_price > span
# 변경가격: #itembest_T > ul.uxb-img.first > li.first > div > div.info > ul > li.d_price > span.sale
# All skill : #itembest_T > ul:nth-child(5) > li:nth-child(2) > div > div.info > div.icon > div > div.icons.ic_allkill
# free_delivery : #itembest_T > ul:nth-child(5) > li:nth-child(2) > div > div.info > div.icon > div > div.icons.ic_free
# smiledelivery : #itembest_T > ul:nth-child(5) > li:nth-child(2) > div > div.info > div.icon > div > div.icons.ic_smiledelivery
# freebie : #itembest_T > ul:nth-child(20) > li:nth-child(3) > div > div.info > div.icon > div > div.icons.ic_freebie

# * 웹 크롤링 동작
from selenium import webdriver 

# ChromeDriver 실행
browser = webdriver.Chrome()                        # - chrome browser 열기

pass
browser.get("https://corners.auction.co.kr/corner/categorybest.aspx")           # - 주소 입력

pass
html = browser.page_source                          # - html 파일 받음(and 확인)

from selenium.webdriver.common.by import By
selector_value = "div.info"
elements_bundle = browser.find_elements(by=By.CSS_SELECTOR,value = selector_value)            # - 정보 획득

for element_item in elements_bundle:
    try:
        elements_title = element_item.find_element(by=By.CSS_SELECTOR,value = "em > a")                                 # 타이틀 정보 수집
        title = elements_title.text
    except:
        title = ""                                                                                                      # 오류 시 빈칸 입력
    try:
        elements_old_price = element_item.find_element(by=By.CSS_SELECTOR,value = "li.c_price > span")                  # 원가 정보 수집
        old_price= elements_old_price.text    
    except:
        old_price = ""                                                                                                 # 오류 시 빈칸 입력
    try:
        elements_sale_price = element_item.find_element(by=By.CSS_SELECTOR,value = "li.d_price > span.sale")           # 변경 가격 정보 수집
        sale_price = elements_sale_price.text
    except:
        sale_price = ""                                                                                               # 오류 시 빈칸 입력
    
    delivery = []                                                                                                     # 배송 방법 리스트 지정
    try:
        elements_delivery = element_item.find_element(by = By.CSS_SELECTOR,value = "div.icons.ic_allkill")            # allkill 정보 수집
        delivery.append(elements_delivery.text)                                                                       # 배송 방법 리스트에 추가
    except:
        pass
    try:
        elements_delivery = element_item.find_element(by = By.CSS_SELECTOR,value = "div.icons.ic_free")               # 무료 배송 정보 수집
        delivery.append(elements_delivery.text)                                                                       # 배송 방법 리스트에 추가
    except:
        pass
    try:
        elements_delivery = element_item.find_element(by = By.CSS_SELECTOR,value = "div.icons.ic_smiledelivery")     # 스마일 배송 정보 수집
        delivery.append(elements_delivery.text)                                                                      # 배송 방법 리스트에 추가
    except:
        pass
    try:
        elements_delivery = element_item.find_element(by = By.CSS_SELECTOR,value = "div.icons.ic_freebie")           # 사은품 정보 수집
        delivery.append(elements_delivery.text)                                                                      # 배송 방법 리스트에 추가
    except:
        pass
    pass
    print("title : {}, old_price : {}, sale_price : {}, ".format(title,old_price,sale_price), end= "")              # 상품 제목, 원가, 변경 가격 출력
    print("delivery : ", end ="")
    for i in range(len(delivery)):
        print("{}" .format(delivery[i]), end=" ")                                                                   # 배송 방법 출력 
    print("")


browser.quit()                                      # - 브라우저 종료
