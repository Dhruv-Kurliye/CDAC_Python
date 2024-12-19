def Armstrong(n):
    a=str(n)
    sum=0
    for i in range(len(a)):
     sum+=int(a[i])**len(a)

    if sum==n:
        print("Armstrong Number")
    else:
        print("Not an Armstrong Number")

Armstrong(153)