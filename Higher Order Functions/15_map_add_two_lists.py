l1=[10,20,30,40,50]
l2=[1,2,3,4,5]
l3=[50,40,30,20,10]
data=map(lambda x,y,z:x+y+z,l1,l2,l3)
#print(data) #<map object at 0x00000167195D32E0>
for i in data:
    print(i)