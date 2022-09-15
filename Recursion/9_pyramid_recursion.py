def star(num,n):
    k=n-num
    print(' '*k,end=' ')
    print(" * "*num)
    if num==n:
        return num
    star(num+1,n)
star(1,5)