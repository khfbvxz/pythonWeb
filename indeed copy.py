## requset 2 라이브러리 
import requests  ## 2.26.0
from bs4 import BeautifulSoup

### radius 무시
'''
indeed 사이트 부터 
'''
import requests
from bs4 import BeautifulSoup
indeed_resul = requests.get("https://www.indeed.com/jobs?q=python&limit=50")
# print(indeed_resul) 
## <Response [200]>
# print(indeed_resul.text)  ## 모든 html 가져옴.

'''
뷰티풀 수프 라이브러리 html 정보 보기위한
2.3
find all ('a') 리스트 반환?
page 부분 

indeed_soup = BeautifulSoup(indeed_resul.text,"html.parser")
# print(indeed_soup)

## page 부분 pargination  div
pagination = indeed_soup.find("div",{"class":"pagination"})
# print(pagination)
## span class pn  부분 확인

pages = pagination.find_all('a')
# print(pages)  ## anchor 안에 span 에 페이지 있음 이제 a 안 span 찾기

spans = []
for page in pages:
  # print(page.find("span"))  ## 2~ 5까지 ? 
  spans.append(page.find("span"))
# print(spans[:-1])## 맨 마지막 넥스트 여서 제거
spans = spans[:-1]
'''

'''2.4 

indeed_soup = BeautifulSoup(indeed_resul.text,"html.parser")

pagination = indeed_soup.find("div",{"class":"pagination"})
## span class pn  부분 확인

pages = pagination.find_all('a')
# print(pages)  ## anchor 안에 span 에 페이지 있음 이제 a 안 span 찾기

spans = []
for page in pages:
  # print(page.find("span"))  ## 2~ 5까지 ? 
  spans.append(page.find("span"))
# print(spans[:-1])## 맨 마지막 넥스트 여서 제거
spans = spans[:-1]
'''

''' 2.5

'''
indeed_soup = BeautifulSoup(indeed_resul.text,"html.parser")

pagination = indeed_soup.find("div",{"class":"pagination"})

links = pagination.find_all('a')

pages = []
for link in links[:-1]:
  pages.append(int(link.string))


print(pages)
max_page = pages[-1]

print(range(max_page))

# ### 실험 1 페이지 5가 아닌 내가 리스트를 따로 준다면?
# pages2=[]
# for i in range(2,12,1):
#   pages2.append(i)
# print(pages2)  # [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

'''2.5
indeet .py 
import requests
from bs4 import BeautifulSoup

## 함수 만들기 
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
  jobs =[]
  for page in range(last_page):
    result=requests.get(f"{URL}&start={page*50}")
    print(result.status_code)
  return jobs

main .py 


last_pages = extract_indeed_pages()  #  5지만 11로 바꿔보자 

# print(max_indeed_pages)
# extract_indeed_jobs(last_pages)
extract_indeed_jobs(12)
'''

'''2.6
indeed.py
import requests
from bs4 import BeautifulSoup

## 함수 만들기 
LIMIT=50
URL = f"https://www.indeed.com/jobs?q=python&limit={LIMIT}"

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
  jobs =[]
  # for page in range(last_page):
  result=requests.get(f"{URL}&start={0*50}")
  # print(result.status_code)
  soup = BeautifulSoup(result.text,"html.parser")
  ### 타이틀만 나오게
  ## new 랑 new 없는거
  job_seen = soup.find_all("h2",{"class":"jobTitle jobTitle-color-purple jobTitle-newJob"})
  joblist1 = []
  joblist2 = []
  for job in job_seen:

    title = job.find_all("span")
    # title = title.text
    # title = job
    joblist1.append(title[1].text)

  job_seen2 = soup.find_all("h2",{"class":"jobTitle jobTitle-color-purple"})
  for job in job_seen2:
    title = job.find("span")
    # print(title.string)
    joblist1.append(title.string)
  # print(job_seen)
  print(len(joblist1))
  return jobs

  main.py 
  from indeed import extract_indeed_pages,extract_indeed_jobs
import os
last_pages = extract_indeed_pages()  #  5지만 11로 바꿔보자 

# print(max_indeed_pages)
# extract_indeed_jobs(last_pages)
# os.system("clear")
extract_indeed_jobs(12)

'''

''' 2.7
import requests
from bs4 import BeautifulSoup

## 함수 만들기 
LIMIT=50
URL = f"https://www.indeed.com/jobs?q=python&limit={LIMIT}"

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
  jobs =[]
  # for page in range(last_page):
  result=requests.get(f"{URL}&start={0*50}")
  # print(result.status_code)
  soup = BeautifulSoup(result.text,"html.parser")
  ### 타이틀만 나오게
  ## new 랑 new 없는거
  job_seen = soup.find_all("td",{"class":"resultContent"})

  jobs=[]
  comp = []
  for job in job_seen:
    # company = job.find("span",{"class":"companyName"})
    # print(company.text)
    # comp.append(company.text)
    if job.find("h2",{"class":"jobTitle jobTitle-color-purple jobTitle-newJob"}) is not None:
      title = job.find("h2",{"class":"jobTitle jobTitle-color-purple jobTitle-newJob"}).find_all("span")
      jobs.append(title[1].text)
      company = job.find("span",{"class":"companyName"})
      company = str(company.string)
      company = company.strip()
      comp.append(company)
    elif job.find("h2",{"class":"jobTitle jobTitle-color-purple"}) is not None:
      title2 = job.find("h2",{"class":"jobTitle jobTitle-color-purple"}).find("span").string
      jobs.append(title2.text)
      company = job.find("span",{"class":"companyName"})
      company = str(company.string)
      company = company.strip()
      comp.append(company)
      # print(title2.text,"2")
    # else:
    #   print("1")


  # print(jobs)
  # print(len(jobs))
  # print(len(comp))
  for x in range(len(jobs)):
    print(jobs[x],"  " , comp[x])

  return jobs
'''


