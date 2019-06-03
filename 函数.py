# 第8章 函数 书114页

# 8.1 定义函数
def greet_user(): # 定义函数格式： def 函数名(形参)：
    """显示简单的问候语"""   #     """文档字符串，描述函数的用处"""
    print("Hello !")        #     def中的执行代码

greet_user()                #     调用函数名中的执行程序

# 8.1.1 向函数传递信息
def greet_user(username): # 给函数定义了一个形参
    """显示一段简单的问候语"""
    print("Hello , " + username.title()) # def码块中的执行代码，会在调用函数的时候，向形参传递实参

greet_user('A') # 调用函数，给函数中的形参传递了一个实参，与执行代码中的形参相匹配

# 8.1.2 实参和形参   
# 形参是在函数后的括号中   
# 实参是在调用是向形参传递的值

# 练习

# 8-1
def display_message():
    """本章初步学习内容"""
    print("本章为复习，因为U盘内容丢失，之前学习的函数内容也一并丢失，本章为复习")

display_message()

# 8-2
def fav_book(book_name):
    """打印一本我最喜爱的书名"""
    print("My fav book is " + book_name)

fav_book('活着')

# 8.2.1 位置实参
def describe_pet(animal_type , pet_name): # 在函数中定义了两个形参
    """显示动物的信息"""
    print("\nI have a " + animal_type + ".") # 两段def码块的执行代码中都引用了函数中的形参
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet('A' , 'B') # 调用函数，向形参传递了两个实参，其位置是一前一后

# 多次调用
def describe_pet(animal_type , pet_name): # 和上一个例子一样，定义两个形参
    """显示动物的信息"""
    print("\nI hava a " + animal_type.title() + ".") # 两段执行代码
    print("My " + animal_type + "'s name is " + pet_name.title())

describe_pet('A' , 'B') # 第一次调用，函数
describe_pet('C' , 'D') # 第二次调用/多次调用，可以多次调用函数及向函数多次传递实参

# 位置传递实参
def describe_pet(animal_type , pet_name): # 定义两个形参，在调用是使用了一前一后的位置传递
    """显示宠物的信息"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name + ".")

describe_pet('A' , 'B') # A和第一个形参对应，B和第二个形参对应，在调用时通过位置传递的方式传递给了形参

# 8.2.2 关键字实参
def describe_pet(animal_type , pet_name): # 关键字传递不存在位置变化，但是指定出准确的形参名
    """显示宠物信息"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name)

describe_pet(animal_type = 'A' , pet_name = 'B') # 在调用阶段，输入了形参名 = 要传递的实参，类似于字典里的key-value

# 8.2.3 默认值  如果一个形参在码块中出现多次，我们可以给这个形参定一个默认值 在调用时不向这个形参传递，这个形参也会有值/实参
def describe_pet(pet_name , animal_type = 'dog'): # 在定义形参的阶段，我们就给其中一个形参一个值，这个叫默认值
    """显示宠物信息""" # 在形参的列表中，必须先列出没有默认值的形参，把有默认值的形参放在最后
    print("\nI have a " + animal_type)
    print("My " + animal_type + "'s name is " + pet_name)

describe_pet(pet_name = 'A')

# 8.2.5 避免缩进错误
# 在写代码的时候，一般情况情况下，码块下都要有四个空格
# 在函数调用的阶段，记得给形参传递实参，有多少个形参就要传递多少个实参

# 练习
# 8-3
def make_T(size , word):
    """显示T上的字样和大小"""
    print("This T's size is " + size + ".")
    print("This T's word is " + word + ".")

make_T(size = 'XXL' , word = 'WL')

# 8-4
def make_Ts(size , word = 'I love Python'):
    """显示Ts的信息"""
    print("This Ts's size is " + size + ".")
    print("This Ts's word is " + word + ".")

make_Ts(size = "xxx")
make_Ts(size = 'xxx' , word = 'Am I love Python?')
make_Ts(size = 'xx' , word = 'Yes, I love Python')

# 8-5
def d_c(city , country = 'China'):
    """显示三个城市的所属国家"""
    print(city + " is in " + country)

d_c(city = 'Chongqing')
d_c(city = 'Sichuan')
d_c(city = 'New York' , country = 'USA')

# 8.3 返回值
def get_f_name(first_name , last_name):
    """显示整洁的姓名"""
    full_name = first_name  + " " + last_name # 创建了full_name变量负责储存两个形参的值，用于储存返回的值
    return full_name # 把定义的变量返回给调用函数
# 我们可以把full_name看作一个值，这个值中也保存着一些值，return时，我们把full_name返回给调用
musician = get_f_name('Wei' , 'Lai') # 调用函数，给形参传递了实参
print(musician) # 打印

# 8.3.2 让实参可选
def get_f_name(fist_name , mid_name , last_name):
    """返回整洁的姓名"""
    full_name = fist_name + " " + mid_name + " " + last_name
    return full_name

musician = get_f_name('A' , 'B' , 'C')
print(musician) # 定义函数要扩展时，在返回值时增加相应的形参和实参

