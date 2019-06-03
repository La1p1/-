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
        """初始化父类属性"""
        super().__init__(make , model , year , unit)