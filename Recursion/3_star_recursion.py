def star(num,n):
    print('*'*num)
    if num==n:
        return num
    star(num+1,n)
star(1,5)