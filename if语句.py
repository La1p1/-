# if语句 书64页

# 5.1 实例
cars = ['audi','bmw','subaru','toyota']

for car in cars:
    if car == 'bmw':  
        print(car.upper()) # 只有检查到有相同，才会运行接下来的代码
    else:
        print(car.title())

# 5.2.1 检查是否相等
car = 'bmw' # 定义值
car == 'bmw' # 用==检查值是否为bmw
# 相等为True，不想到为False

# 5.2.2 检查是否考虑大小写(要考虑)
car = 'bmw'
car == 'Bmw'
# False

car = 'bmw'
car.lower() == 'Bmw' # 将Bmw转换为小写进行检查
# True 
word = 'up'
word.title() == 'Up'
# True
# 5.2.3 检查是否不相等
requested_topping = 'mushrooms'  # ! 代表不，!= 则代表不相等

if requested_topping != 'anchovies':  # 检查这两值是否不相等
    print("hold the anchovies!")      # 不相等则为False，才会运行这行print代码

answer = 17         # 定义值为17

if answer != 42:    # 如果answer不等于42才会运行下面这条print语句
    print("That is not correct answer , try agian!")

# 5.2.4 比较数值
age = 19  # 定义age的值为19
age < 21  # 19 < 21
# True

age = 19
age <= 21 # 19 <= 21
# True

age = 19
age >= 21 # 19 >= 21
# False

# 5.2.5 使用and和or检查多个条件
# 使用and检查多个条件
age_0 = 22
age_1 = 18
(age_0 >= 21) and (age_1 >= 21)  
# False

age_1 = 23                        # 在and可以同时检查多个条件
(age_0 >= 22) and (age_1 >= 22)   # 在and必须是多个条件都达成结果才会True
# True

# 使用or检查多个条件
age_0 = 22
age_1 = 18                        # 在or中只要有一个达成条件结果就会True
age_0 >= 21 or age_1 >= 21        # age0达成条件，age1不达成条件
# True

age_0 = 18 
age_0 >= 21 or age_1 >= 21        # 在or中只有两个或者多个都不达成条件结果才会False，其中有一个达成条件都会返回True

# False

# 5.2.6 检查特定值是否在列表中
requested_toppings = ['mushrooms','noions','pineapple']
'mushrooms' in requested_toppings  # 使用in查找mushroom是否在列表中，若在列表中结果则为True
# True

'pepperoni' in requested_toppings  # 使用in pepperoni不在列表中，所以结果为False
# False

# 5.2.6 检查特定值是否不在列表中
banned_users = ['andrew','carolina','david']
user = 'marie' 

if user not in banned_users:       # 使用not in 查找用户marie是否在列表中，若不在则运行下面的print语句
    print(user.title() + " , you can post a response if you wish.")

# 练习

# 5-1
names = 'Anna'
names == 'King'
if names == 'Anna':
    print("True")

if names != 'King':
    print("False")

# 5-2
name1 = 'Anna'
name2 = 'William'
name3 = 'Kim'
name4 = 'King'

if name1.lower() == 'anna':
    print("将name1里的大写Anna转为小写再进行的检查")

if name1 == 'anna' and name2 == 'william':
    print("that's True")

if name1 == 'chris' or name2 != 'chris':
    print("that's True")

if name1 != name2:
    print("that's True")

names = ['Anna' , 'William' , 'Kim' , 'King']
if 'Anna' in names:
    print("that's True")

if 'Lily' not in names:
    print("that's False")

nummber = 4
nummber0 = 0
nummber1 = 1
nummber2 = 2
nummber3 = 3
nummber4 = 4

if nummber1 <= nummber2:
    print("that's False")

if nummber0 >= nummber1:
    print("that's False , try agian")  # False，不成立

if nummber == nummber4:
    print("that's True")

if nummber3 <= nummber2 and nummber1 <= nummber0:
    print("that's False")

if nummber3 <= nummber2 or nummber1 <= nummber0:
    print("使用or时两个条件都不成立就会返回False")    

if nummber4 >= nummber2 or nummber3 <= nummber2:
    print("or里只要有一项条件达成就会返回True")

if nummber4 != nummber3:
    print(" ! 也可以用来比大小")
