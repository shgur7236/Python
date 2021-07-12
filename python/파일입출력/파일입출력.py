#1. 파일을 열고
#2. 파일에 어떤 내용을 쓰거나 일고 
#3. 파일을 닫는 순서로 진행된다

#파일을 열기 위해서는 open()이라는 함수 사용
#open("파일명","열기 모드",encoding="자습")
#2반째로 전달하는"열기 모드"에는 
#읽기(read,"r"), 쓰기(write,"w"),이어쓰기(append,"a") 약자로 사용
#읽기 모드 파일을 읽어오기 
#파일에 어떤 내용을 쓰기 위해서 쓰기나 이어쓰기 모드 사용
#동일한 이름의 파일이 있는 경우 쓰기 모드는 파일 덮어쓰게 되므로 기존 내용 삭제
#이어쓰기 모드는 파일의 내용 맨 밑에 이어서 쓴다는 차이점
#utf8로 설저하면 한글 포함 내용을 다룰떄도 문제 없음

from os import read

score_file = open("score.txt","w",encoding="utf8") # score.txt 파일을 쓰기("w") 모드로 열기
print("수학 : 0", file=score_file) # score.txt 파일에 내용 쓰기
print("영어 : 50", file=score_file) # score.txt 파일에 내용 쓰기
score_file.close() #score.txt 파일 닫기 
#close는 파일닫기
#파일을 열면 반드시 닫아야 한다

score_file = open("score.txt","a",encoding="utf8") #score.txt 파일을 쓰기("a") 모드로 열기
score_file.write("과학 : 80")
score_file.write("\n코딩 : 100") #write 는 줄바꿈 안해주기 떄문에 탈출문자(\n)로 줄바꿈
score_file.close()

#score_file = open("score.txt","r",encoding="utf8")
#print(score_file.read())# 파일 전체 읽어오기
#score_file.close()

#한 줄 한 줄 끊어서 읽어오기 readline()
# score_file = open("score.txt","r",encoding="utf8")
# print(score_file.readline(), end="") #줄별로 읽기. 한 줄 읽고 커서는 다음 줄로 이동
# print(score_file.readline(), end="") #줄바꿈 중복을 방지하기 위해 end="" 처리
# score_file.close

#score_file = open("score.txt","r",encoding="utf8")

# while True:
#     line = score_file.readline()
#     if not line: #더 이상 읽어올 내용이 없으면? 
#          break 
#     print(line,end="") # 읽어온 줄 출력

# score_file.close()        

score_file = open("score.txt","r",encoding="utf8")

lines = score_file.readlines() # 모든 줄을 읽어와서 list 형태로 저장
for line in lines:
    print(line,end="") 

score_file.close()


