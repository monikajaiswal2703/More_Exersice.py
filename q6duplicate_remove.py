# s = ["Rishabh", "Rishabh", "Abhishek", "Rishabh", "Divyashish", "Divyashish"]
# s= ["Delhi", "Delhi", "Mumbai", "Mumbai", "Delhi", "Chennai", 'Chennai']
# d=[]
# for i in range(len(s)):
#     if s[i] not in d:
#         d.append(s[i])
# print(d)

i=5
while i>=1:
    b=1
    while b<=5-i:
        print(" ",end=" ")
        b+=1
    j=1
    while j<=i:
        print("*",end=" ")
        j+=1
    print()
    i-=1
