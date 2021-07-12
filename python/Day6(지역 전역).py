# #지역변수와 전역변수

# #global을 이용한 전역변수
# gun = 10 #총 10자루

# def checkpoint(soldiers): # 경계근무 나가는 군인 수
#     global gun # 전역공간에 있는 gun 이라는 변수를 사용
#     gun = gun - soldiers #전체 총에서 경계근무 나가는 군인 수만큼 뺀 잔여 총
#     print("[함수 내] 남은 총 :{0}".format(gun))

# print("전체 총 : {0}".format(gun))
# checkpoint(2)
# print("남은 총 : {0}".format(gun))

# #지역변수 사용
# gun = 10

# def checkpoint_ret(gun, soldiers):
#     gun = gun -soldiers
#     print("[함수 내] 남은 총 : {0}".format(gun))
#     return gun

# print("전체 총 : {0}".format(gun))
# gun = checkpoint_ret(gun,2)
# print("남은 총 :{0}".format(gun))

#퀴즈
#조건1: 표준 체중은 별도의 함수 내에서 계산
# *함수명: std_weight 
# *전달값: 키,성별
#조건2: 표준 체중은 소수점 둘째자리까지 표시

# def std_weight(height,gender):
#     meter=height/100
#     if gender == "남자":
#        return meter*meter*22
#     else:
#         return meter*meter*21

# height = 175
# gender = "남자"
# weight=round(std_weight(height,gender),2) #소수점 둘째자리까지 반올림
# print("키 {0}cm {1}의 표준 체중은 {2}kg입니다. ".format(height,gender,weight))


#표준입출력

# print("python","java")

# print("python" + "java")

# print("python","java",sep = ",") #값들을 콤마(,) 로 구분

# print('pyhton','java',sep = ",",end ="?")

# import sys # sts 모듈을 가져와서 사용하겠다는 의미
# print("python","java",file=sys.stdout) #표준 출력
# print("ptthon","java",file=sys.stderr) #표준 에러

# scores = {"수학":0,"영어":50,"코딩":100}

# for subject ,score in scores.items(): #key, value
#     print(subject, score)




#정리
#전역변수를 많이 쓰게 되면 코드 관리가 어려워짐
#꼭 필요한 경우에만 쓰는게 좋음
#global이라는 키워드로 전역변수를 사용할수 있음
#소수점 반올림 하는 방법round(),2 적으면 소수점 둘째자리까지 반올림
#stdout는 정보를 가지는 로그를 남길 때 
#stderr는 에러 발생 시 관련 내용을 출력하기 위해 사용




