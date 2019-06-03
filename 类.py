# 第9章 类 书139页

# 9.1.1 创建Dog()类
class Dog(): # 创建一个类，类的格式：class 类名():  类名要以大写打头定义
    """一次模拟小狗的简单尝试"""

    def __init__(self , name , age): # 在类中，定义的函数成为方法，__init__为特殊的方法，即Python默认方法，每次运行这方法时都会自动打开
        """初始化属性name和age"""     # 在方法init中有三个形参，形参self必不可少，形参self必须在其他形参之前，形参可以和self进行绑定，调用绑定的形参时，都会自动传入给形参self
        self.name = name # 以self.为前缀的变量都可以被类中其他方法使用、访问
        self.age = age   # self都会自动传递，不需要给self传值
                         # 形参和self进行绑定  # self.name = name 获取形参name的值，并存入变量name中     # 绑定格式: self.形参 = 变量
    def sit(self):
        """模拟小狗被命令蹲下"""
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        """模拟小狗打滚的命令"""
        print(self.name.title() + " rolled over!")

# 9.1.2 根据类创建实例(接9.1.1的类)
# 使用句点表示法访问默认方法__init__   # 调用方式同函数调用相似
class Dog():
    """一次模拟小狗的简单尝试"""

    def __init__(self , name , age):
        """初始化属性name和age"""
        self.name = name
        self.age = age

    def sit(self):
        """模拟小狗被命令蹲下"""
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        """模拟小狗打滚的命令"""
        print(self.name.title() + " rolled over!")
                        #使用句点表示访问类中的实例的值，和函数调用赋值类似 
my_dog = Dog('aaa' , 5) # 将Dog对象中的两个属性/实参存入变量my_dog中，两个属性分别对应了name 和 age

print("My dog's name is " + my_dog.name.title() + " !")      # 类似于函数的调用阶段，通过找到实例my_dog再通过self.name找到与实例相关的属性nama  # self.name = name
print("My dog's age is " + str(my_dog.age) + " years old !") # 访问age同理

# 使用句点表示法访问其他方法
class Dog():
    """一次模拟小狗的简单尝试"""

    def __init__(self , name , age , color):
        """初始化属性name和age"""
        self.name = name
        self.age = age
        self.color = color

    def sit(self):
        """模拟小狗被命令蹲下"""
        print(self.name.title() + " is now sitting .")

    def roll_over(self):
        """模拟小狗打滚的命令"""
        print(self.name.title() + " rolled over !")

    def run(self):
        """模拟小狗奔跑"""
        print("the dog's color is " + self.color.upper() + " , the dog is running now !")

my_dog = Dog('BBB' , 7 , 'black') # 找实例和属性这段必不可缺
my_dog.sit() # 访问除默认方法__init__以外的其他方法
my_dog.roll_over()
my_dog.run()

# 创建多个实例
class Dog():
    """一次模拟小狗的简单尝试"""
    def __init__(self , name , age , color):
        """初始化属性name和age"""
        self.name = name
        self.age = age
        self.color = color

    def sit(self):
        """模拟小狗被命令蹲下"""
        print(self.name.title() + " is now sitting .")

    def roll_over(self):
        """模拟小狗打滚的命令"""
        print(self.name.title() + " rolled over !")

    def run(self):
        """模拟小狗奔跑"""
        print("the dog's color is " + self.color.upper() + " , the dog is running now !")

dog1 = Dog('aaa' , 6 , 'white')
dog2 = Dog('bbb' , 7 , 'black')

print("Dog1 name's " + dog1.name.upper() + " !")
print("Dog2 name's " + dog2.name.upper() + " !")
print("\n上面是名字，下面是其他信息")
print("\nDog1 age's " + str(dog1.age) + " !")
print("Dog2 color's " + dog1.color.upper() + " !")

# 练习

