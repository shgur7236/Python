
#마린 : 공격 유닛, 군인. 총을 쏠 수 있음
# name = "마린" #유닛의 이름
# hp = 40 # 유닛의 이름
# damage = 5 #유닛의 공격력

# print("{} 유닛이 생성되었습니다.".format(name))
# print("체력 {0}, 공격력 {1}\n".format(hp,damage))

# tank_name = "tank"
# tank_hp = 150
# tank_damage = 35

# print("{} 유닛이 생성되었습니다.".format(tank_name))
# print("체력 {0}, 공격력 {1}\n".format(tank_hp,tank_damage))

# tank2_name = "tank"
# tank2_hp = 150
# tank2_damage = 35

# print("{} 유닛이 생성되었습니다.".format(tank2_name))
# print("체력 {0}, 공격력 {1}\n".format(tank2_hp,tank2_damage))

# def attack(name, location, damage):
#     print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 {2}]".format(name,location,damage))

# attack(name,"1시",damage) #마린 공격 명령
# attack(tank_name,"1시",tank_damage) #탱크 공격 명령
# attack(tank2_name,"1시",tank2_damage) #탱크2 공격 명령

#클래스
#중요한 개념이다 그래서 어렵다
#보통 서로 연관이 있는 변수와 함수의 집합으로 이루어짐
#clss 클래스명 : 
#  def메소드1(self,전달값1,전달값2,...) 메소드는 클래스 내에서 정의되는 함수 일반 함수랑 동일
#  실행명령문 1
#   ...

class Unit:
    def __init__(self,name,hp,damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{0} 유닛이 생성되었습니다.".format(self.name))
        print("체력 {0}, 공격력{1}".format(self.hp,self.damage))

marien1 = Unit("마린",40,5)
marien2 = Unit("마린",40,5)
tank = Unit("탱크",150,35)

#정리
#클래스는 서로 관련이 있는 변수(멤버변수) 와 함수 (메소드)들의 집합