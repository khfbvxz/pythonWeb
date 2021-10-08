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
# ## requset 2 라이브러리 
# import requests  ## 2.26.0
# from bs4 import BeautifulSoup
# indeed_result = requests.get("http://www.indeed.com/jobs?q=python&limit=50")

# # print(indeed_result) # <Response [200]> ok  
# # print(indeed_result.text)## html 가져오기 

# indeed_soup = BeautifulSoup(indeed_result.text,"html.parser")
# # print(indeed_soup)
# ## class pagination  div 안에 a 링크
# pagination = indeed_soup.find("div",{"class":"pagination"})  ##  div 만 
# # print(pagination)
# links = pagination.find_all('a')
# # print(pages)
# ## span 가져오기

# pages = []
# for link in links[:-1]:
#     # pages.append(link.find("span").string)
#     # string to integer
#     pages.append(int(link.string)) ## a 태그 안 span안에 있으므로 
# # print(spans[:-1])  # why 5 ?

# # pages = pages[:-1] ## 
# max_page = pages[-1]

## 페이지를 계속해서 request 를 만들어야함  
for n in range(max_page):
    print(n)  ## 페이지 숫자 0 -> page 1 
    print(f"start={n*50}") 

