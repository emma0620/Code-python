# 編號：CANDY-005
# 程式語言：Python
# 題目：完成函數的內容，把傳進去的數字的每個位數平方之後組合在一起


# 將數值轉成字串, 拆出每個位數進行平方運算，並組合成新數字字串
def square_digits(num):
    num_str = str(num)
    square_num = "".join(str(int(x) ** 2) for x in num_str)
    return int(square_num)


print(square_digits(3212))
# 印出 9414
print(square_digits(2112))
# 印出 4114
print(square_digits(387))
# 印出 96449


# 將數字轉換為字符串，以便逐位處理
# num_str = str(num)
# 將每一位數字轉換為整數，平方，然後轉回字符串
# squared_str = ''.join(str(int(digit) ** 2) for digit in num_str)
# 將結果字符串轉換回整數
# return int(squared_str)

# squared_num = lambda num: int(''.join(str(int(digit) ** 2) for digit in str(num)))

# squared_num = lambda num: int(''.join(map(lambda digit: str(int(digit) ** 2), str(num))))


# num.toString()：將數字轉換為字串。
# .split('')：將字串拆分為字元陣列，每個字元代表一個位數。
# .map(digit => digit * digit)：對每個位數進行平方運算，digit * digit 直接計算每個位數的平方。
# .join('')：將平方後的數字陣列組合成一個新的字串
