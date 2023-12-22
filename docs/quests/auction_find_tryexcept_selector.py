
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
        print("title : {}".format(title), end = "")                                                                     # 제품 제목 출력
    except:
        print("", end = "")                                                                                                      # 오류 시 빈칸 입력
    try:
        elements_old_price = element_item.find_element(by=By.CSS_SELECTOR,value = "li.c_price > span")                  # 원가 정보 수집
        old_price= elements_old_price.text
        print(", old_price : {}".format(old_price), end = "")                                                           # 원가 출력
    except:
        pass                                                                                                           # 오류 시 빈칸 입력
    try:
        elements_sale_price = element_item.find_element(by=By.CSS_SELECTOR,value = "li.d_price > span.sale")           # 변경 가격 정보 수집
        price = elements_sale_price.text
        print(", price : {}".format(price), end = "")                                                                  # 변경 가격 출력
    except:
        pass                                                                                                            # 오류 시 빈칸 입력
    
    delivery_bundle = []
    elements_delivery = element_item.find_elements(by = By.CSS_SELECTOR,value = "div.icon > div > div > span")     # 배송 방법 정보 수집
    for i in range(len(elements_delivery)):
        delivery_bundle.append(elements_delivery[i].text)
    if len(delivery_bundle) > 0:
        delivery_list = ", ".join(delivery_bundle)
        print(", delivery : {}".format(delivery_list))                                                             # 배송 방법 출력 
    else:
        print("")
        pass
    pass
   
# delivery = element_delivery.text.split() 이렇게 하면 값이 두개가 되므로 자연스럽게 리스트로 구성됨 
# delivery_result = ','.join(delivery)    이렇게 하면 리스트 사이에만 ','가 입력됨 

browser.quit()                                      # - 브라우저 종료
