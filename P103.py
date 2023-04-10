import io

# Python中有兩種字串格式化的寫法，
# 分別是「%」跟「format」，
# 如果是Python3的就比較推薦用「format」


print('{:0.2f}'.format(653.123456)) #加上「.2火」小數第2位
print('{:>10.2f}'.format(853.123456)) #加上「>」靠右對齊
print('{:^10.2f}'.format(853.123456)) #加上「^」置中對齊
print('{:<10.2f}'.format(853.123456)) #加上「<」靠左對齊
print('{:0,.2f}'.format(12345.123456)) #加上「,」


