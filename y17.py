# 編號：CANDY-017
# 程式語言：Python
# 題目：計算數字的 2 進位裡有幾個 1
# 範例：5 -> 101 -> 2 個 1


def count_bits(num):
    num = bin(num)[2:]
    one_count = num.count("1")

    return one_count


print(count_bits(1234))
# 5
print(count_bits(1450))
# 6
print(count_bits(9527))
# 8
