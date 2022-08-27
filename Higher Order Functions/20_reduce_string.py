from functools import reduce
l=['disha','sita','ram','ria']
data=reduce(lambda x,y:x+y,l)
print(data)
#print(type(data)) #<class 'str'>