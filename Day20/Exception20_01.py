# num1 = 10
# num2 = 0

# n3 = num1/num2  # ZeroDivisionError: division by zero

# n = input("정수를 입력하세요 >> ")
# n = int(n)
# print(n)  # 정수를 입력하지 않았을 때 ValueError 가 뜸


while True:
    try:
        n = input("정수를 입력하세요 >> ")
        n = int(n)
        print(n)  # while 문에 넣어두면 정수를 입력하지 않아도 종료되지 않음
        n = n/n
    except Exception:  # 에러를 모두 일일이 처리해줄 수 없으니 전체 예외를 처리해준다
        print("모든 예외처리")
    except ValueError:  # 에러가 뜨면 그냥 재시작이 아니라 경고문을 띄우고 재시작
        print("정수가 아닙니다.")
    except ZeroDivisionError:
        print("0으로 나눌 수 없습니다.")

