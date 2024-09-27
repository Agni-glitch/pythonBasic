s={1,2,5,6}
s2={3,6,7}
print(s.union(s2))#{1, 2, 3, 5, 6, 7}
print(s.intersection(s2))#{6}
print(s.symmetric_difference(s2))#{1, 2, 3, 5, 7}
print(s.isdisjoint(s2))#False
print(s.issubset(s2))#False
print(s.issuperset(s2))#False
s.update(s2)
print(s)#{1, 2, 3, 5, 6, 7}
s.add(8)#{1, 2, 3, 5, 6, 7, 8}
# s.remove(4)#error
s.discard(3)
if 8 in s:
    print(True)
item=s.pop()
print(item)#1
s.clear()
del s