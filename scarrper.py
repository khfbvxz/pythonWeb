import requests
from bs4 import BeautifulSoup

## 함수 만들기 
# LIMIT=50


def get_last_page(url):
  result = requests.get(url)
  soup = BeautifulSoup(result.text,"html.parser")
  pages = soup.find("div",{"class":"s-pagination"}).find_all("a")
  last_page = pages[-2].get_text(strip=True)
  return int(last_page)  ## 나는 9인데 왜 마지막 79인가 

def extract_job(html):
  title = html.find("h2",{"class":""})

def extract_job(html):
  title = html.find("h2").find("a")["title"]
  company, location = html.find("h3").find_all("span",recursive=False)
  company = company.get_text(strip=True)
  location = location.get_text(strip=True).strip("-").strip("\r").strip("\n")
  job_id = html['data-jobid']
  return {'title':title,'company':company,'location':location,"apply_link":f"https://stackoverflow.com/jobs/{job_id}"}

def extract_jobs(last_page,url):
  jobs = []
  
  for pages in range(last_page):
    print(f"Scraping page {pages}")
    # print(page) 0 - 78
    # print(page+1) 1 - 79
    result = requests.get(f"{url}&pa={pages+1}")
    soup = BeautifulSoup(result.text,"html.parser")
    results = soup.find_all("div",{"class":"-job"})
    for result in results:
      job = extract_job(result)
      jobs.append(job)
  return jobs



def get_jobs(word):
  url = f"https://stackoverflow.com/jobs?&q={word}&sort=i"
  last_pages = get_last_page(url)
  jobs = extract_jobs(last_pages,url)
  return jobs