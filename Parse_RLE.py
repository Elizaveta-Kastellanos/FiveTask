import re

def Parse_back_RLE(small_num):
    num = ''
    #for i in small_num:#range(len(small_num)):
    small_num = re.sub(","," ",small_num).split()
    a = int(small_num[0]) 
    for i in range(0,a):
        num = num + small_num[1]
    return num        

def Parse_RLE(big_num):
    count = 1
    num = ''
    for i in range(len(big_num)-1):
        if i <= len(big_num):
            if big_num[i] == big_num[i + 1]:
                count += 1
            else:
                num = num + str(count) + ',' + str(big_num[i]) + '\n'
                count = 1
    num = num + str(count) + ',' + str(big_num[i]) + '\n'
    return num
