def fun(num,n):
    if num==n+1:
        return
    else:
        print(num)
        fun(num+1,n)
fun(1,5)