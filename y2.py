# 編號：CANDY-002
# 程式語言：Python
# 題目：請寫一小段程式，印出連續陣列裡缺少的字元


chars1 = ["a", "b", "c", "d", "f", "g"]
chars2 = ["O", "Q", "R", "S"]


def find_lost_letter(chars):
    first_code = ord(chars[0])

    lost_word = [
        chr(first_code + index)
        for index in range(len(chars))
        if chr(first_code + index) not in chars
    ]

    return lost_word


print(find_lost_letter(chars1))
# 印出 e
print(find_lost_letter(chars2))
# 印出 P


# first_code = ord(chars[0])
# for i in range(len(chars)):
#     if first_code + i != ord(chars[i]):
#         return chr(first_code + i)
# return None

#
#   for (let i = 0; i < chars.length; i++) {
#     if (firstCode + i !== chars[i].charCodeAt()) {
#       return String.fromCharCode(firstCode + i);
#     }
#   }
#   return null;
