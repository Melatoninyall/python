n = int(input("1에서 100까지의 정수 중 한가지를 고르시오"))

for i in range (n+1) :
    if i % 3 == 0 and i != 0:
        print(i)
        i += 1
