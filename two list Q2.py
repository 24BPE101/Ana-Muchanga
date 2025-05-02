list1 = [1,2,3,4,5,6]
list2 = [6,5,4,3,2,1]

m = map(lambda x,y:x+y, 11,12)
print(list(m))








another way
print(list(map(lambda x,y:x+y,[1,2,3,4,5,6],[6,5,4,3,2,1])))
