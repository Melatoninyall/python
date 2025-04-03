n = int(input("n입력"))

stu = {}

for i in range(n):
    name, score = input("이름과 성적을 입력하세요").split()
    stu [name] = score
    i +=1

print(stu)

stu_name = input("점수를 알고싶은 학생을 입력하세요")

print(stu[stu_name])