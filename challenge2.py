
def is_on_list(day , days):
    days_low = []
    for x in days:
        days_low.append(x.lower())
    day_low = day.lower()
    result = day_low in days_low
    result_index = days_low.index(day_low)    
    return print(f'Is {days[result_index]} on "days" list? {result}')

def get_x(num,days):
    num = int(num)
    num_s = {1:"first", 2:"second" , 3 : "third" , 4 :"fourth", 5 : "fifth" , 6 : "sixth" , 7 : "seventh"}
    print(f'The {num_s[num]} item in "days" is : {days[num-1]}')
    
def add_x(in_day , days):
    in_day = in_day.lower()
    in_day_t=in_day.title()
    days.append(in_day_t)
    print(days)
def remove_x(remove_day,days):
    remove_day = remove_day.lower()
    remove_day_t = remove_day.title()
    days.remove(remove_day_t)
    print(days)

days = ['Mon','Tue','Wed','Thu','Fri','Sat','Sun']
day = input("is on list??")
num = input("몇 번째 요일을 보고 싶나요? 숫자를 입력하세요(월요일부터 시작합니다)")
in_day = input("어떤 날짜를 리스트에 추가하고 싶은가요?")
remove_day = input("제거하고 싶은 요일을 입력하세요")

is_on_list(day,days)
get_x(num,days)
add_x(in_day,days)
remove_x(remove_day,days)

'''
def is_on_list(day , days):
    days_low = []
    for x in days:
      ## 입력을 대문자 소문자 상관없이 모두 소문자로 변경
      days_low.append(x.lower())
    day_low = day.lower()
    result = day_low in days_low ## 리스트 내 입력값이 있으면 True 없으면 False
    result_index = days_low.index(day_low) ## 출력 예시 'Sat' 처럼 하기 위한 인덱싱 
    
    return print(f'Is {days[result_index]} on "days" list? {result}')

def get_x(num,days):
    num = int(num)
    ## 요일에 순서에 따라 출력할 단어 딕셔너리 형태로 변수에 저장
    num_s = {1:"first", 2:"second" , 3 : "third" , 4 :"fourth", 5 : "fifth" , 6 : "sixth" , 7 : "seventh"}
    print(f'The {num_s[num]} item in "days" is : {days[num-1]}')
    
def add_x(in_day , days):
    in_day = in_day.lower()
    in_day_t=in_day.title()  ## 소문자로 바꾼 요일에 첫번째 알파벳만 대문자로 바꾸어주는 # title() 함수 사용
    days.append(in_day_t)
    print(days)
def remove_x(remove_day,days):
    remove_day = remove_day.lower()
    remove_day_t = remove_day.title()
    days.remove(remove_day_t)
    print(days)

days = ['Mon','Tue','Wed','Thu','Fri','Sat','Sun']
day = input("is on list??")
num = input("몇 번째 요일을 보고 싶나요? 숫자를 입력하세요(월요일부터 시작합니다)")
in_day = input("어떤 날짜를 리스트에 추가하고 싶은가요?")
remove_day = input("제거하고 싶은 요일을 입력하세요")

is_on_list(day,days)
get_x(num,days)
add_x(in_day,days)
remove_x(remove_day,days)
'''