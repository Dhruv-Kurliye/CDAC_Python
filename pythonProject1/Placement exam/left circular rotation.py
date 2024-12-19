

def left_circular(n):
    list = [1, 2, 3, 4, 5, 6]
    new_list = []
    for i in range(n):
        new_list.append(list[i])

        list.remove(list[i])

        list1=[]

    list.extend(new_list)
    print(list)


left_circular(1)