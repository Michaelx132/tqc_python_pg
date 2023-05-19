import io

# 十進位轉其他進位

inputStr = input()

print("二進位：")
print( "{0:b}".format(int(inputStr))  )
print("十六進位：")
print( "{0:x}".format(int(inputStr))  )

# print( f"{ ord(inputStr) }")