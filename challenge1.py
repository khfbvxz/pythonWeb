'''
7 func + - * /  -  ** %  를 이용하여 계산기  
def plus (a, b):
    return a + b

plus(12,"10")

'''
a = input('숫자 a 를입력하세요')
b = input('숫자 b 를입력하세요')

def plus(a ,b):
    return (float(a)+float(b))
def minus(a,b):
    return (float(a)-float(b))
def times(a,b):
    return (float(a)*float(b))
def division(a,b):
    return (float(a)/float(b))
def negation(a):
    print("-a")
    return (-1*float(a))
def power(a,b):
    return (float(a)**float(b)) 
def reminder(a,b):
    return (float(a)%float(b)) 

print(plus(a,b))
print(minus(a,b))
print(times(a,b))
print(division(a,b))
print(negation(a))
print(power(a,b))
print(reminder(a,b))

