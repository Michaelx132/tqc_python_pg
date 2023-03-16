import io
from logging import exception
# 字串與檔案處理
#  設計說明：
# (1) 請撰寫一程式，讓使用者輸入兩個相同長度的字串與一個正整數 n，字串
# 長度皆不超過128個字元，依ASCII碼表上的順序比對兩字串前n個字元，
# 最後輸出兩字串前 n 個字元的比較結果。若使用者輸入正整數 n 超過字串
# 長度，則輸出「error」

inputa = input()
inputb = input()
a = 0
b = 0
n = int(input())

try:
  if (n>len(inputa)):
    raise exception
  for c in inputa[:n]:
    a = a + ord(c)
  for d in inputb[:n]:
    b = b + ord(d)
  if (a > b):
    print(f"{inputa} > {inputb}")
  elif (a == b):
    print(f"{inputa} = {inputb}")
  elif (a < b):
    print(f"{inputa} < {inputb}")
except:
  print(f"error")
