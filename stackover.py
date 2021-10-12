'''
2.9
so.py
URL = f"https://stackoverflow.com/jobs?&q=python&sort=i"

def get_last_page():
  result = requests.get(URL)
  soup = BeautifulSoup(result.text,"html.parser")
  # print(soup)
  pagination = soup.find("div",{"class":"s-pagination"})
  # print(pagination)
  pages = soup.find("div",{"class":"s-pagination"}).find_all("a")
  print(pages)


def get_jobs():
  last_page = get_last_page()
  return []

main.py 

from indeed import get_jobs as get_indeed_jobs
import os
from so import get_jobs as get_so_jobs


# indeed_jobs = get_indeed_jobs()

so_jobs = get_so_jobs()

'''
#############
'''2.10


'''