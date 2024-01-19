# 데이터명 : 한국주택금융공사_전세자금대출 금리 정보
# from https://www.data.go.kr/iim/api/selectAPIAcountView.do
import requests 

# # url 주소 변수 지정
# url = 'http://apis.data.go.kr/B551408/rent-loan-rate-info/rate-list'

# ## parameters 변수 지정
# params = {'serviceKey':'ow0djIIbtYKcXjahX81pjlVfuA8kUj6DBQkALWCEeCXNuir3R0%2BLMOTTuhmW9Ms7R%2FAVfqb7cGIAazhHFttnPw%3D%3D',
#           'pageNo':1,
#           'numOfRows':30,
#           'dataType':'JSON'
#           }

# # url과 parameters를 response라는 변수로 받음 
# response = requests.get(url, params=params) 

# url 주소에 parameters가 들어간 링크를 변수로 지정
url = 'http://apis.data.go.kr/B551408/rent-loan-rate-info/rate-list?serviceKey=ow0djIIbtYKcXjahX81pjlVfuA8kUj6DBQkALWCEeCXNuir3R0%2BLMOTTuhmW9Ms7R%2FAVfqb7cGIAazhHFttnPw%3D%3D&pageNo=1&numOfRows=30&dataType=JSON'

# respose라는 변수로 받음
response = requests.get(url) 

# response의 내용을 출력
print(response.content) 

pass