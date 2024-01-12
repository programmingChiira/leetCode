def bubble_sort(list):
    list_len = len(list)
    for i in range(list_len):
        for j in range(i+1, list_len):
            if list[i] > list[j]:
                list[j], list[i]  = list[i], list[j]
    return list
print(bubble_sort([9,4,5,2,8,6,1,3,10,7,2000]))