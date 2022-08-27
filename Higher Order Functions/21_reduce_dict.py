from functools import reduce
d={
    1:'disha',
    2:'sita',
    3:'ram',
    4:'ria'
}
print(reduce(lambda x,y:x+y,d.keys()))
print(reduce(lambda x,y:x+y,d.values()))