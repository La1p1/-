 # 5 书33页  3.2

motorcucles = ['honda','yamaha','suzuki']
print(motorcucles)

motorcucles.append('ducati')
print(motorcucles)   #### append() = 附加 将元素附加到列表及 [] ####

# 添加元素

motorcucles = []

motorcucles.append('honda')
motorcucles.append('yamaha')
motorcucles.append('suziki')
motorcucles.append('大运摩托')

print(motorcucles)

# insert 插入元素及插入位置

motorcucles = ['honda','yamaha','suzuki']

motorcucles.insert(0, 'ducati')  #### 0指的是列表[] 里的honda，insert()将新元素ducati插入到0及honda的前一个位置
print(motorcucles)   #### insert() = 插入  可以在列表[] 里的任何位置添加元素 #### 

# del 删除列表元素及删除位置

motorcucles = ['honda','yamaha','suzuki']
print(motorcucles)

del motorcucles[0] #### del[] = 删除 和插入命令相反 insertp[]是插入，del是删除 ####
del motorcucles[1]
print(motorcucles)

# pop() 弹出元素

motorcucles = ['honda','yamaha','suzuki']
print(motorcucles)  #### pop() = 弹出 是将列表的末尾的一个元素弹出，以便我们访问

popped_motorcucles = motorcucles.pop()
print(motorcucles)
print(popped_motorcucles)


motorcucles = ['honda','suzuki','yamaha']

last_owned = motorcucles.pop()
print("The last motorcules I owned a " + last_owned.title() + ".")

# pop() 弹出元素位置

motorcucles = ['honda','yamaha','suzuki']

first_owned = motorcucles.pop(0)  #### 性质和前几个插入、删除一样 ####
print('The first motorcucles I owned was a ' + first_owned.title() + '.')

# remove() 根据值删除元素

motorcucles = ['honda','yamaha','suzuki']
print(motorcucles)  #### remove() 不能像前几个命令一样在括号内输入元素的位置，是直接输入元素的值并删除

motorcucles.remove('honda')
motorcucles.remove('suzuki')
print(motorcucles)
# 
motorcucles = ['honda','yamaha','suzuki','ducati']
print(motorcucles)

too_expensive = 'ducati'   #### 把ducati储存在too_e ####
motorcucles.remove(too_expensive)    #### 这里删除了ducati,但是它还是在too_e这个变量中 ####
print(motorcucles)
print("\tA " + too_expensive.title() + " is too expensive for me")  #### 注意空格 ####  


# 练习

受邀人 = ['进批','疆哥','长富']
print(受邀人)

del 受邀人[0]
受邀人.remove('长富')
print(受邀人)  ####无法来的是 疆哥
print("疆哥 无法到场")

受邀人 = ['进批','疆哥','长富']

受邀人[1] = '毛毛'

print(受邀人)

print("我找到一个更大的桌子，我可以再邀请3位朋友")

受邀人.insert(0,"浩南")
受邀人.insert(3,"肖肖")
受邀人.append("良辰") #### 添加结尾用 .append()

print(受邀人)

len(受邀人)