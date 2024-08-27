# 編號：CANDY-024
# 程式語言：Python
# 題目：算出 N 個數字的最小公倍數
# 提示：可使用 023 計算最大公因數的函數
from functools import reduce
from math import gcd


def calc_LCM(*numbers):

    def LCM_of_two(a, b):
        return abs(a * b) // gcd(a, b)

    return reduce(LCM_of_two, numbers)


print(calc_LCM(10))
# 10
print(calc_LCM(103, 27))
# 2781
print(calc_LCM(21, 15, 18))
# 630
print(calc_LCM(104, 96, 36, 88))
# 41184

# 使用 reduce 將數字縮減為最小公倍數
# return numbers.reduce((acc, num) => findLCM(acc, num), 1);
