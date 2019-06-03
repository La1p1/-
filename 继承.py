# 9.3 继承 书147页

# 9.3.1 子类的方法__init__
# 创建子类时，必须确保父类包含在当前文件中，父子类确保在同一文件中
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
        print("这辆车的行驶路程为" + str(self.odometer_reading) + self.unit + "是辆新车。")

    def update_odometer(self , mileage):
        """把mileage设置成指定的值"""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("你不能回调行驶里程值！")

    def inc_odometer(self , miles):
        """以100递增"""
        self.odometer_reading += miles
                 
class Ecar(Car):   # 把父类继承给子类，子类有父类的全部功能、方法    # 语法： class 子类(继承的父类):
    """电动车的特点"""
    def __init__(self , make , model , year , unit): # def子类中的默认方法__init__
        """初始化父类属性"""
        super().__init__(make , model , year , unit) # super()为超类 即父类   # 将子类和父类关联起来，类似于父类中默认方法下self绑定属性的方式
                                                     
new_tesla = Ecar('tesla' , 'model s' , 2019 , 'KM')  # 在调用时，有多少个属性，就要赋予相同个数的值
print(new_tesla.get_descriptive_name())              # 通过在子类中的实例赋值调用父类中的方法

# 9.3.3 给子类定义属性和方法
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
        print("这辆车的行驶路程为" + str(self.odometer_reading) + self.unit + "是辆新车。")

    def update_odometer(self , mileage):
        """把mileage设置成指定的值"""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("你不能回调行驶里程值！")

    def inc_odometer(self , miles):
        """以100递增"""
        self.odometer_reading += miles

class Ecar(Car):
    """电动车的特点"""

    def __init__(self , make , model , year , unit):
        """初始化电动车特有的属性"""
        super().__init__(make , model , year , unit) # 父子类绑定
        self.battery = 70                            # 在子类中定义了一个默认属性值，负责自动传输方法battery_size中的描述

    def battery_size(self):
        """打印一条描述battery值得语句"""
                                    # 默认值传输
        print("This car has a " + str(self.battery) + " -KWH battery.")

new_tesla = Ecar('tesla' , 'model s' , 2019 , 'KM')  # 实例  注：方法中的属性个数要和实例中的值个数一致
print(new_tesla.get_descriptive_name())              # 将实例传输给父类的方法
new_tesla.battery_size()                             # 调用子类中的方法

# 9.3.5 将实例用作属性
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
        print("这辆车的行驶路程为" + str(self.odometer_reading) + self.unit + "是辆新车。")

    def update_odometer(self , mileage):
        """把mileage设置成指定的值"""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("你不能回调行驶里程值！")

    def inc_odometer(self , miles):
        """以100递增"""
        self.odometer_reading += miles

class Battery():
    """模拟电动车电瓶的尝试"""
    def __init__(self , battery_size = 70):
        """初始化电瓶属性"""
        self.battery_size = battery_size

    def battery(self):
        """描述电瓶容量"""
        print("This car has a " + str(self.battery_size) + " -KWH battery.")

class Ecar(Car):
    """电动车独特之处"""
    def __init__(self , make , model , year , unit):
        """初始化父类属性，再初始化子类特有的属性"""
        super().__init__(make , model , year , unit)
        self.battery = Battery()

new_teala = Ecar('tesla' , 'model s' , 2019 , 'KM')
print(new_teala.get_descriptive_name())
new_teala.battery.battery()   