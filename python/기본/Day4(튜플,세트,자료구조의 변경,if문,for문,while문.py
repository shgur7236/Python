##튜플
##돈까스 식당 고정 메뉴
#menu = ("돈까스","치즈까스")
#print(menu[0]) 
#print(menu[1])
##튜플은 변경,추가,삭제가 되지 않는다

##추가
##기본 형태
#name = "김종국"
#age = 20
#hobby = "코딩"
#print(name,age,hobby)

##튜플 형태
#(name,age,hobby) =("김종국",20,"코딩")
#print(name,age,hobby)


#세트
#세트는 중복을 허용하지 않으며 또한 데이터의 순서도 보장하지 않는다.
# 수학에서 배우는 것과 동일하게 중괄호를 이용하여 선언 가능
# my_set = {1,2,3,3,3} #중복을 허용하지 않아서 3은 1번만 들어감
# print(my_set)


# java = {"곽희상","노혁","진시윤"}
# python = set({"노혁","이주원"})

# #교집합(자바와 파이썬을 모두 다를줄 아는 사람)
# # print(java&python)
# # print(java.intersection(python))

# # #합집합 (java 또는 파이썬을 할 수 있는 개발자)
# # print(java | python)
# # print(java.union(python))

# # #집합은 순서를 보장하지 않는다 출력 순서는 실행할때 마다 달라 질수 있다

# # #차집합 (자바는 할 수 있지만 파이썬은 할 줄 모르는 개발자)
# # print(java-python)
# # print(java.difference(python))

# #파이썬 개발자 추가
# python.add("곽희상")
# print(python) 

# #자바 개발자 삭제
# java.remove("곽희상")
# print(java)

#자료구조의 변경
# menu = {"coffee","milk","juice"}
# print(menu,type(menu)) # menu의 type 정보:set
# #세트 -> 리스트
# menu = list(menu) 
# print(menu,type(menu))
# #리스트 -> 튜플
# menu = tuple(menu) 
# print(menu,type(menu))
# #튜플 -> 세트
# menu = set(menu)
# print(menu,type(menu))


#퀴즈
#조건1: 편의상 댓글은 20명이 작석하였고 아이디는 1~20이라고 가정
#조건2: 댓글 내용과 싱관 업시 무작위로 추첨하되 중복은 불가
#조건3: random 모듈의 shuffle 과 sample을 활용

# from random import*
# #users = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
# users = range(1,21)
# users = list(users)

# winners = sample(users,4)

# print("---당첨자---")
# print("치킨 당첨자: {0}".format(winners[0]))
# print("커피 당첨자: {0}".format(winners[1:]))
# print("---축하해---")


#if문 (if 조건:실행 명령문)
# weather = "비"

# if weather == "비": # if조건문은 들여쓰기가 중요하다
#     print("우산을 챙겨가세요")

# weather = input("오늘 날씨 어때요? ")
# #print(weather)

# if weather == "비"or weather=="눈":
#     print("우산을 챙기세요") #1번
# elif weather == "미세먼지":
#     print("마스크를 챙기세요") #2번
# else:
#     print("그냥 나가") #3번

# temp = int(input("기온은 어때요? "))

# if 30 <= temp:
#     print("너무 더워요")
# elif 10 <= temp and temp <30:
#     print("굿")
# elif 0<= temp <10:
#     print("외투 챙기세요")
# else: 
#     print("너무 추워")

#퀴즈
# class_ = int(input("몇반의 반수를 알고 싶은가욥? "))

# if class_ == 1:
#     print("19")
# elif 2<=class_<=4:
#     print("18")
# else:
#     print("그런 반은 없어요 ㅎㅎ")


#for문
#for waiting_no in range(1,6):
#    print("대기번호: {0}".format(waiting_no))

# starbuks = ["아이언맨","토르","그루트"]
# for customer in starbuks:
#    print("{0}, 커피가 준비되었습니다".format(customer))


#while문
# customer = "토르"
# index = 5

# while index >0:
#     print("{0}, 커피가 준비 되었습니다. {1}번 남았어요.".format(customer,index))
#     index-=1
#     if index == 0:
#         print("커피는 폐기처분되었습니다.")

# customer = "노혁"
# index = 1

# while True:
#     print("{0}, 커피가 준비 되었습니다. 호출{1}회".format(customer,index))
#     index+=1

# customer = "노혁"
# person = "unknown"

# while person != customer:
#     print("{0}, 커피가 준비 되었습니다".format(customer))
#     person = input("이름이 어떻게 되세요? ")


