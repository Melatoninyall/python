age = int(input("0에서 120까지의 나이를 입력하세요"))

if 0 <= age <= 12:
    print("500원")

elif 13<= age <= 18:
    print("1000원")

elif 19 <= age <= 64:
    print("2000원")

elif 64 <= age <=120:
    print("무료료")

else:
    print("잘못된 입력입니다")