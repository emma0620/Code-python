# 編號：CANDY-023
# 程式語言：Python
# 題目：算出 N 個數字的最大公因數

from functools import reduce
from math import gcd


def calc_GCD(*numbers):

    return reduce(gcd, numbers)


print(calc_GCD(10))
# 10
print(calc_GCD(103, 27))
# 1
print(calc_GCD(21, 15, 18))
# 3
print(calc_GCD(104, 96, 36, 88))
# 4

# 遍歷每個數字，依次計算與結果的最大公因數
# const findGCD = numbers.reduce((acc, curr) => {
#  console.log("acc: " + acc + "  curr:" + curr);
#  return GCDOfTwo(acc, curr);
# });
