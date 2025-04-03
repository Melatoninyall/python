n = int(input("n을 입력하십시오"))

for i in range (n+1):
    
    if i % 7 == 0:
        continue
    elif i > 100:
        break
    else:
        print(i)