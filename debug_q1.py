
def numbers_less_than_twenty(list):
    b=[]
    d=[]
    for i in list:
        if i > 20:
            b.append(i)
        else:
            d.append(i)
    print(b)
    print(d)
num_list = [12, 312, 42, 123, 5, 12, 53, 75, 123, 62, 9]
numbers_less_than_twenty(num_list)
# d=[]
# b=[]
# for i in num_list:
#     if i>20:
#         d.append(i)
#     elif i<20:
#         b.append(i)
# print("greater than 20",d)
# print("less than 20",b)
