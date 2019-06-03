# 和之前的导入函数模块类似    

# 语法：from 模块 import 类
from 继承 import Car

new_car = Car('toyota' , 'a4' , 2019 , 'KM')
print(new_car.get_descriptive_name())  

new_car.odometer_reading = 100
new_car.read_odometer()

# 从一个模块中打开其中的两个类   
# 语法：from 模块 import 类名1 , 类名2      
# 打开的类与类之间用逗号隔开
from 两个类 import Car , Ecar
# 分别调用模块中两个类
tesla = Car('tesla' , 'model s' , 2019 , 'KM')
print(tesla.get_descriptive_name())

beetle = Ecar('toyota' , 'model s' , 2019 , 'KM')
print(beetle.get_descriptive_name())

# 导入整个模块
# 语法：import 类名
# 注：打开后，使用句点表示法访问  # 句点表示法语法： 实例 = 模块名.类名(属性 ， 属性 ， 属性)
import 继承

beetle = 继承.Car('toyota' , 'model s' , 2019 , 'KM')
print(beetle.get_descriptive_name())

tesla = 继承.Ecar('audi' , 'a4' , 2019 , 'KM')
print(tesla.get_descriptive_name())

# 导入模块中的所有类（不推荐使用）
# 语法：from 模块名 import *
# 弊端：各个类容易引起冲突     # 推荐使用导入整个模块的方法，再访问其类的方法
from 继承 import *

# 同时导入多个类
# 语法：from 模块 import 类
#      from 模块 import 类


# 练习 

# 9-10
from 两个类 import Car
car = Car('audi' , 'a4' , 'KM' , 2019)
print(car.get_descriptive_name())