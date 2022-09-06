import hashlib
import random

array = []
mux1 = [1000]
mux2 = [1000]
password = input('使用者輸入密碼:')
print('使用者密碼:', password)
hash_password = hashlib.sha256(password.encode(
    "utf-8")).hexdigest()  # 用sha256對password進行加密
print("十六進位:", hash_password)
number = int(hash_password, 16)
print("十進位:", number)  # 十六轉十
decimalValue = number
binaryString = ""
while decimalValue != 0:
    binaryString = str(decimalValue % 2) + binaryString
    decimalValue //= 2
print("二進位: ", binaryString)
# print(list(binaryString))
print()
array = [random.randint(10, 99) for x in range(1024)]
print(len(array))  # 1024個
print("--------------------第一組--------------------")
print(array[0:256])
print()
print("--------------------第二組--------------------")
print(array[256:512])
print()
print("--------------------第三組--------------------")
print(array[512:768])
print()
print("--------------------第四組--------------------")
print(array[768:1024])
print()
i = 0
for n in binaryString:
    if n == '1':  # 比大
        if array[i] > array[256+i]:
            print(array[i])
            #mux1[1] = array[i]

        elif array[i] < array[256+i]:
            print(array[256+i])
            #mux1[i] = array[256+i]

        elif array[512+i] > array[768+i]:
            print(array[512+i])
           # mux2[i] = array[512+i]

        else:
            print(array[768+i])
            #mux2[i] = array[768+i]

    else:  # 比小
        if array[i] < array[256+i]:
            print(array[i])
            #mux1[i] = array[i]

        elif array[i] > array[256+i]:
            print(array[256+i])
            #mux1[i] = array[256+i]

        elif array[512+i] > array[768+i]:
            print(array[768+i])
            #mux2[i] = array[768+i]

        else:
            print(array[512+i])
           # mux2[i] = array[512+i]

    i += 1
