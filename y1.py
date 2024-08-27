# 編號：CANDY-001
# 程式語言：Python
# 題目：找出陣列裡最小的兩個值的總和


def sum_of_smallest_values(arr):
    arr.sort()
    return arr[0] + arr[1]


list1 = [19, 5, 42, 2, 77]
list2 = [23, 15, 59, 4, 17]

print(sum_of_smallest_values(list1))  # 印出 7
print(sum_of_smallest_values(list2))  # 印出 19


# // 編號：CANDY-001
# // 程式語言：JavaScript
# // 題目：找出陣列裡最小的兩個值的總和

# //陣列排序, 取二個小最小值
# function sumOfSmallestValues(arr) {
#   arr = arr.sort((a, b) => a - b);
#   return arr[0] + arr[1];
# }

# const list1 = [19, 5, 42, 2, 77];
# const list2 = [23, 15, 59, 4, 17];

# console.log(sumOfSmallestValues(list1));
# console.log(sumOfSmallestValues(list2));
