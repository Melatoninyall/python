try:
    a = input("첫 번째 숫자: ")
    b = input("두 번째 숫자: ")
    a = int(a)
    b = int(b)
    c = input("연산자(+, -, *, /): ")
except ValueError:    
    print("숫자만 입력 가능합니다.")
except ZeroDivisionError:
    print("0으로 나눌 수 없습니다.")
else:
    if c == "+":
        print("결과: ", int(a + b))
    elif c == "-":
        print("결과: ",int(a - b))
    elif c == "*":
        print("결과: ",int(a * b))
    elif c == "/":
        print("결과: ",int(a / b))
finally:
    print("종료")