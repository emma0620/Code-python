# 編號：CANDY-014
# 程式語言：Python
# 題目：把鄰近的重複值去除，但仍照原本的順序排序
# 範例："AAABBBDDDAABBBCC" -> ['A', 'B', 'D', 'A', 'B', 'C']


def unique_order(sequence):
    new_sequence = []
    for i in range(len(sequence)):
        if i == 0 or sequence[i] != sequence[i - 1]:
            new_sequence.append(sequence[i])
    return new_sequence


print(unique_order("AABCC"))
# [ 'A', 'B', 'C']
print(unique_order("AAABBBCCBCC"))
# [ 'A', 'B', 'C', 'B', 'C']
print(unique_order([1, 2, 1, 2, 1]))
# [ 1, 2, 1, 2, 1 ]
print(unique_order([1, 1, 1, 2, 2, 2, 1]))
# [1, 2, 1]
