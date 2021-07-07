#countinue 와 break

# absent = [2,5] # 결석한 학생 출석번호

# for student in range(1,11): #출석번호 1~10
#     if student in absent : #결석했으면 책을 읽지 않고 다음 학생으로 넘어가기
#         continue
#     print("{0},책을 읽어봐.".format(student))

# no_book = [7] #책을 가져오지 않은 학생 출석번호

# for student in range(1,11):
#     if student in absent:
#         continue
#     elif student in no_book:
#         print("오늘 수업 여기까지.{0}는 교무실로 따라와".format(student))

# #한 줄 for
# students = [1,2,3,4,5]
# print(students)

# #한 줄 for를 이용하여 각 항목에 100을 더함
# students= [i+100 for i in students]
# print(students) 

# students =["Iron man","Thor","I am groot"]
# print(students)

# students=[len(i) for i in students]
# print(students)

# students =["Iron man","Thor","I am groot"]
# print(students)

# students = [i.upper() for i in students]
# print(students)

#퀴즈
#조건1 : 승객별 운행 소요 시간은 5분~50분 사이의 난수로 정해짐
#조건2 : 당신은 소요 시간 5분~15분 사이의 승객만 매칭해야 함

# from random import *

# cnt = 0 # 총 탑승 승객 수

# for i in range(1,51): # 총 50분의 승객
#     time = randrange(5,51) # 5분~50분 사이의 소요 시간

#     if 5<= time <=15:
#         print("[0] {0}번째 손님 (소요시간 : {1}분)".format(i,time))
#         cnt +=1
#     else:
#         print("[ ] {0}번째 손님 (소요시간 : {1}분)".format(i,time))


# print("총 탑승 승객 : {0}분".format(cnt))
