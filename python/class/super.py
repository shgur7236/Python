#super
#다중 상속일 경우에는 가장 먼저 상속받은 클래스로 접근

# 일반 유닛
class Unit:
    def __init__(self, name, hp, speed): # speed 추가
        self.name = name
        self.hp = hp
        self.speed = speed # 지상 이동 속도

    def move(self,location): # 이동 함수 정의
        print("[지상 유닛 이동]")
        print("{0} : {1} 방향으로 이동합니다. [속도 {2}]" \
            .format(self.name,location,self.speed))

# 공격 유닛
class AttackUnit(Unit):
    def __init__(self, name, hp, speed, damage): # speed 추가
        Unit.__init__(self, name, hp, speed) # speed 추가
        self.damage = damage

    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 {2}]" \
            .format(self.name, location, self.damage))

    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))    

#날 수 있는 기능을 가진 클래스
class Flyable:
    def __init__(self,flying_speed): # 공중 이동 속도
        self.flying_speed = flying_speed

    def fly(self,name,location): # 유닛 이름, 이동 방향
        print("{0} : {1} 방향으로 날아갑니다.[속도 {2}]" \
            .format(name,location,self.flying_speed))

# 공중 공격 유닛
class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage) # 지상 speed 0
        Flyable.__init__(self, flying_speed)
        
    def move(self,location): #unit 클래스의 move() 메소드를 새롭게 정의 (오버라이딩)
        print("[공중 유닛 이동]")
        self.fly(self.name,location)        
 
# 벌쳐 : 지상 유닛, 기동성이 좋음
vulture = AttackUnit("벌쳐",80,10,20) #지상 speed 10

#배트크루저 : 공중 유닛, 체력도 굉장히 좋음, 공격력도 좋음
battlecruiser = FlyableAttackUnit("배틀크루저",500,25,3)

vulture.move("11시")
#battlecruiser.fly(battlecruiser.name,"9시")
battlecruiser.move("9시") # 오버라이딩된 move() 호출

class BuildingUnit(Unit):
    def __init__(self,name,hp,location):
        super().__init__(name,hp,0) # 부모 클래스(Unit) 접근. self 없이 사용
        self.location = location

#서플라이 디폿: 건물, 1개 건물 = 8유닛
supply_depot = BuildingUnit("서플라이 디폿",500,"7시") #체력 500, 생성위치 7시

def game_start():
    print("[알림] 새로운 게임을 시작합니다.")

def game_over():
    pass

game_start()
game_over()

