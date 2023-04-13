import io
# 數字相乘
# 設計說明：
# (1) 請撰寫一程式，讓使用者輸入一個 1~9 位數的數字，
# 輸出每一個數字相乘的算式及結果。
# 技巧
# split() 會將字串 str ing 變成 "str","ing"
# strip() 會將字串 string 變成 "s","t","r","i","n","g"

inputStr  = input()
try:
    score = 1
    int(inputStr)
    listStr = list(inputStr.strip())
    for x in listStr:
        score = score * int(x)
    print("{:0.2f}".format(score))
except ValueError:
    print("error")
    

