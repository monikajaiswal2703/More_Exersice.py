# i=int(input("enter the number"))
# a=1
# while(i>0):
#     a*=i
#     i-=1
# print(a)
# a=[1,2,3,4]
# for i in range(a):
#     print(sum(a[i]))


# sum=0
# i=0
# while i<len(a):
#     sum+=a[i]
#     d.append(sum)
#     i+=1
# print(d)
i=1
d=[]
while i<=10:
    n=int(input("enter the number"))
    d.append(n)
    i+=1
print(d)
max=0
i=0
while i<len(d):
    if d[i]>max:
        max=d[i]
    i+=1
print(max)