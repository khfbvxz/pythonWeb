## requset 2 라이브러리 
import requests  ## 2.26.0
from bs4 import BeautifulSoup


LIMIT=50
URL = f"http://www.indeed.com/jobs?q=python&limit={LIMIT}"

def extract_indeed_pages():
    result = requests.get(URL)
    soup = BeautifulSoup(result.text,"html.parser")
    pagination = soup.find("div",{"class":"pagination"})  ##  div 만 
    links = pagination.find_all('a')
   
    pages = []
    for link in links[:-1]:
       
        pages.append(int(link.string)) ## a 태그 안 span안에 있으므로 

    max_page = pages[-1]
    return max_page

def extract_indeed_jobs(last_page):
    jobs = []
    # for page in range(last_page):
        # print(f"&start={page*LIMIT}")
    result=requests.get(f"{URL}&start={0*LIMIT}")
    # print(result.status_code) ## 200 이 5개 출력되야함... 
    soup = BeautifulSoup(result.text,"html.parser")
    results =soup.find_all("div",{"class":"jobsearch-SerpJobCard"})
    print(results)

    ## 태그 잘 찾아야함.. 
    # for result in results:
    #     print(result.find("div", {"class":"title"}.string))
    return jobs
lsat_page=extract_indeed_pages()
extract_indeed_jobs(lsat_page)