# 9-1
class Restaurant():
    def __init__(self , restaurant_name , cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def d_restaurant(self):
        print("这个餐馆叫" + self.restaurant_name.upper() + "。")

    def open_restaurant(self):
        print("烹饪类型是" + self.cuisine_type.upper() + "。")

restaurant = Restaurant('aaa' , 'bbb')

print(restaurant.restaurant_name.upper())
print(restaurant.cuisine_type.upper())

restaurant.d_restaurant()
restaurant.open_restaurant()

# 9-2
class Restaurant():
    def __init__(self , restaurant_name , cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def d_restaurant(self):
        print("这个餐馆叫" + self.restaurant_name.upper() + "。")

    def open_restaurant(self):
        print("烹饪类型是" + self.cuisine_type.upper() + "。")

restaurant1 = Restaurant('aaa' , 'bbb')
restaurant2 = Restaurant('ccc' , 'ddd')
restaurant3 = Restaurant('eee' , 'fff')

restaurant1.d_restaurant()
restaurant2.d_restaurant()
restaurant3.d_restaurant()

restaurant1.open_restaurant()
restaurant2.open_restaurant()
restaurant3.open_restaurant()

# 9-3
class User():

    def __init__(self , first_name , last_name , age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def describe_user(self):
        print("First name is: " + self.first_name.upper() + ".")
        print("Last name is: " + self.last_name.upper() + ".")
        print("I am " + str(self.age) + " years old.")

    def greet_user(self):
        full_name = self.first_name + self.last_name
        print("Hello " + full_name.upper() + " ! I am " + str(self.age) + " years old !")

    def gree_users(self):
        '''随意加了一段试手，这段方法没用'''
        full_name = self.first_name + self.last_name
        print("Hello " + full_name.upper() + " ! I am " + str(self.age) + " years old !")

user1 = User('魏' , '来' , 18)
user2 = User('王' , '进' , 18)

user2.describe_user()
user2.greet_user()

user1.describe_user()
user1.gree_users()

# 9.2 使用类和实例
# Car类
class Car():
    """模拟汽车的简单尝试"""
    
    def __init__(self , make , model , year): # def默认的方法，self打头，除self外还有三个形参在其中
        """描述汽车属性"""
        self.make = make # 把各个形参和self进行绑定，方便自动传输属性
        self.model = model
        self.year = year
    
    def get_descriptive_name(self): # def一个方法，负责描述init方法中的形参
        """返回汽车属性的信息"""
        car_information = str(self.year) + ' ' + self.make + ' ' + self.model # 将所有的形参以字符串的形式存入一个变量中
        print("Year: " + str(self.year))
        print("\nMake: " + self.make.upper())
        print("\nModel: " + self.model.upper()) 
        return car_information.upper() # 将储存属性的变量返回，这样省去了print步骤，碰到字符串就要返回值

new_car = Car('audi' , 'aaa' , '2019') # 定义实例和值，通过self传输给各个属性赋值
print(new_car.get_descriptive_name()) # 在类中打印展示实例中的值

# 9.2.2 给属性赋默认值
class Car():

    def __init__(self , make , model , year , unit):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 2 # 在默认的方法中定义了一个默认值  注：这个属性没有出现在形参表中
        self.unit = unit

    def get_descriptive_name(self):
        car_information = str(self.year) + ' ' + self.make.upper() + ' ' + self.model.upper()
        return car_information

    def read_odometer(self): # 定义一个方法，用于显示汽车的行驶里程
        """打印汽车的行驶路程"""
        print("这辆车的行驶里程为" + str(self.odometer_reading) + self.unit) # 在这个方法中可以直接调用那个默认值

new_car = Car('audi' , 'aaa' , '2019' , 'KM') # 通过self的自动传输，给类中的属性赋值
print(new_car.get_descriptive_name()) # 将实例中的值传输给方法中使用
new_car.read_odometer() # 调用方法，访问这个方法中的执行程序

# 9.2.3 修改属性的值

# 修改属性值得第一种方法：通过实例直接修改属性值
# 直接在调用阶段通过实例修改
class Car():

    def __init__(self , make , model , year , unit):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 333 # 在init默认方法中定义了个默认值，需修改
        self.unit = unit

    def get_descriptive_name(self):
        car_information = str(self.year) + ' ' + self.make.upper() + ' ' + self.model.upper()
        return car_information

    def read_odometer(self):
        """打印汽车的行驶路程"""
        print("这辆车的行驶路程为" + str(self.odometer_reading) + self.unit + ", 是辆新车。")

new_car = Car('audi' , 'aaa' , '2019' , 'KM')
print(new_car.get_descriptive_name())

new_car.unit = '千米'          # 这段试着修改init方法中的第一个属性，未成功，但是能随意修改init方法中的最后一个方法  ？？？
new_car.odometer_reading = 444 # 通过实例在方法中访问指定的属性   # 格式：实例名.属性（需要访问/修改的属性） = 修改内容/值
new_car.read_odometer()

# 修改属性值得第二个方法：通过方法修改属性值
# 将要修改的属性存入一个新的变量中，在调用阶段进行修改
class Car():

    def __init__(self , make , model , year , unit):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 333
        self.unit = unit

    def get_descriptive_name(self):
        car_information = str(self.year) + ' ' + self.make.upper() + ' ' + self.model.upper()
        return car_information

    def read_odometer(self):
        """打印汽车的行驶路程"""
        print("这辆车的行驶路程为" + str(self.odometer_reading) + self.unit + ", 是辆新车。")

    def update_odometer(self , mileage): # def一个方法，其中包括除self另一个属性
        """把mileage设置成指定的值"""
        self.odometer_reading = mileage # 将要修改的属性存入新的属性中  # 注：在调用时，给这个属性赋值，也是在修改这个属性的值/内容

new_car = Car('audi' , 'aaa' , '2019' , 'KM')
new_car.update_odometer(444) # 给updata_odometer方法赋值
new_car.read_odometer()

# 修改属性得第三个方法：通过方法对属性值进行递增
class Car():

    def __init__(self , make , model , year , unit):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 333
        self.unit = unit

    def get_descriptive_name(self):
        car_information = str(self.year) + ' ' + self.make.upper() + ' ' + self.model.upper()
        return car_information

    def read_odometer(self):
        """打印汽车的行驶路程"""
        print("这辆车的行驶路程为" + str(self.odometer_reading) + self.unit + ", 是辆新车。")

    def update_odometer(self , mileage):
        """把mileage设置成指定的值"""
        self.odometer_reading = mileage

    def inc_odometer(self , miles):
        """以100递增"""
        self.odometer_reading += miles  # 

new_car = Car('toyota' , 'aaa' , '2019' , 'KM')
print(new_car.get_descriptive_name())

new_car.update_odometer(400)
new_car.read_odometer()

new_car.inc_odometer(100)
new_car.read_odometer()

# 练习

# 9-4
class Restaurant():
    def __init__(self , restaurant_name , cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def d_restaurant(self):
        print("餐馆：" + self.restaurant_name)
        print("有" + str(self.number_served) + "在用餐")

    def open_restaurant(self):
        print("餐馆状态：" + self.cuisine_type)

aaa = Restaurant("老地方" , "将会一直开着")

aaa.d_restaurant()
aaa.open_restaurant()

# 第二段
class Restaurant():
    def __init__(self , restaurant_name , cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def d_restaurant(self):
        print("餐馆：" + self.restaurant_name)
        print("有" + str(self.number_served) + "在用餐")

    def open_restaurant(self):
        print("餐馆状态：" + self.cuisine_type)

    def set_number_served(self , 人数):
        self.number_served = 人数

    def in_number_served(self , 递增人数):
        self.number_served += 递增人数

aaa = Restaurant("老地方" , "将会一直开着")

aaa.set_number_served(100)
aaa.in_number_served(100)
aaa.d_restaurant()
aaa.open_restaurant()

# 9-5
class User():

    def __init__(self , first_name , last_name , age , login_att):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.login_att = 0

    def describe_user(self):
        print("First name is: " + self.first_name.upper() + ".")
        print("Last name is: " + self.last_name.upper() + ".")
        print("I am " + str(self.age) + " years old.")

    def greet_user(self):
        full_name = self.first_name + self.last_name
        print("Hello " + full_name.upper() + " ! I am " + str(self.age) + " years old !")

    def inc_login_att(self , 递增数):
        self.login_att += 递增数

    def reset_login_att(self , 重置):
        self.login_att = 0

    def gree_users(self):
        '''随意加了一段试手，这段方法没用'''
        full_name = self.first_name + self.last_name
        print("Hello " + full_name.upper() + " ! I am " + str(self.age) + " years old !")

user1 = User('魏' , '来' , 18 , 17)
user2 = User('王' , '进' , 18 , 17)

user2.describe_user()
user2.greet_user()

user1.describe_user()
user1.gree_users()
