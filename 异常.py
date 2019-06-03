# 异常 10.4
# 在try码块中写入要测试的代码，如果try码块中的代码没有出错，就会跳过excep中的代码，运行其后的代码
# 在except写入你认为在try码块中会出现的错误，如果依旧出错就是自己的问题了
try:
    with open('C:\d_text\_text') as file:
        file.read()
except FileNotFoundError:
    print("错误")

# 10.3.4 try-except-else码块
# 可在try-except中添加else码块
# 不管try结果如何，都会运行except或者else任意一块码块
# 注：最好不要让用户在使用的时候，看到程序出错
print("Give me two nummbers , and I'll divide them.")
print("Enter 'q' to quit.")

while True:
    first_nummber = input("First Nummber: ")
    if first_nummber == 'q':
        break
    second_nummber = input("Sceond Nummber: ")
    if second_nummber == 'q':
        break
    try:
        answer = int(first_nummber) / int(second_nummber)     # try answer
    except ZeroDivisionError:                                 # 如果出错运行except中的代码
        print("'0'不能被除！！！")
    else:                                                     # 如果try answer没有出错，直接跳过except码块，转而运行else码块
        print(answer)

# 10.3.5 处理FileNotFoundError
# 注：在使用try时，需将try放在认为出错的代码前，例如：这段是open函数出错（找不到文件）所以将try放在open函数前
try:
    with open('C:\d_text\_text') as file:
        file.read()
except FileNotFoundError:
    information = "You can't FOUND FILE in your computer!"
    print(information)

# 10.3.6 分析文本
# 函数split() 以空格为分隔符将字符串拆分成多个部分
# 通过函数split()会将a变量中这个的字符串变化成为有三个元素的列表
a = "aaa bbb ccc"
a.split()

#### 这段屡清楚存入的变量
filename = 'C:\d_text\guest_book.txt'

try:
    with open(filename) as file:
        contents = file.read()
except FileNotFoundError:
    information = "You can't FOUND FILE in your computer!"
    print(information)
else:
    # 计算打开的文件有多少字符
    words = contents.split()
    num_words = len(words)
    print("The file " + filename + " has about " + str(num_words) + " words.")

# 10.3.7 使用多个文件
# 注：使用函数定义，反复调用函数可以做到查看多个文件
def conunt_words(filename):
    try:
        with open(filename) as file:
            contents = file.read()
    except FileNotFoundError:
        print("You can't FOUND FILE in your computer! ")
    else:
        words = contents.split()
        num_words = len(words)
        print(num_words)

filename = 'C:\d_text\guest_book.txt'
conunt_words(filename)

filename = 'C:\d_text\guest.txt'
conunt_words(filename)

# 反复调用函数，打开两个文件
def conunt_words(filename):
    with open(filename) as file:
        print(file.read())

filename = 'C:\d_text\guest.txt'
conunt_words(filename)

filename = 'C:\d_text\guest_book.txt'
conunt_words(filename)

# 使用for循环可以循环打开文件内容
# 注：和def的打开文件的方法类似，不过推荐使用def函数调用的方法打开
# 注：将打开的文件存入一个列表中，使用for循环分别打开文件
def conunt_words(filename):
    with open(filename) as file:
        print(file.read())

filenames = ['C:\d_text\guest_book.txt' , 'C:\d_text\guest.txt' , 'C:\d_text\wl.txt']
for filename in filenames:
    conunt_words(filename)

# 10.3.8 不显示出错
# 注：在except中使用pass后，如果程序出错，也不会有任何提醒
# 注：就算是代码中未找到一个文件也会继续运行
def conunt_words(filename):
    try:
        with open(filename) as file:
            contents = file.read()
    except FileNotFoundError:
        # pass还能充当占位符，告诉此处的except什么都不用做
        pass
    else:
        words = contents.split()
        num_words = len(words)
        print(num_words)
                                          # 第二文件未找到路径
                                          # 注：这个错误仅供测试
filenames = ['C:\d_text\guset_book.txt' , 'C:\d_text\uset.txt' , 'C:\d_text\wl.txt']
for filename in filenames:
    conunt_words(filename)

# 练习
# 10-6
try:
    print("Enter two nummbers to add.")
    num1 = input("Enter a nummber: ")
    num2 = input("Enter a nummber: ")
    answer = int(num1) + int(num2)
    print(answer)
except ValueError:
    print("你的输入格式有问题，无法计算...")

# 10-7
while True:
    try:    
        num1 = input("请输入第一个数字： ")
        num2 = input("请输入另一个数字： ")
        answer = int(num1) + int(num2)
        print(answer)
    except ValueError:
        print("你的输入格式有问题，无法计算...")

# 10-8 

# 10-9
# 注：本题中的错误仅供测试
try:
    with open("C:\d_text\cat.txt") as cat:
        cat.read()
except FileNotFoundError:
    pass