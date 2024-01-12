def selection_sort(list):
    list_len = len(list)
    for i in range(list_len):
        min_value = i
        for j in range(i+1, list_len):
            if list[j] < list[min_value]:
                min_value = j
        list[i], list[min_value] = list[min_value], list[i]
    return list
print(selection_sort([9,4,5,2,8,6,1,3,10,7,2000]))