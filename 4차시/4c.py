
a, b, c = map(int, input().split())
d, e, f = map(int, input().split())


set1 = set([a, b, c])

set2 = set([d, e, f])

print (len(set1.intersection(set2)))