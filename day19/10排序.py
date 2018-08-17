# 排序
# 冒泡
# numbers = [34,26,77,100,1,20,-66,666]
# # 从小到大
# for i in range(len(numbers)-1):#需要比较几轮
#     for j in range(len(numbers)-1-i):  #比几次
#        if  numbers[j]  >  numbers[j+1]:
# #             交换位置
#             numbers[j],numbers[j+1] = numbers[j+1],numbers[j]
# print(numbers)

#[-66,1,20,26,30,34,77,99,100]
#二分法

import math
numbers = [34,26,77,100,1,20,-66,30,99]
def half_sort(list,base_number):
    i = 0

    middle_index = math.ceil(int(len(list)/2))
    list[middle_index] ,list[0]= list[0],list[middle_index]
    for j in range(len(list)-middle_index):
        #基数右边
        if base_number == list[-1]:
            pass
        elif base_number > list[list.index(base_number)+1]:
            list.insert(0,list.pop(list.index(base_number)+1))
        #基数左边
        if base_number == list[0]:
            pass
        elif base_number < list[list.index(base_number)-1]:
            list.append(list.pop(list.index(base_number)-1))
    half_sort(list,numbers[0])
    return list
half_sort(numbers,numbers[0])
print(numbers)

# list_ed = ["a","b","c","a","b","c","a","b","c"]
# def spilt_list(list):
#     base_number = list[0]
#     print(list_ed)
#     half_sort(list,base_number)
#     if len(list) >= 2:
#         if base_number == list[-1] :
#             left_list = list[:list.index(base_number)]
#             list_ed[list.index(base_number)]=base_number
#             return spilt_list(left_list)
#         if base_number == list[0]:
#             right_list = list[list.index(base_number) + 1:]
#             list_ed[list.index(base_number)] = base_number
#             return spilt_list(right_list)
#         left_list = list[:list.index(base_number)]
#         right_list = list[list.index(base_number) + 1:]
#         list_ed[list.index(base_number)] = base_number
#
#     else:
#         # print(list)
#         return
#
#     return spilt_list(list = left_list),spilt_list(list = right_list)


# 20,1,26,-66,30    -66,20,1,    1,20,-66  -66,20,1

# half_sort([30, -66, 20, 1])


# 选择
# numbers = [34,26,77,100,1,20,-66,666]
# for i in range(len(numbers)-1): #要取多少次
#     index = i
#     for j in range(i+1,len(numbers)):
#         if numbers[j] < numbers[index]:
#             index = j
#     numbers[i],numbers[index]= numbers[index],numbers[i]
#
# print(numbers)
# 插入

# numbers = [34,26,77,100,1,20,-66,666]
# for i in range(1,len(numbers)):
#     j = i - 1
#     if numbers[i] <  numbers[j]:
#         temp = numbers[i]
#         numbers[i] = numbers[j]
#
#         j = j -1
#         while j >= 0 and temp < numbers[j]:
#             numbers[j+1] = numbers[j]
#             j = j -1
#         numbers[j+1] = temp
# print(numbers)
#






