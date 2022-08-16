def fun(num,n):
    if num==n+1:
        return
    else:
        fun(num+1,n)
        print(num)
fun(1,5)