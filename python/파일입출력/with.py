#with
#with는 파일을 열고 나서 closed()를 호출하지 않아도 자동으로 닫아주는 역할
import pickle

with open("profile.pickle","rb") as profile_file:
    print(pickle.load(profile_file))


with open("study.txt","w",encoding="utf8") as study_file:
    study_file.write("파이썬을 열심히 공부하고 있어요")

#with를 사용하면 파일을 읽고 쓰는 코드도 간결해지고,
#close()함수를 안써도 된다.


