import os
import requests
def url_s(in_urls):
  in_urls = in_urls.split(",")  ##  , 로 split  list type
  
  for url in in_urls:
    url = url.strip()
    if ".com" not in url:
      print(f"{url} is not a valid URL.")
      break
 
  for x in range(len(in_urls)):
    in_urls[x] = in_urls[x].strip().lower() 
    if ("http://" not in in_urls[x] ):
      in_urls[x] = "http://"+in_urls[x]
  
  return in_urls

def url_check(urls):
  for url in in_urls:
    try:
      response = requests.get(url)
      print(f"{url} is up!" )
    except:
      print(f"{url} is down!" )  

restart="y"
while restart=="y":
  print("Welcome to IsItDown.py!")
  print("Please write a URL or URLs you want to check. (separated by comma)")
  in_urls = input()

  in_urls=url_s(in_urls)## split strip lower
  url_check(in_urls)  ## url check 

  test = True
  while(test):
    restart = input("Do you want to restart over? y/n ")
    if(restart == "y"):
      test = False
      ## 콜솔창 클리어
      clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')
      clearConsole()
      #  print("\x1B[H\x1B[J") ## 콘솔창 종료
    elif(restart=="n"): ## n 입력시 종료
      test = False
      print("k. bye!")
      break
    else:
      print("That's not a valid answer")
      test = True
