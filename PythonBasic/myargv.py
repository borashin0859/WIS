import sys

l=sys.argv

print(l[1:])
print(sum(list(map(lambda x:int(x),l[1:]))))
#print(sum(list(map(lambda x:int(x),l[1:]))))
