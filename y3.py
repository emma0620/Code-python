#  編號：CANDY-003
#  程式語言：python
#  題目：完成函數的內容，把陣列裡的 0 都移到最後面

list = ["false", 1, 0, -1, 2, 0, 1, 3, "a"]


def move_zeros_to_end(arr):
    zero = [n for n in arr if n == 0]
    arr = [n for n in arr if n != 0]

    arr = arr.extend(zero)
    return arr


result = move_zeros_to_end(list)
print(result)  # 印出 [false, 1, -1, 2, 1, 3, "a", 0, 0]


#   const findzeroArr = arr.filter((item) => item === 0);
#   return arr.filter((item) => item !== 0).concat(findzeroArr);

#   // const findzeroArr = arr.filter((item) => item === 0);
#   // arr = arr.filter((item) => item !== 0);
#   // const newArr = arr.concat(findzeroArr);
#   // return newArr;
