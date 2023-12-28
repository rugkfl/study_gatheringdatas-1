
        # * 웹 크롤링 동작
from selenium import webdriver 
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
import time
from selenium.webdriver.common.by import By     
from selenium.webdriver.chrome.options import Options

webdriver_manager_directory = ChromeDriverManager().install()
# ChromeDriver 실행                        
# Chrome 브라우저 옵션 생성
chrome_options = Options()
# User-Agent 설정
chrome_options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36")
# WebDriver 생성
browser = webdriver.Chrome(service = ChromeService(webdriver_manager_directory), options=chrome_options)                        # - chrome browser 열기
# Chrome WebDriver의 capabilities 속성 사용
capabilities = browser.capabilities

browser.get("https://www.courtauction.go.kr/")                                     # - 주소 입력
html = browser.page_source                          # - html 파일 받음(and 확인)
def dbmongo(client,Database,Collection):
    from pymongo import MongoClient                                                                                     # DB에 접속
    mongo_client = MongoClient(client)
    database = mongo_client[Database]
    collection = database[Collection]        
    collection.delete_many({}) 
    return  collection

def quest(collection):
    browser.switch_to.frame("indexFrame")                                                                   # frame 안으로 이동
    browser.find_element(by=By.CSS_SELECTOR,value = "#menu > h1:nth-child(5) > a").click()                  # 물건상세검색 페이지 이동
    court_options = browser.find_elements(by=By.CSS_SELECTOR,value="#idJiwonNm > option")                   # selector의 option들 찾기
    value_list = []                                                                                         # selector list 작성
    for option in court_options:
        court_option = option.get_attribute('value')                                                        # selector의 value 값 가져오기
        value_list.append(court_option)                                                                     # value_list에 value값
    pass
    for i in (1,2,0):
        element_range = browser.find_element(by=By.CSS_SELECTOR, value="#idJiwonNm")                       # 법원 selector find
        Select(element_range).select_by_value(value_list[i])                                               # 법원 선택
        browser.find_element(by=By.CSS_SELECTOR,value = "#contents > form > div.tbl_btn > a:nth-child(1)").click() # 검색 버튼 클릭
        time.sleep(2)
        for j in (2,4,5,6,7,8,9,10,11):                                                                    # 10페이지까진 반복
            item_info_list = browser.find_elements(by=By.CSS_SELECTOR,value="form:nth-child(1) > table > tbody > tr")       
            for item_info in item_info_list:
                try:
                    item_number = item_info.find_element(by=By.CSS_SELECTOR,value="td:nth-child(2)").text # 법원 이름과 사건 번호 찾기
                    list_item_number = item_number.split("\n")
                    court_name = list_item_number[0]                                                       #법원 이름 변수 지정
                    str_item_number = list_item_number[1]                                                  # 사건 번호 변수 지정
                    for i in range(len(list_item_number)-2):
                        str_item_number = str_item_number + ", " + list_item_number[i+2]
                    list_item_contents = item_info.find_elements(by=By.CSS_SELECTOR,value=" td:nth-child(4) > div")
                    for i in range(len(list_item_contents)):
                        dic_item_contents = list_item_contents[i].text                                    # 소재지와 내역 찾기
                        item_contents = dic_item_contents.split("\n")
                        item_region = item_contents[0]                                                   # 소재지 변수 지정
                        item_content = item_contents[1]                                                  # 내역 변수 지정
                        collection.insert_one({"법원 소재지": court_name,
                                            "사건 번호": str_item_number,
                                            "소재지": item_region,
                                            "내역": item_content})
                except:
                    pass
            try:    
                page_value = "div > div.page2 > a:nth-child({})".format(j)
                browser.find_element(by=By.CSS_SELECTOR,value = page_value).click()
            except:
                pass
                break
            pass
        pass
        browser.find_element(by=By.CSS_SELECTOR,value = "form:nth-child(1) > div > div > a:nth-child(5)").click()
        time.sleep(2)    
        pass
    browser.quit()                                      # - 브라우저 종료



 


collection = dbmongo("mongodb://localhost:27017","gatheringdatas","courts")
quest(collection)