list1 = [1, 342, 75, 23, 98,45,12,34]
list2 = [75, 23, 98, 12, 78, 10, 1]
d=[]
l=list1+list2
for i in l:
    c=0
    for j in l:
        if i==j:
            c+=1
    if c>=2:
        d.append(i)
    e=[]
    for i in d:
        if i not in e:
            e.append(i)
print(e)

