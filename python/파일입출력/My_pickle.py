#pickle
#프로그램에서 사용하고 있는 데이터를 파일 형태로 저장하거나 불러올 수 있게 해주는 모듈

#데이터를 파일로 저장 dump() 함수 사용
#dump(data,dest_file)

#pickle을 이용해서 저장되는 파일은 바이너리 형태
#open() 함수를 이용할 떄 "wb"라고 해야 저장이 된다. encoding은 지정할 필요가 없다

import pickle 
 
profile_file = open("profile.pickle","wb") #바이너리 형태로 저장
profile = {"이름":"박명수","나이":30,"취미":["축구","골프","코딩"]}
print(profile)

pickle.dump(profile,profile_file) #profile 데이터를 file에 저장
profile_file.close

#load는 파일을 다시 불러오기
profile_file = open("profile.pickle","rb") 
profile = pickle.load(profile_file) #file 에 있는 정보를 불러와서 profile 에 저장

print(profile)
profile_file.close()











