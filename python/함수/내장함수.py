#내장함수
#import를 하지 않고도 사용할 수 있도록 내장되어 있는 함수를 의미한다

# lan = input("무슨 언어를 좋아하세요? ") # 내장함수 input 
# print("{0}은 아주 좋은 언어입니다.!".format(lan))

#내장 함수는 종류가 매우 많다 
#그 중 하나인 dir()함수
#dir()은 어떤 객체를 넘겼으 때 그 객체가 어떤 변수와 함수를 가지고 있는지 알려주는 목적으로 사용 가능

# print(dir())
# import random # random 모듈 가져다 쓰기
# print(dir())
# import pickle # pickle 모듈 가져다쓰기
# print(dir())

# import random
# print(dir(random))

# lst = [1,2,3]
# print(dir(lst))

name = "Noh"
print(dir(name))