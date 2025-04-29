try:
    file_name = input("입력할 파일의 이름: ")
    f = open(file_name, "r")
    
except FileNotFoundError as e:
    print("{}파일이 존재하지 않습니다.". format(file_name))
else:
    s = f.read()
    print(s)
finally:
    try:
        f.close()
    
    except NameError:
        pass