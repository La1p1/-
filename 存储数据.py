# 10.4 存储数据

# 10.4.1 使用dump()、load()
# dump()接受两个实参，一个是存储的数据，一个是用于存储的数据文件对象
# 注：dump()用于写入储存
import json
numbers = [1 , 2, 3 , 4 , 11]

filename = 'numbers.json'
with open(filename , 'w') as file:
    # dump()中存储的numbers是储存的内容，file是存储的文件路径
    json.dump(numbers , file)
            # 存储内容  # 存储文件路径

# load()就同单词意思一样 加载 读取方式
# 使用load()加载json格式文件
import json
filename = 'C:\d_text\_numbers.json'

with open(filename) as file:
   # 加载/读取numbers.json格式的文件并存入一个变量，存入变量只为了方便打印
    numbers = json.load(file)

print(numbers)

# 10.4.2 保存读取用户生成的数据
import json
information = input('Enter your name: ')

filename = 'C:\d_text\information.json'
with open(filename , 'w') as file:
    json.dump(information , file)
    print("Welconme " + information)