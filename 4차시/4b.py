'''

t1 = ()
n1, n2, n3 = input("숫자 3개를 입력하세요").split()

t1 = (n1,n2,n3)

#set_t1 = set(t1)
#set_t1.add(n1,n2,n3)


for i in range(len(t1)):

    if t1[i] > t1[i+1]:
        max = t1.index(i)

    elif t1[i] < t1[i+1]:
        max = t1.index(i+1)

    elif t1[i] == t1[i+1]:
        max = t1.index(i)

    i += 1



print(t1.index(max))

'''


n1, n2, n3 = map(int, input("숫자 3개를 입력하세요").split())

t1 = (n1,n2,n3)

print(t1.index(max(t1)))