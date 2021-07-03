#문자열
#sentence1 = '나는 노혁입니다'
#print(sentence1)

#sentence2 = "파이썬은 어려워요"
#print(sentence2) # 작은 따음표와 큰 따음표의 차이는 크게 없다
# 그러나 앞 뒤 쌍은 맞춰야 한다

#sentence3="""
#나는 노혁이고.
#파이썬은 쉬워요
#"""
#print(sentence3) # 따옴표 3개로 감싸는 것은 주석 때도 사용하기 때문에 주석은 작음 따옴표,문자열은 큰 따옴표로 사용

#슬라이싱
# jumin = "050611-1234567"
# print("성별 :"+jumin[7]) # 성별 :1 c배열과 똑같다
# print("연 : "+jumin[0:2]) # 0부터 2직전까지
# print("월"+jumin[2:4]) # 2부터 4직전까지
# print("일"+jumin[4:6]) # 4부터 6직전까지

# print("생년월일 : "+jumin[:6]) # 처음부터 6직전까지 
# print("뒤 7자리 :"+jumin[7:]) # 7부터 끝까지
# print("뒤 7자리 (뒤에부터)"+jumin[-7:]) # 맨뒤에서 7번쨰 위치로부터 끝까지

#문자열처리함수
#python = "Python is null "
#print(python.lower()) # 소문자
#print(python.upper()) # 대문자
#print(python[0].isupper()) #0번째 인덱스의 값이 대문자인지 확인 True False
#print(len(python)) # 전체 길이
#print(python.replace("Python","java")) # Python ->java 

# index = python.index("n") # 처음으로 발견된 n의 인덱스
# print(index) # 5 : python 의 n
# index = python.index("n",index+1) # 6 번째 인덱스 이후에 처음으로 발견된 n의 인덱스
# print(index) # 10 : 

# print(python.find("n")) # 처음으로 발견된 n의 인덱스
# print(python.find("Java"))  #Java가 없으므로 -1
# print(python.count("n")) # n의 갯수

#문자열포맷
# print("a"+"b") # ab
# print("a","b") # a b

# print("나는 %d살입니다."%17)
# print("나는 %s을 좋아합니다"%"돈")
# print("BANANA 는 %c로 시작합니다" %"B")

# print("나는 %s살입니다." %17)# %s로도 정수값 표현 가능
# print("나는 %s색과 %s색을 좋아합니다."%("검정","노란")) # 2개 이상의 값을 넣는 방법

# print("나는 {}살입니다.".format(20))
# print("나는 {}색과 {}색을 좋아합니다".format("RED","BLACK"))
# print("나는 {1}색과 {0}색을 좋아해요".format("RED","BLACK"))

# age = 17
# color = "검정"
# print(f"나는 {age}살이며, {color}색을 좋아합니다")

#탈출문자
#from os import replace
#from typing import Counter


#print("백문이 불여일견\n백견이 불여일타")
#print("저는 \"노혁\" 입니다") 

#print(r"/:\Users\1106노혁\Deskop\git\WEB1-1>")
#print("Red apple\rpine") #\r 은 커서를 맨앞으로 이동시키는 역활을 한다 RED를 덮은다
#print("Redd\bApple") # \b 앞 글자 하나 삭제 
# \t 는 tab 역활
 
#퀴즈
#url = "http://naver.com"
#url = "http://daum:net/
#url = "http://youtube.com"

#one = url.replace("http://","") # 규칙1
#one = one[:one.index(".")] # 규칙2
#password = one[:3] +str(len(one))+str(one.count("e"))+"!"# 규칙3

#print("{0}의 비밀번호는 {1}입니다".format(url,one))
