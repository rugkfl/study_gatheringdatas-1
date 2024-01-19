# 데이터명 : 한국주택금융공사_전세자금대출 금리 정보
# from https://www.data.go.kr/iim/api/selectAPIAcountView.do
import requests 

# url 주소 변수 지정
url = 'http://apis.data.go.kr/B551408/rent-loan-rate-info/rate-list'

## parameters 변수 지정
params1 = {'serviceKey':'ow0djIIbtYKcXjahX81pjlVfuA8kUj6DBQkALWCEeCXNuir3R0%2BLMOTTuhmW9Ms7R%2FAVfqb7cGIAazhHFttnPw==',
          'pageNo':1,
          'numOfRows':30,
          'dataType':'JSON'
          }

# url과 parameters를 response라는 변수로 받음 
response = requests.get(url, params=params1) 

# # url 주소에 parameters가 들어간 링크를 변수로 지정
# url = 'http://apis.data.go.kr/B551408/rent-loan-rate-info/rate-list?serviceKey=ow0djIIbtYKcXjahX81pjlVfuA8kUj6DBQkALWCEeCXNuir3R0%2BLMOTTuhmW9Ms7R%2FAVfqb7cGIAazhHFttnPw%3D%3D&pageNo=1&numOfRows=30&dataType=JSON'

# # respose라는 변수로 받음
# response = requests.get(url) 

# response의 내용을 출력
print(response.content) 

# json 파일을 dictionary 형태로 변환
import json
contents = json.loads(response.content)
pass

type(contents)
# <class 'dict'>

contents['header']
# {'resultCode': '00', 'resultMsg': '정상'}

contents['header']['resultCode']
# '00'

contents['body']
# {'pageNo': 1, 'totalCount': 18, 'numOfRows': 30, 'items': [{...}, {...}, {...}, {...}, {...}, {...}, {...}, {...}, {...}, ...]}

contents['body']['items'][0]
# {'bssYmdStart': '20240108', 'interest4_1': '0', 'interest3_2': '0', 'interest4_2': '0', 'interest2_1': '0', 'interest1_2': '0', 'interest3_1': '0', 'interest2_2': '0', 'interest1_1': '0', 'bssYmdEnd': '20240114', 'organId': '산업은행', 'callCenter': '1588-1500'}

# mongoDB 저장
from pymongo import MongoClient
# mongodb에 접속 -> 자원에 대한 class
mongoClient = MongoClient("mongodb://localhost:27017")
# database 연결
database = mongoClient["data_go_kr"]
# collection 작업
collection = database['rent-loan-rate-info_rate-list']
# insert 작업 진행
result = collection.insert_many(contents['body']['items'])