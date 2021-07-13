from random import *
words =["apple","orange","banana"] 
word = choice(words) # 랜덤으로 단어 중 1개를 선택
# print("answer : " +word) # 참고용으로 정잡 출력 (실제 게임에서는 지우기)
letters = "" # 플레이어가 지금까지 입력한 알파벳들 저장

while True:
    succed = True 
    print()
    for w in word: # 제시 단어를 알페벳별로 한 글자씩 비교
        if w in letters: # 현재 알파벳이 플에이어가 입력한 값들 중에 있으면
            print(w,end=" ") # 그 알파벳을 표시
        else:
            print("_",end=" ") # 밑줄을 표시
            succed = False
    print()

    if succed: # 만약 성공했다면 게임 종료
        print("Success")
        break

    letter = input("Input letter > ") # 플레이어로부터 한 글자씩 입력
    if letter not in letters: # 입력값 중에 포함되어 있지 않다면
        letters += letter # 새로 입력받은 글자를 입력값에 추가

    if letter in word: # 입력한 글자가 제시 단어에 포함되었다면
        print("Correct")
    else: 
        print("Wrong")