#finally
#try를 벗어나는 시점에 무조건 실행되는 구문
#맨 끝에 정의

class BigNumberError(Exception): # 사용자 정의 에러
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg

try:
    print("한 자리 숫자 나누기 전용 계산기입니다.")
    num1 = int(input("첫 번째 숫자를 입력하세요: "))
    num2 = int(input("두 번째 숫자를 입력하세요: "))
    if num1 >= 10 or num2 >= 10: # 입력받은 수가 한 자리인지 확인
        raise BigNumberError("입력값 : {0}, {1}".format(num1, num2)) # 자세한 에러 메시지
    print("{0} / {1} = {2}".format(num1, num2, int(num1 / num2)))
except ValueError:
    print("잘못된 값을 입력하였습니다. 한 자리 숫자만 입력하세요.")
except BigNumberError as err:
    print("에러가 발생하였습니다. 한 자리 숫자만 입력하세요.")
    print(err) # 에러 메시지 출력
finally: # 에러 발생 여부 상관없이 항상 실행
    print("계산기를 이용해 주셔서 감사합니다.")

#일반적으로 try구문 내에서 파일이나 자원을 사용한 경우
#finally 구문에서 열린 파일을 닫거나 자원을 해제하는 작업 수행