# 返回字典
def get_f_name(fist_name , last_name , mid_name = ' '):
    """返回整洁的姓名"""
    if mid_name: # Python将非空的字符串检测为True，所以if测试也为True
        full_name = fist_name + ' ' + mid_name + ' ' + last_name # 如果在调用阶段向形参传递了三个实参就会运行if语句
    else:                                                        # 反之如果没有传递三个实参，就会运行else语句
        full_name = fist_name + ' ' + last_name 
    return full_name # 我们将值返回给调用

musician = get_f_name('A' , 'B' , 'C')
print(musician)

musician = get_f_name('A' , 'B')
print(musician)

# 8.3.3 返回字典
def build_person(first_name , last_name):
    """返回一个字典，其中包括一个人的信息""" # 将一个字典封装进了值person中，进行返回
    person = {'first': first_name , 'last': last_name} # 定义了一个字典，其中包括两个key-value
    return person # 在函数中可以返回任何类型的值，字典、列表等一些列比较复杂的数据类型
# 字典中value和函数的形参对应，其形参又和实参对应
musician = build_person('A' ,'B') # 如果我们要返回更多的数据，我们就要在字典中加入更多的key-value，同时形参和实参数量也要随之增加
print(musician)
 # 切记带有默认值的形参要放在形参表的最后一个

# 8.3.4 结合使用函数和while循环 可以在函数中放任何类型的数据结构
def get_f_name(first_name , last_name):
    """返回整洁的姓名"""
    full_name = first_name + ' ' + last_name
    return full_name # 和上个实例一样

while True: # while True 测试通过
    print("\n输入你的名字: ")
    print("输入'q'可以退出询问")

    f_name = input("First name: ") # 询问用户的名字
    if f_name == 'q': # 如果用户输入q则退出while循环
        break

    l_name = input("Last name: ")
    if l_name == 'q': 
        break

    formatted = get_f_name(f_name , l_name) # 注意：在调用时，传递的形参是在用户input的实参
    print("\nHello , " + formatted)

# 练习

# 8-6
def city_country(city , country = 'China'):
    """显示三个国家和城市"""
    a = "City: " + city + " , " + country + "."
    return a

b = city_country('Sichaun')
print(b)
b = city_country('Chongqing')
print(b)
b = city_country('Beijing')
print(b)

# 8-7
def make_album(歌手 , 歌名 , 专辑):
    """显示一个位歌手的歌曲和专辑"""
    information = {'歌手': 歌手 , '歌名': 歌名 , '专辑名': 专辑}
    return information

all = make_album('王菲' , '暗涌' , '玩具')
print(all)

