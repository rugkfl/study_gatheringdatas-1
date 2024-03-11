# * 웹 크롤링 동작
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
webdriver_manager_directory = ChromeDriverManager().install()
browser = webdriver.Chrome(service=ChromeService(webdriver_manager_directory))

browser.get("https://corners.auction.co.kr/corner/categorybest.aspx")

pass

from selenium.webdriver.common.by import By
selector_value = "div.info"
element_bundle = browser.find_elements(by=By.CSS_SELECTOR, value=selector_value)


for element_item in element_bundle: # list slicing
    # print(element_item.text) # 상품 정보들
    # 상품 제목
    element_title = element_item.find_element(by=By.CSS_SELECTOR, value="em")
    title= element_title.text
    # 상품 판매 원가(try-except)
    try :
        element_old_price = element_item.find_element(by=By.CSS_SELECTOR, value="span.cost")
        old_price = element_old_price.text

    except :
        old_price = ""
        pass
    finally :
        pass

    # 상품 변경가격
    try :
        element_new_price = element_item.find_element(by=By.CSS_SELECTOR, value="span.sale")
        new_price = element_new_price.text
    except :
        new_price = ""
    finally:
        pass

    # 배송방법

    try :
        element_delivery = element_item.find_element(by=By.CSS_SELECTOR, value="div.icon")
        delivery = element_delivery.text
    except :
        delivery = ""
    finally :
        delivery = delivery.split() # delivery list화
    

    # print("title : {}, old price : {}, new price : {}, delivery : {}".format(title, old_price, new_price, delivery))
    print("""
    title : {}
    old price : {}
    new price : {}
    delivery : {}
    """.format(title, old_price, new_price, delivery))
    

pass
# 브라우저 종료
browser.quit()