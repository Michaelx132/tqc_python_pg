import io
# 植物大戰殭屍™: 和睦小鎮保衛戰
# (1) 設計一個可以輸入小數 1 到 4 位數
# 將這四個浮點數以欄寬為7，先列印向右對齊
# 再印向左對齊，中間以|區隔

inputList = []
for i in range(4):
  inputList.append('{:.2f}'.format(float(input())))


print(inputList)
print(f"|{ '{:>7s}'.format(inputList[0]) }{ '{:>7s}'.format(inputList[1]) }|")
print(f"|{ '{:>7s}'.format(inputList[2]) }{ '{:>7s}'.format(inputList[3]) }|")
print(f"|{ '{:<7s}'.format(inputList[0]) }{ '{:<7s}'.format(inputList[1]) }|")
print(f"|{ '{:<7s}'.format(inputList[2]) }{ '{:<7s}'.format(inputList[3]) }|")
