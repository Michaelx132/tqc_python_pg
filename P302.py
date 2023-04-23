import io
from logging import exception

#迴圈偶數連加

inputInt = []
for i in range(2):
  inputInt.append( int(input()) )

try:
  total = 0
  if (inputInt[1] < inputInt[1]):
    raise exception
  for x in range(inputInt[0], inputInt[1]+1):
    if (x % 2 == 0):
      total = total + x
  print(f"{total}")
except:
  print(f"error")