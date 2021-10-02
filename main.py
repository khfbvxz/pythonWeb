a_string='like this'  ## string
a_number=3
a_flaoat = 3.12
a_boolean = False ## c= False 파이썬은 앞에 대문자 js 는 소문자 true false
a_none = None ## 비어있다 존재하지않는다. 그냥 없다. null

## 리스트 수정 가능  다양한 타입을 넣을 수 있음
# days =[ "Mon","Tue","Wed","Thur","Fri"]
# print(days)
# days.append("Sat")
# days.reverse()
# print(days)

##  튜플 수정 불가능
days =( "Mon","Tue","Wed","Thur","Fri" )
print(type(days))

name = "Nico"
age = 29
korean = True
fav_food = ["kimchi","sashimi"]
## 딕셔너리  key value
nico = { 
        "name" : "Nico",
        "age" : 29,
        "korean" : True,
        "fav_food" : ["kimchi","sashimi"]
    }
print(nico)
nico["hansome"] = True
print(nico)