# 8.4.1
def print_models(unprinted_designs , completed_models): # def码块中的执行程序在没有调用的情况下是没有值的
    """模拟答应每个设计，直到没有未打印的设计为止
    打印后将每个设计都转移到competed_madels中
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        # 将u_d中的列表pop到c_d变量中
        print("Printing model: " + current_design)
        completed_models.append(current_design) # 将变量中的列表append到形参2中

def show_models(completed_models): # 创建一个新的函数
    """显示打印好的设计模具"""
    print("打印好的设计模具: ")
    for completed_model in completed_models: # 变量形参2中列表
        print(completed_model) # 打印

unprinted_designs = ['a' , 'b' , 'c'] # 创建列表，这些列表用于传递给形参的值
completed_models = []

print_models(unprinted_designs , completed_models) # 给形参赋值
show_models(completed_models)

# 从书上的126页到书上的128页的内容我傻逼到没有保存
# 直接从书上129页开始记录

# 8.4.2 禁止函数修改列表
# 使用切片的表达方式[:]禁止一切对列表的修改

# 练习 书129

# 8-9
def show_mag(names):
    """显示魔术师的名字"""
    for name in names:
        namess = name
        print(namess)

nam = ['A' , 'b' , 'c']
show_mag(nam)

# 8-10
def make_great(lieb1 , lieb2):
    while lieb1:
        lieb3 = lieb1.pop()            # while码块下的代码很重要
        lieb4 = 'the Great：' + lieb3
        lieb2.append(lieb4)

def show_mag(lieb4):
    for name in lieb4:
        print(name)

lieb1 = ['q' , 'w' , 'e']
lieb2 = []

make_great(lieb1 , lieb2)
show_mag(lieb2)

# 8.5 传递任意数量的实参
def make_pizza(*topping): # 在形参前加*号，在调用时不管有多少个实参都会传递给带*的形参
    """打印所有实参"""
    print(topping)

make_pizza('a' , 'b' 'c')
make_pizza(1, 2 , 3) # 调用阶段会把调用时传递给实参都封装到带*的形参中（元组）

# 8.5改版
def make_pizza(*topping): # 不管收到多少实参都会传递给带*的形参
    """打印所有实参并加了几句话"""
    for a in topping:
        print("这是所有的实参名： " + str(a))

make_pizza(1 ,2 ,3, 4) # 调用阶段传递的实参都会传递给带*的形参

# 8.5.1 接合使用位置实参和任意数量实参
def make_pizza(size , *toppings): # 在定义形参时，要把带有*的形参放在形参表的最后一个
        """显示披萨的配料"""
        print("\n这是一个大小 " + str(size) + " 的披萨，配料有 : ") # 在传递时，如果有数字几个str
        for topping in toppings:
                print(topping)

make_pizza(16 , 'a') #### python在传递时，首先匹配位置传递，再进行的关键词匹配，最后把剩余的都传递给带*的形参里 ####
make_pizza(17 , 'b' , 'c' , 'd')
# 注意：带*的形参是元组的储存方式

# 8.5.2 使用任意数量的关键字实参
def build_profile(first , last , **user_info): # 带两个*是接受一个字典的传递 
        """创建一个字典，其中包括用户信息"""
        profile = {} 
        profile['first_name'] = first # 向空的字典里加入了两个k-v
        profile['last_name'] = last
        for key , value in user_info.items(): # 遍历最后一个形参中的k-v
                profile[key] = value # 因为在变量user_info的循环码块中，所以是将profile中的k-v放入了user_info中
        return profile # 把profile这个表达式返回给调用阶段

user_profile = build_profile('Wei' , 'Lai', location = 'Deyang' , age = 17) # 向形参传递
print(user_profile)

# 练习

# 8-12
def pizza(*toppings):
        """显示pizza的实参"""
        print("\n实参： ")
        for topping in toppings:
                print(topping)

pizza('a')
pizza('b')
pizza('c')

# 8-13
def build_profile(first , last , **user_info):
        """创建一个字典，其中包括用户信息"""
        profile = {}
        profile['first_name'] = first
        profile['last_name'] = last
        for key , value in user_info.items():
                profile[key] = value
        return profile

user_profile = build_profile('Wei' , 'Lai', location = 'Deyang' , age = 17 , weight = '62kg' , hight = '172cm')
print(user_profile)

# 8-14
def car_information(color , year , **information):
        """显示汽车的颜色、生产年份、和制造商和型号"""
        color_year = {}
        color_year['color'] = color
        color_year['year'] = year
        for k , v in information.items():
                color_year[k] = v
        return color_year

a = car_information('red' , '1997' , 制造商 = '中国BYD' , 型号 = '宋')
print(a)

# 8.6 将函数存储在模块中
#### 使用import导入函数码块
#### 用法/格式：import 要打开的模块/.py文件 名

# 8.6.1 导入整个模块  模块：是一个python以.py结尾，当中可以包含python对象和python语句
                   # 模块：能定义函数、类和变量，也能包含执行代码
def make_pizza(size , *toppings):
        """显示pizza的配料和大小"""
        print("\nMaking a " + str(size) + 
                "-inch pizza with the following toppings: ")
        for topping in toppings:
                print("- " + topping)
# 定义了一个函数，当中包括一些执行程序，将除去调用代码保存为名为pizza的python文件（结尾必须为.py才会储存为python文件）
# 在python中直接输入 import pizza 可以直接导入在pizza文件中定义的函数及函数中的执行程序，并且执行了
# import之后要给导出的模块赋值，我这里导出的是一个函数模块，所以要在import之后给形参传递实参（调用）

# 8.6.2 导入特定的函数
#### 用法/格式：from 模块/.py文件名称 import 指定打开函数
#### 从模块/.py文件中导出多个函数：from 模块/.py文件 import 函数1 , 函数2   在打开的函数名之间使用逗号隔开
#### 使用这种方法，可以直接调用，不需要在函数名前加模块/.py文件名称

# 8.6.3 使用as给函数指定别名
#### 用法/格式：from 模块/.py文件名称 import 指定打开函数 as 外号
#### 别名之后，每当要调用这个函数时，都可以直接使用这个函数的别名

# 8.6.4 使用as给模块指定别名
#### 用法/格式：import 模块/.py文件名称 as 别名
#### 和as函数别名用法类似，一个别名函数，一个别名模块

# 8.6.5 导入模块中的所有函数
#### 用法/格式：from 模块/.py文件名称 import *
#### 可以直接调用函数，不用句点
#### 在大项目中不推荐导入一个模块中的全部函数
#### 如果在导入模块中有和项目中相同名称的函数和变量，会对函数进行覆盖，而不是分别导入所有的函数

# 练习

# 8-15
import 测试import

测试import.make_pizza('12' , 'a' , 'b')

# 8-16
# 导入模块
import 测试import
测试import.make_pizza(12 , 'a' , 'b')

# 导入模块中的指定函数
from 测试import import make_pizza
make_pizza(12 , 'a' , 'b')

# 导入模块中的函数并别名
from 测试import import make_pizza as aa
aa(12 , 'a' , 'b')
# 有冲突

# 导入模块并别名
import 测试import as ab
ab.make_pizza(12 , 'a' , 'b')
# 导入模块别名调用时记得带句点

# 导入模块中的所有函数
from 测试import import *
make_pizza(12 , 'a' , 'b')

