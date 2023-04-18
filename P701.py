import io
# 、二進位轉十進位
# 設計說明：
# (1) 請撰寫一個程式，讓使用者輸入一個 10 字元以內的二進位字串，
# 將其轉換成十進位並輸出
# 技巧
# 次方 n ** 2  = n 的2次方

inputStr = list(input().strip())
score = 0
try:
    if (len(inputStr) > 10):
        raise Exception
    n=0
    for x in range(len(inputStr)-1,-1,-1):
        if (x==0):
            if (inputStr[n] == '1'):
                score = score + 2 ** x
        else:
            if (inputStr[n] == '1'):
                score = score + 2 ** x
        n = n+1
    print(score)
except:
    print("error")
