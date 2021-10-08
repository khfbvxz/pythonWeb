import os
import requests
from bs4 import BeautifulSoup

os.system("clear")
url = "https://www.iban.com/currency-codes"

result = requests.get(url)
soup = BeautifulSoup(result.text, "html.parser")
# print(soup)
iban_soup=soup.find("tbody")
iban_soup = iban_soup.find_all("td")
list_iban = []
for text in iban_soup:
    list_iban.append(text.string)
    
# print(len(list_iban)/4)
iban_na = []
iban_code = []

for na in range(len(list_iban)):
    if na%4==0:
        iban_na.append(str(list_iban[na]).capitalize())
    elif na%4==2:
        iban_code.append(list_iban[na])

for i in range(len(iban_code)):
    print(f"# {i+1} {iban_na[i]}")
while(True):
    
    try:
        q= int(input("#:"))
        if q <= len(iban_na):
            print(f"You Chose {iban_na[q]}\nThe currency code is {iban_code[q]}")
            break
        elif q > len(iban_na):
            print("Choose a number from the list.")
    except:
        print("That wasn't a number.")
        continue
