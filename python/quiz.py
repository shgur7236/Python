
class House:
    #매물 초기화 : 위치, 건물 종류, 매물 종류, 가격, 준공년도
    def __init__(self,location,house_type,deal_type,price,completion_year):
        self.location = location
        self.house_type = house_type
        self.deal_type = deal_type
        self.price = price
        self.completion = completion_year

    #매물 정보 펴시
    def show_detail(self):
        print(self.location,self.house_type,self.deal_type,self.price,self.completion)

Buildings = []
Building1 = House("강남","아파트","매매","10억","2010년")    
Building2 = House("마포","오프스텔","전세","5억","2007년")    
Building3 = House("송파","빌라","월세","500/50","2000년")   

Buildings.append(Building1)
Buildings.append(Building3)
Buildings.append(Building2)

print("총 {0}대의 매물이 있습니다. ".format(len(Buildings)))
for Building in Buildings:
    Building.show_detail()