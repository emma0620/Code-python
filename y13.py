# 編號：CANDY-013
# 程式語言：Python
# 題目：根據台灣財政部所提供的公司統編驗證規則，計算統一編號是否正確
# https://www.fia.gov.tw/singlehtml/3?cntId=c4d9cff38c8642ef8872774ee9987283


def is_valid_vat_number(vat):
    ID_num = str(vat)
    logical_num = [1, 2, 1, 2, 1, 2, 4, 1]

    if ID_num[6] != "7" or len(ID_num) == 8:
        for i in range(len(ID_num)):
            logical_num[i] *= int(ID_num[i])
            if logical_num[i] > 9:
                logical_num[i] = sum(int(n) for n in str(logical_num[i]))

    logical_sum = sum(logical_num)
    return logical_sum % 5 == 0


print(is_valid_vat_number("10458575"))
# true
print(is_valid_vat_number("88117125"))
# true
print(is_valid_vat_number("53212539"))
# true
print(is_valid_vat_number("88117126"))
# false
