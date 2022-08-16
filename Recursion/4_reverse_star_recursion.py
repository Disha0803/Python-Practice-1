def star(num,n):
    print('*'*num)
    if num==1:
        return num
    else:
        star(num-1,n)
star(5,1)