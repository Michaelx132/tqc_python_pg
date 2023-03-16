import io
# 、函式與陣列
# 設計說明：
# (1) 請撰寫一程式，包含名為 compute()的函式，接收主程式傳遞的一個期中
# 考分數，compute()判斷分數值，若分數在 0~100 以外，則回傳「-1」；若
# 分數大於等於 60，則加 5 分；否則一律加 10 分，回傳至主程式輸出。

def compute(par):
  if (par <0 or par > 100):
    return -1
  else:
    if (par >= 60):
      return par+5
    else:
      return par+10

input = int(input())
print(f"{compute(input)}")