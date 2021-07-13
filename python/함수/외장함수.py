#외장함수
#외장함수를 사용하기 위해서는 반드시 해당모듈을 import 해야 한다

#glob
#어떤 경로 내의 폴더 또는 파일의 목록을 조회할 때 사용한다

# import glob
# print(glob.glob("*.py")) # 확장자가 py인 모든 파일

import os
# print(os.getcwd()) # 현재 디렉토리

# folder = "sample_dir"

# if os.path.exists(folder): #폴더가 존재한다면
#     print("이미 존재하는 폴더입니다.")
#     os.rmdir(folder) # 폴더 삭데
#     print(folder,"폴더를 삭제하였습니다.")
# else: # 폴더가 존재하지 않으면
#     os.makedirs(folder) # 폴더 생성
#     print(folder,"폴더를 생성하였습니다.")

# print(os.listdir())

# import time
# print(time.strftime("%Y-%m-%d %H:%M:%S")) # 연-월-일 시:분:초

import datetime
print("오늘 날짜는", datetime.date.today())
today = datetime.date.today() # 오늘 날짜 저장
td = datetime.timedelta(days=100) # 100일 저장
print("우리가 만난지 100일은",today+td) # 오늘부터 100일 후