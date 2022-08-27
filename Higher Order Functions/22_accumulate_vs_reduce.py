from itertools import accumulate
from functools import reduce
l=[1,2,3,4,5]
data_accu=list(accumulate(l,lambda x,y:x+y))
print(data_accu)
print(type(data_accu)) #<class 'list'>
data_redu=reduce(lambda x,y:x+y,l)
print(data_redu)
print(type(data_redu)) #<class 'int'>