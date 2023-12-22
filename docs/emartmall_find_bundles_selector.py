# https://emart.ssg.com/disp/category.ssg?dispCtgId=6000214033

# * 웹 크롤링 동작
from selenium import webdriver 

# ChromeDriver 실행
browser = webdriver.Chrome()                        # - chrome browser 열기

pass
browser.get("https://emart.ssg.com/disp/category.ssg?dispCtgId=6000214033")           # - 주소 입력

                                                    # - 가능 여부에 대한 OK 받음
pass

from selenium.webdriver.common.by import By

## 여러 개 elements 정보 가져오기
selector_value = "div.mnemitem_unit"
elements_bundle = browser.find_elements(by=By.CSS_SELECTOR,value = selector_value)            # - 정보 획득

for element_item in elements_bundle[10:41]: # list slicing
    # print(element_item.text) # 상품 정보들
    # 상품 제목
    element_title = element_item.find_element(by=By.CSS_SELECTOR,value = "span.mnemitem_goods_tit")
    title = element_title.text
    # 상품 판매 원가

    try:
        element_old_price = element_item.find_element(by=By.CSS_SELECTOR, value = "div > del > em")
        old_price = element_old_price.text
        pass
    except:
        old_price = ""
        pass
    finally:
        pass
    print("title : {},old price: {}".format(title,old_price))
    pass
pass


browser.quit()                                      # - 브라우저 종료
