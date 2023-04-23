import io

#不定數迴圈-最小值

total = None
total = int(input())
while(True):
    inputInt = int(input())
    if (inputInt== 9999):
      break
    if (total == None):
      total = inputInt
    elif (inputInt < total ):
      total = inputInt
print(f"{total}")        