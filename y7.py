# 編號：CANDY-007
# 程式語言：Python
# 題目：在某個數字陣列裡，可能藏有某個不合群的奇數或偶數，試著找出它！


def find_Some_different(numbers):
    odd_count = [n for n in numbers if n % 2 != 0]
    even_count = [n for n in numbers if n % 2 == 0]

    if len(odd_count) > len(even_count):
        return even_count[0]
    else:
        return odd_count[0]


print(find_Some_different([2, 4, 0, 100, 4, 11, 2602, 36]))
# 印出 11
print(find_Some_different([160, 3, 1719, 19, 11, 13, -21]))
# 印出 160
