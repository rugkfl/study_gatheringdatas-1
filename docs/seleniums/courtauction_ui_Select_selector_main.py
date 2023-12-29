import courtauction_ui_Select_selector_subfunction as subfuction
def main(): # self 키워드 필요 (class 소속 확인용)
    try: 
        uri = "https://www.courtauction.go.kr/"
        browser = subfuction.getBrowserFromURI(uri)
        court_count = subfuction.selectCourts(browser)
        print("court count : ".format(court_count))
        pass        # 업무 코드
    except:
        pass        # 업무 코드 문제 발생 시 대처 코드
    finally:
        subfuction.quitBrowser(browser)       # try나 except이 끝난 후 무조건 실행 코드
    pass    # 내용 넣기
    return 0

if __name__ == "__main__":
    try: 
        main()        # 업무 코드
    except:
        pass        # 업무 코드 문제 발생 시 대처 코드
    finally:
        pass        # try나 except이 끝난 후 무조건 실행 코드

    pass

