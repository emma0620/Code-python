# 編號：CANDY-008
# 程式語言：Python
# 題目：傳入一字串，計算得分最高的字
# 英文字母 a 得 1 分、b 得 2 分、c 得 3 分，以此類推。
# 所有傳入的字都是小寫。


def highest_score_word(input):
    character = input.split(" ")
    print(f"vocabulary {character}")
    max_score = 0
    max_word = ""
    for word in character:
        word_score = sum(ord(w) - 96 for w in word)
        print(f" {word} : {word_score}")
        if word_score > max_score:
            max_score = word_score
            max_word = word

    return max_word


print(highest_score_word("lorem ipsum dolor sit amet"))
# 印出 ipsum
print(highest_score_word("heyn i need a rubygem up to build this"))
# 印出 rubygem
print(highest_score_word("in time machine there are some bugs"))
# 印出 there
