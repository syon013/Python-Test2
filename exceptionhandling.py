# try:
#     print("나누기 전용 계산기입니다.")
#     nums = []
#     nums.append(int(input("첫번째 숫자를 입력하세요 : ")))
#     nums.append(int(input("두번째 숫자를 입력하세요 : ")))
#     print("{0} / {1} = {2}".format(nums[0], nums[1], nums[2]))

# except ValueError:
#     print("에러! 잘못된 값을 입력하였습니다.")

# except ZeroDivisionError as err:
#     print(err)

# except Exception as err:
#     print("알 수 없는 에러가 발생하였습니다.")
#     print(err)


# class BigNumberError(Exception):
#     def __init__(self, msg):
#         self.msg = msg

#     def __str__(self):
#         return self.msg

# try:
#     print("한 자리 숫자 나누기 전용 계산기입니다.")
#     unm1 = int(input("첫 번째 숫자를 입력하세요 : "))
#     unm2 = int(input("두 번째 숫자를 입력하세요 : "))
#     if unm1 >= 10 or unm2 >= 10:
#         raise BigNumberError("입력값 : {0}, {1}".format(unm1, unm2))
#     print("{0} / {1} = {2}".format(unm1, unm2, int(unm1/unm2)))

# except ValueError:
#     print("잘못된 값을 입력하셨습니다. 한 자리 숫자만 입력하세요.")

# except BigNumberError as err:
#     print("에러가 발생하였습니다. 한 자리 숫자만 입력하세요.")
#     print(err)
# finally:
#     print("계산기를 이용해 주셔서 감사합니다.")

# Quiz) 동네에 항상 대기 손님이 있는 맛있는 치킨집이 있습니다.
# 조건1 : 1보다 작거나 숫자가 아닌 입력값이 들어올 때는 ValueError로 처리
#        출력 메시지 : "잘못된 값을 입력하였습니다."
# 조건2 : 치킨집 주문 가능한 총량은 10마리로 한정
#       치킨 소진 시 사용자 정의 에러[SoldOutError]를 발생시키고 프로그램 종료
#       출력 메시지 : "재고가 소진되어 더 이상 주문을 받지 않습니다."

# [코드]

class soldOutError(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg


try:
    chicken = 10
    waiting = 1 # 홀 안에는 현재 만석. 대기번호 1부터 시작

    while(True):
        print("[남은 치킨 : {0}]".format(chicken))
        order = int(input("치킨 몇 마리 주문하시겠습니까?"))
        if order > chicken:
            print("재료가 소진되었습니다.")

        elif order < 1 or order > 10: # 남은 치킨보다 주문량이 많을 때
            raise ValueError
        
        else:
            print("[대기번호 {0}] {1} 마리 주문이 완료되었습니다."\
                .format(waiting, order))
            waiting += 1
            chicken -= order


        if chicken == 0:
            raise soldOutError("재고가 소진되어 더 이상 주문을 받지 않습니다.")
        
except ValueError:
    print("잘못된 값을 입력하였습니다.")

except soldOutError:
    print("재고가 소진되어 더 이상 주문을 받지 않습니다.")
    