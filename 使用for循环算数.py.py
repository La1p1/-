# 数字列表 4.3 书51页

for value in range(1,5):    #### -1定律 ####
    print(value)    #### 函数range让python指定从1开始数，到第5停止，所以不包括5. ####


# 使用range创建数字列表及 4.3.2

numbers = list(range(1,6))   #### list 目录/列表 ####
print(numbers)      #### list 将range的输出结果转换为列表形式显示，科学制表 ####

even_numbers = list(range(2,11,2))
print(even_numbers) #### even是偶数的意思，第一个2表示从2开始数，然后不断加2，直到11终止 ####

squares = []
for value in range(1,11):
    square = value**2           #### for square in squares ####
    squares.append(square)      #### 这里已经把squares存储变量为square ####

print(squares)

#### 为了使代码看起来简洁，可以不使用square变量，不容易出错 ####
squares = []        #### squares 平方 ####
for value in range(1,11):
    squares.append(value**2)    #### 两个 ** 代表乘方 ####

print(squares)

# 补充: min = 小的
#      max = 大的
#      sum = 总和/求和

# 4.3.4 列表解析

# 列表解析 #                                                                                                                                                                                                                          
squares = [value**2 for value in range(1,11)]  #### 解释：让value的平方值的范围在1-11之间 ####
print(squares)

# 练习
# print("1-10000001的总和") #
numbers = list(range(1,10000001))
max(numbers)
min(numbers)
sum(numbers)

numbers = list(range(1,10000001))
for nummber in numbers:
    print(nummber)

# 4-6
print("算出1-20之内的奇数")
uneven_numbers = list(range(1,21,2))    # 1+2=3 #
print(uneven_numbers)
for numbers in uneven_numbers:
    print(numbers)

# 4-7 
print("算出3-30之内能被3整出的数")
multiple = list(range(3,31,3))          # multiple = 倍数 #
print(multiple)
for numbers in multiple:
    print(numbers)

# 4-8
print("算出1-10之内的立方")
squares = []
for value in range(1,11):               # 注意符号 #
    squares.append(value**3)
    print(squares)

# 4-9
print("使用列表显示1-10的整数立方")
squares = [value**3 for value in range(1,11)]
print(squares)