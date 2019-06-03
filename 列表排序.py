# 6 书39页  3.3.1
 
cars = ['bmw','audi','toyota','subaru']
cars.sort()  #### sort() = 分类  将列表里的元素按照字母顺序排列且永久修改 ####
print(cars)

cars = ['bmw','audi','toyota','subaru']
cars.sort(reverse=True)  #### .sort(reverse=True)  将列表里的元素按照字母顺序反向的顺序排列且永久修改 ####
print(cars)              #### .sort(reverse=True)  这里的”reverse“必须是小写

 # sorted() 对列表临时排列  3.3.2

cars = ('bmw','audi','toyota','subaru')

print("here is the original list:")
print(cars)

print("\nhere is the original list:")
print(sorted(cars))   #### 可以向.sorted()使用revesr=True 进行临时反向排序 ####

print("\nhere is the original list again:")
print(cars)

 # .reverse() 倒着打印列表 3.3.3
 
cars = ['bmw','audi','toyota','subaru']
print(cars)
                  #### .reverse() 是对列表排序永久修改，但可重复使用.reverse()将其恢复
cars.reverse()    #### .reverse() = 颠倒 是反转列表里的元素排序，不是按照字母表的反转排序 ####
print(cars)

 # len() 确定列表长度(确定列表元素个数)
 
cars = ['bmw','audi','toyota','subaru']
len(cars)  #### python计算列表元素个数时是从元素1开始 ####

# 练习 书41页 3-8
 
地点 = ['sh','usa','hlj','home','js']   #### 貌似对中文没用 ####
print(地点)

print(sorted(地点))
print(地点)         #### 按照字母顺序排序 ####   


地点 = ['sh','usa','hlj','home','js']
print(地点)
                            #### 中英切换的时候，千万注意符号！！！！！  ####
地点.sort(reverse=True)
print(地点)         #### 按照字母相反顺序排序 ####  


print("核实情况:")
print(sorted(地点)) #### 核实列表内容
print(地点)


地点.reverse()   #### 颠倒列表内元素的顺序进行核实 ####
print(地点)      #### 【元素内容颠倒】

地点.reverse()
print(地点)      #### 再次使用颠倒将列表内元素恢复，确定元素内容正确 ####

地点.sort()      #### 这里是使用.sort() 列表元素以字母顺序排序 ####
print(地点)

地点.sort(reverse=True)  #### 这里使用.sort(reverse=True) 将列表内容以字母顺序相反排序 ####
print(地点)              注 ： 这里是用字母的相反顺序排列

len(地点)


#  不能再powershell里运行，但能在python运行 好奇怪
