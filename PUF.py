import hashlib
import random

array = []
mux1 = []
mux2 = []
ropuf = []
change = []
sum = []
sum1 = []
sum3 = []
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
print("二進位: ", str(binaryString))
# print(list(binaryString))
print()
array = [random.randint(10, 99) for x in range(1024)]
print(len(array))  # 1024個
mux1 = array[0:256]
mux2 = array[0:256]
ropuf = array[0:256]
print("--------------------第一組--------------------")
array1 = array[0:256]
print(len(array1))
print()
print("--------------------第二組--------------------")
array2 = array[256:512]
print(len(array2))
print()
print("--------------------第三組--------------------")
array3 = array[512:768]
print(len(array3))
print()
print("--------------------第四組--------------------")
array4 = array[768:1024]
print(len(array4))
print()
i = 0
print(len(str(binaryString)))
for n in range(0, 256):
    
    if binaryString[n] == '1':  # 比大
        if array1[n] >= array2[n]:
            mux1[n] = array1[n]

        elif array1[n] < array2[n]:
            mux1[n] = array2[n]

        if array3[n] >= array4[n]:
            mux2[n] = array3[n]

        elif array3[n] <= array4[n]:
            mux2[n] = array4[n]

    else:  # 比小
        if array1[n] <= array2[n]:
            mux1[n] = array1[i]

        elif array1[n] > array2[n]:
            mux1[n] = array2[n]

        if array3[n] <= array4[n]:
            mux2[n] = array3[n]

        elif array3[n] >= array4[n]:
            mux2[n] = array4[n]

print("RO PUF:")

for i in range(0, 256):
    if mux1[i] > mux2[i]:
        ropuf[i] = 1

    else:
        ropuf[i] = 0

print(ropuf)
print()

print("交換位移量:")
change = ropuf[0:8]
print(change)
sum = change[0]*1+change[1]*2+change[2]*4 + change[3] * \
    6+ropuf[4]*8+change[5]*10+change[6]*12+change[7]*14
print(sum)

last=array[0:256]
i=0
for n in range(0, 256):
    try:
        last[n+sum]=ropuf[n]
    except:
        last[i]=ropuf[n]
        i=i+1

print(ropuf[0:50])
print(last[0:50])