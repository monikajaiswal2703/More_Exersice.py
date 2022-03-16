# output=new_list = [1, 2, 5, 10, 12, 13, 16, 20]

list1 = [1, 5, 10, 12, 16, 20]
list2 = [1, 2, 10, 13, 16]
l=list1+list2
# print(l)
list=[]
for i in l:
    if i not in list:
        list.append(i)
print(list)
# b=[]
# for i in list:
#     for j in list:
#         if i>j:
#             i,j= j,i
#             b.append(j)
#     print(b) 