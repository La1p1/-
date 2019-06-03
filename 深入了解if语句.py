# 深入了解if语句 书70页

# 5.3.2 if-else语句
age = 17
if age >=18:                # 条件
    print("you are old enough to vote.")
    print("have you registerd to vote yet?")        # 通过执行
else:
    print("sorry , you are too young ti vote.")     # 未满足条件的就会执行else下面的代码
    print("please register to vote as soon you turn 18!")   # 不通过条件执行
# 在if-else两个中，总会执行其中一个代码

# 5.3.3 if-elif-else 结构
age = 12

if age < 4:
    print("your admission cost is $0.")
elif age < 18:
    print("your admission cost is $5.")   
else:
    print("your admission cost is $10.")
# 可以把第一行的if看做单独，后面的elif-else看做一体

# 简版 将每一个通过条件后的提示语简写成一句age = 12
age = 12             # 条件
if age < 4:          # 年龄大于4且不超过12
    price = 0
elif age < 18:       # 年龄大于12且不超过18
    price = 5
else:                # 年龄大于18
    price = 10

print("your admission cost is $" + str(price) + ".")   # 输出结果
# str可以理解为插入price的值

# 5.3.4 使用多个dlif代码块 (可根据需要使用任意数量的elif代码块)
age = 12

if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age = 65:    # 在上一个例子的基础上多加了一个elif代码块
    price = 10
else:
    price = 5
print("your admission cost is" + str(price) + ".")

# 5.3.5 省略else代码块
# 在if-elif-else中不要求必须有else代码块
age = 12

if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
    price = 10
elif age >= 65:   # 以上一个例子为例，可以直接省略else代码块，依旧使用elif代码块编写
    price = 5

print("your admission cost is " + str(price) + ".")
# else是不满足if-elif才会通过的码块

# 5.3.6测试多个条件
r_t = ['mushrooms' , 'extra cheese']

if 'mushrooms' in r_t: 
    print("adding mushrooms.")

if 'peppernoi' in r_t:  # False
    print("adding peppernoi")

if 'extra cheese' in r_t:
    print("adding extra cheese.")

print("\nFinished makeing your pizza!")
# 在if-elif-else中，如果只使用if代码块，则当中不管有没有不通过的条件都会执行下一行代码命令
# 看做3个独立的代码块，不会受到不通过代码的影响
# 若要运行一个代码块就用if-elif-else，若要运行多个代码块就用if

# 练习

# 5-3
alien_color1 = 'green'
alien_color2 = 'yellow'
alien_color3 = 'red'
if alien_color1 == 'green':
    print("You got 5 point" + "!")

if alien_color == 'yellow' or 'red':

    print("You are so suck" + "!")

# 5-4
alien_color = 'green'
if alien_color == 'green':
    print("You got 5 point" + "!")

if alien_color != 'red':
    print("You got 10 point" + "!")
# else版本
alien_color = 'green'
if alien_color != 'green':
    print("You got 10 point" + "!")
else:
    print("You got 5 point" + "!")

# 5-5
alien_colors = ['green' , 'yellow' , 'red']

if alien_color == 'green':
    point = 5
elif alien_color == 'yellow':
    point = 10
else:
    point = 15

print("You got " + str(point) + "!")
# 二版
alien_color = ['green' , 'yellow' , 'red']

if alien_color == 'green':
    print("You got 5 point" + "!")
elif alien_color == 'yellow':
    print("You got 10 point" + "!")
else:
    print("You got 15 point" + "!")

#5-6
age = 2

if age >= 0:
    stage = 'baby'
elif age <= 4:
    stage = 'learn walk'
elif age <= 13:
    stage = 'child'
elif age <= 20:
    stage = 'teenager'
elif age <= 65:
    stage = 'grow up'
else:
    stage = 'old man'

print("You are in " + str(stage) + " " + "stage" + "!")

# 5-7
fav_fruits = ['apple' , 'banana' , 'pear']
if 'apple' in fav_fruits:
    print("I like apple so much")

if 'banana' in fav_fruits:
    print("I like banana")

if 'pear' in fav_fruits:
    print("I like pear")

if 'watermelon' not in fav_fruits:
    print("I hit watermelon")

if 'lemon' and 'orange' in fav_fruits:
    print("That is False")

# 5.4.1检查特殊元素
r_ts = ['mushrooms' , 'green peppers' , 'extra cheese']
for r_t in r_ts:
    if r_t == 'green peppers':
        print("Sorry , we are out of green peppers right now!")
    else:
        print("Adding " + r_t + ".")

print("\nFinnshed making your piazz!")
# 在if语句中使用for循环遍历列表，就不用使用多个if-elif-else，效率更高

# 5.4.2确认列表不是空的
r_ts = []

if r_ts:
    for r_t in r_ts:
        print("Adding " + r_t + ".")         # 如果列表中遍历到元素，则和上一个例子相同
    print("\nFinished making your pizza!")   # 在if中使用for，但for在列表中没有遍历到任何元素，因为列表是空的，所以返回False，转为执行else代码块
else:
    print("Are you sure you want a plain pizza?")

# 5.4.3使用多个列表
a_ts = ['mushroomes' , 'olives' , 'green peppers' , 'peppernoi' , 'pineapple' , 'extra cheese']

r_ts = ['mushrooms' , 'french fries' , 'extra cheese']

for r_t in r_ts:
    if r_t in a_ts:   # 如果for循环遍历到a_ts中有r_ts中相应的元素，才会执行if码块中的print
        print("Adding " + r_t + ")
    else:             # 如果for循环没有遍历到相应/相同的元素，才会执行else码块中的print
        print("Sorry , we don't have " + r_t + ".")

print("\nFinished making your pizza!")

# 练习

# 5-8
names = ['admin' , 'william' , 'lily' , 'king' , 'john']
for name in names:
    if name == 'admin':
        print("Hello admin , would you like to see a staus report?")
else:
    print("Hello william , thank you for logging again!")

# 5-9
names = []
if names:
    for name in names:       # for循环遍历列表name，如果列表为空，结果返回False
        print("We need to find some users!")

print("Our list is blank")

# 5-10
current_users = ('lily' , 'kim' , 'king' , 'john' , 'chris')
new_users = ('lily' , 'william' , 'king' , 'anna' , 'jake')

for new_user in new_users:
    if new_user in current_users:          # 被遍历的列表要放在前面
        print("需要输入的用户名：")
else:
    print("这个名字未被使用")

# 5-11    书80页 练习
 
# 暂留


