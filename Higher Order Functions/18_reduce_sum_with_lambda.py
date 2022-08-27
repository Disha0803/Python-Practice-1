from functools import reduce
l=[1,2,3,4,5]
data=reduce(lambda x,y:x+y,l)
print(data)
#print(type(data)) #<class 'int'>