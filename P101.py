import io
# 基本認識
# P101 計算總和
#  設計說明：
# (1) 請撰寫一程式，讓使用者輸入要購買的瓶果汁數量，
# 蘋果汁一瓶單價 23.34元，
# 計算總共要花多少錢並輸出至小數點後第二位。


input = input("")
print('{:.2f}'.format((float(input) * float(23.34))))
# print( round((float(input) * float(23.34)),2))
