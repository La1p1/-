# 第四章 4.1 书44页
 
magicians = ['alice','david','carilina']
for magician in magicians:              #### for循环对列表重复使用命令 ####
	print(magician)                     #### for循环后面没有代码，循环结束 ####
                                        #### for会对列表每一个元素进行命令，不管包括多少元素 #### 

# for 执行更多作 4.1.2

magicians = ['alice','david','carolina']
for magician in magicians:
    print(magician.title() + ", that was a greet trick!" + "\n")  #### 在for循环中，包含多少代码都可以 ####

#### 换行符加在末尾

# 4.1.3

for magician in magicians:
    print(magician.title() + ",that is greet trick!")   #### 在for循环里，将列表里的元素依次重复命令 ####
    print("I will see your trick next time," + magician.title()+ ".\n")  
    #### 以上两条print语句要有缩进才会循环 ####  
    #### 下面这条没有缩进，所以没有缩进，就没有循环 ####
print("Thank you ,everyone. That is greet magic show!")

# 4.2.2

for magician in magicians :            #### 注：这段代码是错误的示范 ####
    print(magician.title() + ",that was a greet trick!")
print("I will see your trick  next time!" + magician.title() + ".\n")   #### 这行前面没有缩进，所以没有起到循环 ####
    #### 由于变量最终值是"carolina"所以for循环只执行了列表的最后一项元素 ####

# 4.2.4

magicians = ['alice','david','carolina']
for magician in magicians:    #### 此处如果漏掉":"符号将导致语法错误 #### 
    print(magician.title() + ",that was a greet trick!")
    print("I will see your trick nxet time," + magician.title() + "\n")
    print("Thank you everyone , that was a greet magic show !")
    #### 上面的这一段没有缩进，所以终端输出也将此段进行了循环 ####

    #### 为了避免缩进错误，只需要缩进需要缩进的代码 ####
    #### 只要在for循环中对每个元素执行的代码都需要缩进 ####


    # 练习

pizzas = ["芝士披萨",'海鲜披萨','香肠披萨']
for pizza in pizzas:
    print(pizza.title() + ",that's my favorite food!")
    print("i like pizza , althought they are not healthy , but i still like," + pizza.lower()+ ".")

print("i reayll like pizza" + "\n")


animals = ['兔子','猫','狗']
for animal in animals:
    print("A" + animal.title() + "would make a great pet.")

print("they are so cute" + "\n\t")