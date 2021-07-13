#에러 발생시키기
#raise를 사용하여 에러가 발생시킨것처럼 할 수 있다
try:
    print("한 자리 숫자 나누기 전용 계산기입니다.")
    num1 = int(input("첫 번째 숫자를 입력하세요 : "))
    num2 = int(input("두 번째 숫자를 입력하세요 : "))
    if num1 >= 10 or num2 >= 10: #입력받은 수가 한 자리인지 확인
        raise ValueError
    print("{0} / {1} = {2} ".format(num1,num2,int(num1/num2)))
except ValueError:
    print("잘못된 값을 입력하였습니다. 한 자리 숫자만 입력하세요. ㅋㅋ")