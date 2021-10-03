'''
웹 스크래핑
url 로 부터 제목과 상단 첫 이미지 등 web index data mining 
'''

'''
페이지 몇개인지 알아야함 한페이지당 몇개의 글을 볼건지
마지막 페이지 알아야함
indeed 11page 50
stack 
4.10.0
'''
## requset 2 라이브러리 
import requests  ## 2.26.0
from bs4 import BeautifulSoup
indeed_result = requests.get("http://www.indeed.com/jobs?q=python&limit=50")

# print(indeed_result) # <Response [200]> ok  
# print(indeed_result.text)## html 가져오기 

indeed_soup = BeautifulSoup(indeed_result.text,"html.parser")
# print(indeed_soup)
## class pagination  div 안에 a 링크
pagination = indeed_soup.find("div",{"class":"pagination"})
# print(pagination)
pages = pagination.find_all('a')
# print(pages)
## span 가져오기

spans = []
for page in pages:
    # print(page.find("span"))
    spans.append(page.find("span"))
# print(spans[:-1])  # why 5 ?

spans = spans[:-1]



## 2.4
