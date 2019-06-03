# 第6章 <字典> 书81页

# 6.1 简单的字典 {}代表字典
alien_0 = {'color' : 'green' , 'points' : 5}    # 字典alien_0储存了颜色和点数
print(alien_0['color'])   # 两行print打印了字典里的颜色和点数
print(alien_0['points'])

# 6.2 使用字典 详细理论见书82页
alien_0 = {'color': 'green' , 'points': 5}  # 当中的color和points在字典中称为键
                                            # 'green'和'points'在字典中称为值，它们和键是相对的
# 6.3 访问字典中的值
alien_0 = {'color' : 'green' , 'points' : 5}  # 创建字典，定义color和points的值

new_points = alien_0['points']   # 将alien字典中points的值储存在新建列表new_points中
print("You just earend" + str(new_points) + " points!")   # 打印并访问了字典及新列表中相同的points的值
# 也可以不用定义新值直接使用这行代码  print("You got " + str(alien_0['points'] + "points !"))
# 6.4 添加键-值
alien_0 = {'color': 'green' , 'points': 5}
print(alien_0)       # 创建并打印字典（此时只有2个键-值对）

alien_0['x_position'] = 0    # 使用[]将x_position键-值对添加进alien_0字典中
alien_0['y_position'] = 25   # 相同操作
print(alien_0)               # 打印修改后的字典，最终包含4个键-值对
# 书中说，python不关心添加进字典的顺序，只关心键和值的关系，但是实际操作还是依照加入字典的书序排列

# 6.5 创建一个空字典/向字典中添加键-值对
alien_0 = {}   # 创建一个空的字典，字典不是空的也可以用这种方法添加键-值对，但在特殊情况下必须用空字典
alien_0['color'] = 'green'  # 添加第一个 键-值对
alien_0['points'] = 5       # 添加第二个 键-值对
print(alien_0)   # 打印看输出结果
# 字典名['键'] = '值' , 添加格式  和添加新键-值对进入字典方法一样

# 6.2.4 修改字典中的值
alien_0 = {'color': 'green'}   # 创建一个字典
print("The alien color is " + alien_0['color'] + " now .") # 打印结果显示alien的color是green

alien_0['color'] = 'red'  # 在方括号内输入字典中键的名称，输入新的值且重新定义color的值
print("The alien color is " + alien_0['color'] + " now .") # 打印修改后的输出结果

# 2
alien_0 = {'x_position': 0 , 'y_position': 25 , 'speed': 'medium'}  # 定义alien的x和y坐标和alien的速度 ，速度是变量
print("Original x_position: " + str(alien_0['x_position'])) # 初始的x坐标为0

if alien_0['speed'] == 'slow':   # 如果alien的速度为slow，就在x初始坐标的基础上+1
    x_increment = 1
elif alien_0['speed'] == 'medium': # 如果速度为medium，增量就+2
    x_increment = 2
else: # 如果都不是，增量就+3
    x_increment = 3

alien_0['x_position'] = alien_0['x_position'] + x_increment # 因为初始速度为medium，所以就在基础坐标上+2
print("New x_position: " + str(alien_0['x_position'])) # x新坐标就为2

# 6.2.5 删除键-值对
alien_0 = {'color' : 'green' , 'points' : 5} # 删除键-值对，需要指定删除的键，即可永久删除这个键-值对
print(alien_0)

del alien_0['points'] # del 字典名['键名'] 永久删除，直接输入要删除的键名，值也会一并删掉
print(alien_0) # 同列表删除相似

# 6.2.6 由类型对象组成的字典
fav_languages = { # 运用这种新的格式定义fav_languages的字典中的键-值对
    'jen': 'python',  # 花括号打头，提行4格缩进
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python', # 在最后一个键-值对后面打上逗号，以便之后进行添加键-值对
    } # 提行4格缩进，花括号结尾，实际操作看来，结尾花括号没有缩进也能运行
# 个人感觉这样的格式易阅读
print("Sarah's fav languages is " + fav_languages['sarah'].title() + ".")
# 实操发现 结尾没有逗号，花括号没有缩进，代码都能运行
# 练习
# 6-1
information = {
    'frist_name': 'Wang',
    'last_name': 'Jin',
    'age': 18,
    'city': 'Guanghan',
    }

print(information['first_name'])
print(information['last_name'])
print(information['age'])
print(information['city'])

# 第二种方式
information = {
    'frist_name': 'Wang',
    'last_name': 'Jin',
    'age': 18,
    'city': 'Guanghan',
    }

