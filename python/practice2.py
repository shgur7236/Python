# import theater_module  # theater_module을 가져다가 사용
# theater_module.price(3) # 3명이 영화 보러 갔을 때 가격
# theater_module.price_morning(4) # 4 명이 조조 영화 보러 갔을 때
# theater_module.price_soldier(5) # 5명이 군인 영화 보러 갔을 떄

#as 를 사용하여 짧게
# import theater_module as mv # theater_module을 가져다가 사용
# mv.price(3) # 3명이 영화 보러 갔을 때 가격
# mv.price_morning(4) # 4 명이 조조 영화 보러 갔을 때
# mv.price_soldier(5) # 5명이 군인 영화 보러 갔을 떄

#from을 써서 짧게
# from theater_module import * # theater_module 내에서 모든 것을 가져다가 사용
# price(3) # theater_module. 필요 없음
# price_morning(4)
# price_soldier(5)

# from theater_module import price, price_morning # 모듈에서 일부만 가져다가 사용
# price(5) # 이번에는 5명
# price_morning(6)
# # price_soldier(7) # import 하지 않았으므로 사용 불가

#from theater_module import price_soldier as price # price_soldier 를 새로운 별명의 price
#price(5) # price_soldier() 를 호출