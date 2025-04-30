n = input("학생 수 입력: ")

name = ()
name = input("이름 입력: ").split()

sorted_names = sorted(name, key = lambda x: (len(x), x))

for i in range(len(sorted_names)):
    print ("", sorted_names[i], end = " ")