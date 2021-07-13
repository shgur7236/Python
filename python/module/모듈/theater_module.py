#모듈
#함수 정의나 클래스 등 서로 관련이 있거나 비슷한 기능을 하는 
#파이썬 문장들을 담고 있는 파일을 모듈 이라고 한다.

#일반 가격
def price(people):
    print("{0}명 가격은 {1}원 입니다.".format(people,people * 10000))

#조조 할일 가격
def price_morning(people):
    print("{0}명 조조 할인 가격은 {1}원 입니다.".format(people,people * 6000))

#군인 할인 가격
def price_soldier(people):
    print("{0}명 군인 할인 가격은 {1}원 입니다.".format(people,people * 4000))

