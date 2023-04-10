import io

# '{n:[d/f/s]}
# n 對應 .format(0,1,2,3...)
# d 整數
# f 浮點數
# s 字串
# 'format'.format(variable)
# 

print("write 1: format(number,format)")
print(format(int(123.456),'>5d'))
print("write 2: 'format'.format(number)")
print('{:>5d}'.format(int(123.456)))

a = int(123.456)
b = int(789.456)
print("1234567890")
print('{1:5d}'.format(a,b))
print('|{1:>5d}|\n|{0:<5d}|'.format(a,b))