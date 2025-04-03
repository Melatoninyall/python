def fac(n):
    if n == 0:
        return 1
    else:
        return n * fac(n-1)
    

n = int(input("정수N 입력"))

print(fac(n))

