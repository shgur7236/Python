#리스트
#지하철 칸별로 10명,20명,30명
#subway1 = 10
#subway2 = 20
#subway3 = 30

#subway = ["유재석","조세호","박명수"] 
#print(subway.index("조세호")) 

#하하씨가 다음 정류장에서 다음 칸에 탐
#subway.append("하하") # append 추가 
#print(subway) 
#정현돈씨를 유재석 / 조세호 사이에 태움
#subway.insert(1,"정현돈") # 인덱스 1위치에 추가 insert는 삽입
#print(subway)
#subway.insert(0,"노혁")
#print(subway)

#지하철에 있는 사람을 한 명씩 뒤에서 꺼냄
#print(subway.pop()) #이거는 누가 꺼내지는지 출력
#print(subway) 
#print(subway.pop()) # 한명 더 내림
#print(subway)

#같은 이름의 사람이 몇 명있는지 확인
#subway.append("노혁")
#print(subway) # 노혁이 2명
#print(subway.count("노혁")) # count의 안에 수를 출력

#num_list = [5,2,4,3,1]

#num_list.sort() #오름차순 정렬 
#print(num_list) 
#num_list.reverse() #순서 뒤집기
#print(num_list)
#num_list.clear() #모두 지우기
#print(num_list)

#mix_list = ["노혁",15,True] # 다양한 자료형을 함께 사용 가능
#print(mix_list) 

#num_list = [5,2,4,3,1] # num_list 값 다시 정의
#num_list.extend(mix_list) # 리스트 확장 extend()를 사용하면 괄호 안에 있는 것을 확장할수 있음
#print(num_list) 



#사전
#사전에는 key와 value가 있다

#예제 멤버들이 목용탐에 가서 각자 사물함 key를 받고 사물함을 이용
#cabinet = {3:"유재석",100:"김태호"} # 대괄호 속에 key 값을 넣는다
#print(cabinet[3]) # key3에 해당하는 value
#print(cabinet.get(3)) # get을 이용하는 방법
#print(cabinet[5]) # key가 5인 값이 없을 땐 에러 발생 후 프로그램 종료
#print(cabinet.get(5)) # key가 5인 값이 없을 땐 None 반환 후 계속 진행
#print(cabinet.get(5,"사용 가능")) # key에 해

#사전 자료형에 값이 있는지 여부 확인
#print(3 in cabinet) #True false로 판단
#print(5 in cabinet) 

#key는 정수형이 아닌 문자열도 가능
#cabinet = {"A-3":"유재석","B-100":"김대호"}
#print(cabinet["A-3"]) # 유재석
#print(cabinet["B-100"]) # 김대호

#업데이트 또는 추가
#print(cabinet)
#cabinet["A-3"] = "김종국"
#cabinet["C-20"] = "조세호"
#print(cabinet) 

#삭제
#del cabinet["A-3"] # key "A-3"에 해당하는 데이터 삭제
#print(cabinet) 

#key들만 출력
#print(cabinet.keys()) 
#value들만 출력
#print(cabinet.values()) 
#key,value 쌍으로 출력
#print(cabinet.items()) 

#전체 삭제
#cabinet.clear()
#print(cabinet)