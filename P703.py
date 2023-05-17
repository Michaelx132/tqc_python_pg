import io

inputStr = input();
try:
    if len(inputStr) > 10:
        raise Exception
    str2 = int(inputStr,2)
    print(str2)
except:        
    print(f"error")

