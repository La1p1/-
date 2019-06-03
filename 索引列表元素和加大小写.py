  # 4 第三章 3.1


bicycles = ['trek','cannondale','redline','specialized']
print(bicycles[0].upper())  #### 索引列表是从 0 开始，不是从 1 开始 ####
print(bicycles[1].upper())
print(bicycles[2].lower())  
print(bicycles[3].lower())
print(bicycles[-1].upper())

 #### lower()是全字母小写
 #### upper()是全字母大写
 #### title()是首字母大写

message = "My first bicycle was a " + bicycles[0].title() + "."

print(message)

 # 练习

names = ['进批','长富','疆哥']
print(names[0],names[1],names[2])

message2 = "\n\t他叫"+names[0]+"。"+"\n\t他叫"+names[1]+"。"+"\n\t他叫"+names[2]+"。" 

print(message2)
