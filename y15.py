# 編號：CANDY-015
# 程式語言：Python
# 題目：把原本的字串拆解成 2 個字元一組，若不足 2 個字則補上底線
# 範例：
#      "abcdef" -> ['ab', 'cd', 'ef']
#      "abcdefg" -> ['ab', 'cd', 'ef', 'g_']


def split_string(str):
    split_str = []
    pair = ""

    for i in range(0, len(str), 2):
        pair = str[i : i + 2]

        if len(pair) == 1:
            pair = pair + "_"

        split_str.append(pair)

    return split_str


print(split_string("abcdef"))
# ["ab", "cd", "ef"]
print(split_string("abcdefg"))
# ["ab", "cd", "ef", "g_"]
print(split_string(""))
# []
