import courtauction_ui_Select_selector_subfunction as subfunction
# 기본 function 형식 - 기다림. 불릴 때 기능
def main() :  
    try :
        uri = "https://www.courtauction.go.kr/"
        browser = subfunction.getBrowserFromURI(uri)
        court_count = subfunction.selectCourts(browser=browser)
        print("court count : {}".format(court_count))
    except :
        pass  # 업무 코드 문제 발생 시 대처 코드
    finally :
       
        subfunction.quitBrowser(browser=browser)

if __name__ == "__main__" :
    try :
        main() # 업무 코드
    except :
        pass  # 업무 코드 문제 발생 시 대처 코드
    finally :
        pass # try