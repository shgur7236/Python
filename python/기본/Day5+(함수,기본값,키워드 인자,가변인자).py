# #함수

# def open_account():
#     print("새로운 계좌가 생성되었습니다.")

# open_account()

# def deposit(balance,money):
#     print("입금이 완료되었습니다. 잔액은{0}원입니다.".format(balance+money))
#     return balance+money

# balance = 0 # 최초 잔액
# balance = deposit(balance,1000)
# print(balance) # 현재 잔액

# def withdraw(balance,money): # 출금
#     if balance >= money: 
#         print("출금이 완료 되었습니다. 잔액은{0}입니다.".format(balance-money))
#         return balance-money 
#     else:
#         print("출금이 완료되지 않았습니다. 잔액은{0}입니다.".format(balance))
#         return balance # 기존 잔액 반환

# balance = 0
# balance = deposit(balance, 1000)

# #출금 시도
# balance = withdraw(balance, 2000) #2000원 출금 시도 시 잔액이 부족하므로 실패
# balance = withdraw(balance, 500) #500원 출금 시도 시 성공
# print(balance)

# def withdraw_night(balance, money):
#     commission = 100 
#     return commission, balance- money-commission # 튜플 형식으로 반환

# balance = 0
# balance = deposit(balance, 1000) #천원 입금

# commission,balance= withdraw_night(balance,500) #튜플 형식으로 반환된 2개의 값을 각 변수에 저장
# print("수수료 {0} 원이며, 잔액은{1} 원입니다.".format(commission,balance))


# #기본값

# def profile(name,age,main_lang):
#     print("이름 : {0}\t나이 : {1}\t주 사용 언어 : {2}".format(name,age,main_lang))

# profile("유재석",20,"파이썬")
# profile("김태호",25,"자바")

# def profile(name,age=17,main_lang="파이썬"):
#     print("이름: {0}\t나이 : {1}\t주 사용 언어 : {2}".format(name,age,main_lang))

# profile("유재석")
# profile("김태호")    

# #키워드 인자

# def profile(name, age, main_lang):
#     print(name,age,main_lang)
    
# # profile("유재석",20,"파이썬")
# # profile("김태호",25,"자바")

# profile(name="유재석", main_lang="파이썬", age=20)
# profile(main_lang="자바",age=25,name="김태호")

# #가변 인자

# def profile(name, age, *language): #언어 정보를 전달하고 싶은 갯수 만큼 전달 가능
#     print("이름 : {0}\t나이 : {1}\t".format(name,age),end =" ")
    
#     # print(type(language))  # tuple
#     for lang in language:
#         print(lang,end=" ") # 언어들을 모두 한 줄에 표시
#     print() #줄바꿈 목적   

# profile("유재석",20,"Python","Java","c","c++","c#","js")
# profile("김태호",25,"Kotlin","Swift","","","")













