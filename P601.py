import io
# 字串拆解
# 設計說明：
# (1) 請撰寫一程式，讓使用者輸入一個包含英文大小寫的字串，
# 並依序將字串中的大、小寫字母分離，最後依序輸出字串中的大寫字串、
# 小寫字串及大寫字母的數量。
# 技巧
# str.upper() 轉大寫
# str.lower() 轉小寫
# str.isupper() 大寫 回傳 true
# str.islower() 小寫 回傳 true
# ''.join(list) 將list轉string ex:"str","ing" => "string"

inputStr = list(input().strip())
lowerStr = []
upperStr = []
for x in inputStr:
    if (x.isupper()):
        upperStr.append(x)
    if (x.islower()):
        lowerStr.append(x)
print(''.join(upperStr))
print(''.join(lowerStr))
print(len(upperStr))

