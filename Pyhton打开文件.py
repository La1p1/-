# 第10章 文件和异常
# 注：把测试文件放入‘来批’文件夹中进行测试
# 注：Python在当前执行的文件所在的目录中查找指定文件


# 10.1.1 读取、读取文件
# 语法：with open('文件名.文件格式') as 取个名字:
with open('包装作业.txt') as file_object:  # 使用open()函数打开文件
    print(file_object.read())                       # 打印


# 10.1.2 文件路径 从子文件中找到要打开的文件
# 语法：with open('所找的文件\文件名.文件格式') as 取个名字:
# 注：在Windows中使用反斜杠\，在Linux和OS X中使用/
with open('测试文件夹\wl.txt') as file_object:
    print(file_object.read())


# 绝对文件路径 打开不在当前py文件的文件
# 注：文件储存的路径一定要非常准确，python才能在输入的路径中找到要打开的文件
# 注：记得使用rstrip()函数删除空白换行符
i = 'C:\d_text\wl.txt'
with open(i) as file:
    print(file.read().rstrip())


# 逐行读取 一行一行的读取文件内容吧
# 注：使用for遍历打开的文件，没有使用read()函数
# 注：逐行读取的文件内容是一行一行的读取输出
i = 'C:\d_text\_text_file.txt'
with open(i) as file:
    for line in file:
        print(line.rstrip())


# 10.1.4 在with码块外访问open()的文件内容
# 注：只需在with码块中将open()的文件存入一个变量中，即可在with码块外访问
# 新函数：readlines()  方法：按行读取内容
filename = 'C:\d_text\_text_file.txt'
with open(filename) as file:        # 读取open()中的文件
    a = file.readlines()            # 将读取的文件存入一个变量中   ####调用readlines按照行读取文件中的内容

for b in a:
    print(b.rstrip())               # 在with码块中是把要读取的文件存入一个列表中，所有要使用for循环遍历打印列表中的内容


# 10.1.5 使用文件内容
# 注：将读取的文件存入一个变量中，用for将文件内容遍历添加进一个空的变量中
filename = 'C:\d_text\_text_file.txt'
with open(filename) as file:
    a = file.readlines()

text = ''
for line in a:
    text += line.rstrip()   # 遍历进text变量中

print(text)
print(len(text))

# 10.1.6 打开大型文件
# 使用列表切片，遍历显示列表的部分内容
# 注：处理数据python没有限制，内存足够就ok
filename = 'C:\d_text\_text_file.txt'
with open(filename) as file:
    a = file.readlines()

textname = ''
for line in a:
    textname += line.rstrip()

print(textname[88:99] + "... 后面还有更多")
print(len(textname))

# 练习
# 10-1  三中读取文件内容方法
with open('C:\d_text\_text_file.txt') as file:
    a = file.read()
    print(a)
 
with open('C:\d_text\_text_file.txt') as file:
    for i in file:
        print(i.rstrip())


with open('C:\d_text\_text_file.txt') as file:
    lines = file.readlines()

i = ''
for line in lines:
    i += line
print(i)

# 10-2
with open('C:\d_text\wl.txt') as file:
    lines = file.readlines()

for line in lines:
    line1 = line.replace('Python' , 'C')
    print(line1.rstrip())

# 10.2.1 写入空文件
# 这段代码把一串字符串写入了文件_text_file中，修改了之前.txt文件的中的内容
# 注：若写入一个有内容文件中，会替换掉原本内容
# 注：如果没有提前创建需要写入内容的文件，依旧可以使用这样的写法，会在路径中创建文件夹
filename = 'C:\d_text\_text_file.txt'

with open(filename , 'w') as file:   # w = write()   r = read()
    file.write('I Love Python.')     # 将内容写入文本文件时， Python会清空文件中的内容，转而使用新写入的内容

# 10.2.2 写入多行
# 使用write函数多写了一段话
# 注：在编辑器中，给代码使用换行符使txt文本看起来更整洁
# 注：要写入内容需在Python中运行，才能起效
information = 'C:\d_text\learning.txt'

with open(information , 'w') as file:
    file.write('I Love Python.\n')
    file.write('I Love Programming.\n')

# 10.2.3 附加文件
# 使用实参'a'给文件写入内容，而不覆盖原内容
# 注：附加内容会被写入文件的结尾
information = 'C:\d_text\learning.txt'

with open(information , 'a') as file:
    file.write('这是一条附加文件\n')    # 如果在python中运行这段代码两次，则会将四段附加内容写入txt文件内
    file.write('这是另一条附加文件\n')

# 练习
# 10-3
i = 'C:\d_text\guest.txt'

with open(i , 'a') as file:
    file.write('Name: ')
    name = input("Enter your name: ")
    file.write(name)

# 10-4
i = 'C:\d_text\guest_book.txt'

with open(i , 'w') as file:
    file.write('Name: ')
    while True:
        name = input("Enter your name here , Enter 'q' to quit if you want: ")
        if name == 'q':
            break
        file.write(name)

# 10-5
a = 'C:\d_text\language.txt'

with open(a , 'a') as file:
    while True:
        language = input("What program language do you like? (Enter here): ")
        if language != 'Python':
            break
        file.write(language)