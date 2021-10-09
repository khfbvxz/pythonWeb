import os
import requests
from bs4 import BeautifulSoup
from babel.numbers import format_currency
os.system("clear")

url = "https://www.iban.com/currency-codes"

countries = []

request = requests.get(url)
soup = BeautifulSoup(request.text, "html.parser")

table = soup.find("table")
rows = table.find_all("tr")[1:]

for row in rows:
  items = row.find_all("td")
  name = items[0].text
  code =items[2].text
  if name and code:
      country = {
        'name':name.capitalize(),
        'code': code
      }
      countries.append(country)


def ask():
  try:
    choice = int(input("#: "))
    if choice >= len(countries) or choice <0:
      print("Choose a number from the list.")
      ask()
    else:
      country = countries[choice]
      # print(f"You chose {country['name']}\nThe currency code is {country['code']}")
      print(f"{country['name']}")
  except ValueError:
    print("That wasn't a number.")
    ask()
  return country['name'],country['code']

print("Welcom to CurrencyConvert PRO 2000\n")
for index, country in enumerate(countries):
  print(f"#{index} {country['name']}")
print("\n Where are you from? Choose a country by number.\n")
name1,code1 = ask()
print( name1 , "  " , code1)
print("\nNow choose another country.\n")
name2,code2 = ask()
print( name2 , "  " , code2)

def ask2():
  try:
    money = int(input(f"\nHow many {code1} do you want to convert to {code2}\n"))
  except ValueError:
    print("That wasn't a number.")
    ask2()
  return money
money = ask2()
con_money=0
res = requests.get(f"https://wise.com/gb/currency-converter/{code1.lower()}-to-{code2.lower()}-rate?amount={money}")
soup = BeautifulSoup(res.text,"html.parser")
# change_money = soup.find_all("div",{"class":"input-group input-group-lg"})
change_money = soup.find_all("input",{"id":"rate"})
lista = []
for x in change_money:
  lista.append(x)
sample = str(lista[0]).split()
# print(sample)
for i in sample:
  if 'value'==i[0:5]:
    change = float(i[7:-3])
    con_money = change*float(money)
    print(format_currency(float(money), code1.upper(), locale="ko_KR"),end='')
    print(' is ',end="")
    print(format_currency(con_money, code2.upper(), locale="ko_KR") ) 

"""
Use the 'format_currency' function to format the output of the conversion
format_currency(AMOUNT, CURRENCY_CODE, locale="ko_KR" (no need to change this one))
"""

# print(format_currency(5000, "KRW", locale="ko_KR"))