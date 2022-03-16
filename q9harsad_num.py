def is_harshad_number(n):
    sum=0
    c=n
    while c>0:
        r=c%10
        sum+=r
        c//=10
    if n%sum==0:
        return True
    else:
        return False
n=int(input("enter the number"))
print(is_harshad_number(n))

print(9//10)