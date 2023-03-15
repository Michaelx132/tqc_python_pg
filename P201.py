import io
from logging import exception
# 選擇敘述與迴圈
# 計算分數
# 設計說明：
# (1) 請撰寫一程式，讓使用者輸入分數，若分數大於 60 分，則加 10 分，否則
# 加 5 分，最後輸出調整後的分數。
# (2) 若使用者輸入的分數在 0~100 以外，則輸出「error」。

string = input()
try:
  score = int(string)
  if (score <0 or score > 100):
    raise exception
  if (score>60):
    print(f"{score+10}")
  else:
    print(f"{score+5}")
except:
    print(f"error")
  
# print(f"{string.upper()}")

