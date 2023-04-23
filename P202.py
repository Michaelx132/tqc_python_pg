import io

# 倍數判斷
# 設計說明
# 輸入一個正整數
# 

try:
  inputInt = int(input())
  if ( inputInt % 3 == 0 and inputInt % 5 == 0 ):
    print(f"{inputInt} is a multiple of 3 and 5")
  elif ( inputInt % 3 == 0 ):
    print(f"{inputInt} is a multiple of 3")
  elif ( inputInt % 5 == 0 ):
    print(f"{inputInt} is a multiple of 5")
  else:
    print(f"{inputInt} is not a multiple of 3 or 5")
except:
  print(f"error")