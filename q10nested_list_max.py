marks = [[45, 21, 42, 63], [12, 42, 42, 53], 
[42, 90, 78, 13], [94, 89, 78, 76], [87, 55, 98, 99]]
for i in range (len(marks)):
    max=0
    for j in range(len(marks[i])):
        if marks[i][j]>max:
            max=marks[i][j]
    print(max)

