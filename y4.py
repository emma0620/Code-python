# 編號：CANDY-004
# 程式語言：Python
# 題目：完成函數的內容，把傳進去的秒數變成平常人類看的懂的時間格式

# 秒為總秒數除以的餘數, 分為除以小時的餘數, 秒為除以60秒的餘數
import math

def human_readable_timer(seconds):
    secs = str(seconds % 60)
    minutes = str(math.floor((seconds % 3600) / 60))
    hours = str(math.floor(seconds / 3600))
    return f"{hours:0<2}:{minutes:0<2}:{secs:0<2}"


print(human_readable_timer(0))
# 印出 00:00:00
print(human_readable_timer(59))
# 印出 00:00:59
print(human_readable_timer(60))
# 印出 00:01:00
print(human_readable_timer(90))
# 印出 00:01:30
print(human_readable_timer(3599))
# 印出 00:59:59
print(human_readable_timer(3600))
# 印出 01:00:00
print(human_readable_timer(45296))
# 印出 12:34:56
print(human_readable_timer(86399))
# 印出 23:59:59
print(human_readable_timer(86400))
# 印出 24:00:00
print(human_readable_timer(359999))
# 印出 99:59:59

# padStart() 會將用給定用於填充的字串，以重複的方式，插入到目標字串的起頭(左側)，直到目標字串到達指定長度
# Math.floor() 函式會回傳小於等於所給數字的最大整數。
