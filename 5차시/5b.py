'''

1번 문장을 입력하세요: 안녕하세요
2번 문장을 입력하세요: 안녕하세요
2번 문장을 입력하세요: 안녕하세요
안녕하세요
해달 부트캠프 파이썬 분반
파이팅

'''

str1 = input("1번 문장을 입력하세요: ")
str2 = input("2번 문장을 입력하세요: ")
str3 = input("3번 문장을 입력하세요: ")

f = open('test.txt', "w")
f.write(str1 + "\n")
f.write(str2 + "\n")
f.write(str3 + "\n")
f = open('test.txt', "r")
s = f.read()
print(s)
f.close()

