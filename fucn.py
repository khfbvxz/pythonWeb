
## 함수

# print(len("sjhfklhjasdflkjjas"))

# age = "16"
# print(type(age))
# n_age = int(age)
# print(type(n_age))

# create function  들여쓰기로 함수 안을 표시 tab body안
# def say_hello(name="anonymous"):
#     print("hello",name)
#     print("bye")
# say_hello()
# say_hello("nicolas")
# say_hello(3)
# say_hello(True)

# def plus(a,b):
#     print(a+b)
# def minus(a,b=0):
#     print(a-b)
# plus(3,5)
# minus(2)
# def r_plus(a,b):
#     return a-b  # 리턴하는 순간 함수 종료 
#     print("ashdkjhasjkl") # 실행 x 
# # p_res = plus(2,3)
# r_res = r_plus(b=30,a=1)

# print(r_res)
# ## keyworded Argument 
# def say_hello(name,age):
#     # return f"Hello { name} you are {age} years old"
#     return "Hello "+  name+ " you are "+ age+ " years old " 

# hello = say_hello("nico","12")
# hello = say_hello(age = "12", name="nico")
# print(hello)

## code challenge! 
## 7가지 연산자 가지고 예외처리  7 func + - * /  -  ** % 

'''
7 func + - * /  -  ** % 
def plus (a, b):
    return a + b

plus(12,"10")

'''
## 1.9
# def plus (a, b):
#     if type(b)  is int or type(b) is float:
#         return a+b
#     else:
#         return None

# print(plus(12,15.5))

## 1.10 
# def age_check(age):
#     print(f"you are {age}")
#     if age<18:
#         print("you cant drink")
#     elif age ==18 or age == 19:
#         print("you are new to this!")
#     elif age>20 and age <25:
#         print("you are still kind of young")
#     else:
#         print("enjoy your drink")
# age_check(19)

## 1.11 for loop
# days = ("Mon","Tue","Wed","Thu","Fri")

# for day in days:
#     # print(day)
#     if day is "Wed":
#         break
#     else:
#         print(day)
# for letter in "nicolas":  ## 문자열도 하나의 시퀀스 
#     print(letter)


## 1. 12  modules
# import math 

# print(math.ceil(1.2))
# print(math.fabs(-1.2))

from math import  fsum as sexy_sum
# print(ceil(1.2))
print(sexy_sum({1,2,3,4,5,6,7}))

from calculator import plus , minus
print(plus(1,2))
print(minus(1,2))