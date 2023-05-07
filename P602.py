import io

# 撲克牌總和
# 1. 寫一個程式輸入五張牌
# 2. 計算五張牌的總和 A=1, J=11, Q=12, K=13
# 範例:
# 3
# 2
# 4
# 6
# A
# ouput: 16

nums = ['','A','2','3','4','5','6','7','8','9','10','J','Q','K']
total = 0
for i in range(5):
  inputStr = input().upper()
  print(inputStr)
  if ( inputStr  in nums):
    total = total + nums.index(inputStr)
print(f"{total}")
  
