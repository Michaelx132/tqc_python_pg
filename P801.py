import io

# 字元對應



total = 0
inputStr = input()


for i in inputStr:
    total = total + ord(i)
    print(f"ASCII Code for {i} is {ord(i)}")

print(f"{total}")