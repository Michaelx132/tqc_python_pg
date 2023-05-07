import io
# 數組合併排序

list1 = []
list2 = []
combin_list1 = []
print("Create tuple1:")
while(True):
  inputInt1 = int(input())
  if inputInt1 == -9999:
    break
  list1.append(int(inputInt1))
print("Create tuple2:")
while(True):
  inputInt2 = int(input())
  if inputInt2 == -9999:
    break
  list2.append(int(inputInt2))

combin_list1 = list1 + list2
print(f"Combined tuple before sorting:{combin_list1}")
print(f"Combined list after sorting:{sorted(combin_list1)}")
  
