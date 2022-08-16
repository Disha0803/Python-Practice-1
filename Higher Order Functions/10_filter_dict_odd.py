d={
    1:'suresh',
    2:'mahesh',
    3:'rakesh',
    4:'bristhi',
    5:'misthi',
    6:'sristhi'
}
print("People with odd roll numbers:")
print(list(filter(lambda x:x[0]%2 != 0,d.items())))
print("People with even roll numbers:")
print(list(filter(lambda x:x[0]%2 == 0,d.items())))