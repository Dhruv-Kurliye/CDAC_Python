# write a program tp print if the sum of the digits of elements in an array is even or odd

list=[123,51,76,87,4331]
new_l=[]

for l in list:
    sum_a = 0
    a=str(l)
    for i in a:
        sum_a+=int(i)

    if sum_a%2==0:
        new_l.append("Even")
    else:
        new_l.append("Odd")
print(new_l)