''' 2.8
import requests
from bs4 import BeautifulSoup

## 함수 만들기 
LIMIT=50
URL = f"https://www.indeed.com/jobs?q=python&limit={LIMIT}"

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

def extract_job(html):
  if html.find("h2",{"class":"jobTitle jobTitle-color-purple jobTitle-newJob"}) is not None:
    title = html.find("h2",{"class":"jobTitle jobTitle-color-purple jobTitle-newJob"}).find_all("span")
    title = title[1].text
    company = html.find("span",{"class":"companyName"})
    company = str(company.string)
    company = company.strip()
    
  elif html.find("h2",{"class":"jobTitle jobTitle-color-purple"}) is not None:
    title = html.find("h2",{"class":"jobTitle jobTitle-color-purple"}).find("span").string
    title = title.text
    company = html.find("span",{"class":"companyName"})
    company = str(company.string)
    company = company.strip()

  location = html.find("div",{"class":"companyLocation"})
  location = str(location.string)
  location = location.strip()
  # print(location)

  return {'title':title , 'company':company , 'location':location}
  

def extract_indeed_jobs(last_page):
  jobs =[]
  for page in range(last_page):
    print(f"Scraping page {page}")
    result=requests.get(f"{URL}&start={0*50}")
    # print(result.status_code)
    soup = BeautifulSoup(result.text,"html.parser")
    ### 타이틀만 나오게
    ## new 랑 new 없는거
    job_seen = soup.find_all("td",{"class":"resultContent"})
    # job_ids = soup.find("div",{"class":"mosaic mosaic-provider-jobcards mosaic-provider-hydrated"})
    # if job_ids.find_all("a")['data-jk'] is not None:
    #   jon = job_ids.find_all("a")['data-jk']
    #   print(jon)
    jobs=[]
    # comp = []
    cont = 0
    for job in job_seen:

      job = extract_job(job)
      jobs.append(job)
      cont=cont+1
    # print(job , cont)
  # for job in job_ids:
  #   print(job.find("a")["data-sk"])


  # print(jobs)
  # print(len(jobs))
  # print(len(comp))
  

  return jobs

  main . py
  from indeed import extract_indeed_pages,extract_indeed_jobs
import os
last_pages = extract_indeed_pages()  #  5지만 11로 바꿔보자 

# print(max_indeed_pages)
# extract_indeed_jobs(last_pages)
# os.system("clear")
indeed_jobs = extract_indeed_jobs(12)
print(indeed_jobs)

'''

'''10-11
indeed.py
import requests
from bs4 import BeautifulSoup

## 함수 만들기 
LIMIT=50
URL = f"https://www.indeed.com/jobs?q=python&limit={LIMIT}"

def get_last_page():
  result = requests.get(URL)
  soup = BeautifulSoup(result.text,"html.parser")
  pagination = soup.find("div",{"class":"pagination"})  ##  div 만 
  links = pagination.find_all('a')
  
  pages = []
  for link in links[:-1]:
      
      pages.append(int(link.string)) ## a 태그 안 span안에 있으므로 

  max_page = pages[-1]
  return max_page

def extract_job(html):
  if html.find("h2",{"class":"jobTitle jobTitle-color-purple jobTitle-newJob"}) is not None:
    title = html.find("h2",{"class":"jobTitle jobTitle-color-purple jobTitle-newJob"}).find_all("span")
    title = title[1].text
    company = html.find("span",{"class":"companyName"})
    company = str(company.string)
    company = company.strip()
    
  elif html.find("h2",{"class":"jobTitle jobTitle-color-purple"}) is not None:
    title = html.find("h2",{"class":"jobTitle jobTitle-color-purple"}).find("span").string
    title = title.text
    company = html.find("span",{"class":"companyName"})
    company = str(company.string)
    company = company.strip()

  location = html.find("div",{"class":"companyLocation"})
  location = str(location.string)
  location = location.strip()
  # print(location)

  return {'title':title , 'company':company , 'location':location}
  

def extract_jobs(last_page):
  jobs =[]
  for page in range(last_page):
    print(f"Scraping page {page}")
    result=requests.get(f"{URL}&start={0*50}")
    # print(result.status_code)
    soup = BeautifulSoup(result.text,"html.parser")
    ### 타이틀만 나오게
    ## new 랑 new 없는거
    job_seen = soup.find_all("td",{"class":"resultContent"})
    # job_ids = soup.find("div",{"class":"mosaic mosaic-provider-jobcards mosaic-provider-hydrated"})
    # if job_ids.find_all("a")['data-jk'] is not None:
    #   jon = job_ids.find_all("a")['data-jk']
    #   print(jon)
    jobs=[]
    # comp = []
    cont = 0
    for job in job_seen:

      job = extract_job(job)
      jobs.append(job)
      cont=cont+1
    # print(job , cont)
  # for job in job_ids:
  #   print(job.find("a")["data-sk"])
  # print(jobs)
  # print(len(jobs))
  # print(len(comp))
  return jobs

def get_jobs():
  last_pages = get_last_page()  #  5지만 11로 바꿔보자 
  # jobs = extract_jobs(12) # 라스트 페이지 임의조정함 
  jobs = extract_jobs(last_pages)
  return jobs
  
  main.py

from indeed import get_jobs as get_indeed_jobs
import os



indeed_jobs = get_indeed_jobs()
print(indeed_jobs)

'''