for key , value in information.items():
    print("\nKey:" + key)
    print("Value:" + str(value))

# 6-2
fav_nummber = {
    'weijiang': 1,
    'wangjin': 2,
    'chenchangfu': 3,
    'chenhaoran': 4,
    'xiaotianhao': 5,
    }

print("Weijiang fav nummber is " + str(fav_nummber['weijiang']) + " .")

# 6.3 遍历字典
user_0 = {
    'usename': 'efermi',
    'first': 'enrico',
    'last': 'fremi',
    }
# items() 是返回一个键-值对列表，用for循环遍历每一个字典中的键-值对
for key, value in user_0.items():  # for k, v in user_0.items()    使用for和.items()遍历字典user_0，创其变量为key和value，这里的key和value是两个变量
    print("\nKey:" + str(key)) # 将字典中的键储存在变量key中
    print("Value:" + str(value)) # 值储存在变量value中 并打印 key 和 value

# 之前的一个例子
fav_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

for name , languages in fav_languages.items():  # 这里的name和langua是两个变量，它们和字典中的键值相对应
    print(name.title() + "fav languages is " + languages.title() + ".")

# 6.3.2 遍历字典中的键
fav_languages = {
    'jen' : 'python',   
    'sarah' : 'c',
    'edward' : 'ruby',
    'phil' : 'python',
    }
# 
for name in fav_languages.keys(): # 将字典中的键-值对存入变量名name中，.items()是遍历字典中的键-值对，用.keys()只遍历字典中的键
    print(name.title())
# 遍历时会自动遍历字典中的键，所以不用.keys()输出结果和有.keys()一样的,如果只遍历字典中的值，只需要把.keys()改成.values()即可

# 2 
fav_languages = {
    'jen' : 'python',
    'sarah' : 'c',
    'edward': 'ruby',
    'phil': 'python',
    }


for name in fav_languages.keys():  # 遍历字典，将字典的键储存为name
    print(name.title())  # 打印字典的键(打印朋友的名字)
    
friends = ['phil', 'sarah']
if name in friends:  # 如果name中有friends列表中的元素，就运行下面的print代码
    print(" Hi " + name.title() + ", I see your fav language is " + fav_languages[name].title() + ".")

# 6.3.3 按顺序遍历字典中的key
fav_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

for name in sorted(fav_languages.keys()): # 老样子在使用.keys()遍历列表的同事使用当时学习列表中的一个函数sorted()，将字典中的key按字母顺序临时排序
    print(name.title() + " , thank you for taking the poll.")

# 6.3.4 遍历字典中的所有值
fav_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

print("The following languages have been mentioned:")
for language in fav_languages.values():
    print(language.title())

# 用set(集合) 剔除字典中的重复项
fav_languages = {
    'jen': 'python',
    'sarah': 'c',
    'eaward': 'ruby',
    'phil': 'python'
    }

print("The following languages have been mentioned: ")
for language in set(fav_languages.values()):
    print(language.title())
# 字典中本来有几项重复value，用set，可以剔除字典中的重复的value

# 练习

# 6-4
user_0 = {
    'usename': 'laipi',
    'first': 'Wei',
    'last': 'Lai',
    'age': '17',
    'city': 'Zizhong'
    }

for key,value in user_0.items():
    print(key,value)

# 6-5
rivers = {
    'chongqing': 'jialinjiang',
    'xijiang': 'yaluzangpu',
    'china': 'changjiang',
    }

for place , river in rivers.items():
    print("The " + str(place.title()) + " runs throngh " + str(river.title() + " ."))

rivers = {
    'chongqing': 'jialinjinag',
    'xizang': 'yaluzangpu',
    'china': 'changjiang',
    }

for river in rivers.values():
    print("\nHere is river's name: " + str(river.title()))

rivers = {
    'chongqing': 'jialinjiang',
    'xizang': 'yaluzangpu',
    'china': 'changjiang',
    }

for place in rivers.keys():
    print("\nHere is place'name " + str(place.title()))

# 6-6
fav_languages = {
    'jen' : 'python',
    'sarah' : 'c',
    'edward' : 'ruby',
    'phil' : 'python',
    }

willing = ['jen' , 'sarah' , 'edward' , 'phil' , 'lisa' , 'eric']
for name in willing:
    if name in fav_languages.keys():
        print("Thank you , " + name.title())
    else:
        print("Welcome to join us , " + name[:])