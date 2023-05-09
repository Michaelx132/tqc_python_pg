import io

# 資料加總

fs = open("P901.txt","r")

loadInts = fs.read().split(" ")
score = 0

for i in loadInts:
    score = score + int(i)

print( f"{score}" )




