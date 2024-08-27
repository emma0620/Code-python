# 編號：CANDY-016
# 程式語言：Python
# 題目：把原本 snake_case 的字轉換成 camelCase 格式
# 範例："hello_world" -> "helloWorld"


def to_camel_case(words):
    words = words.split("_")
    camel_case_string = words[0] + "".join(i.capitalize() for i in words[1:])
    return camel_case_string


print(to_camel_case("book"))
# book
print(to_camel_case("book_store"))
# bookStore
print(to_camel_case("get_good_score"))
# getGoodScore
