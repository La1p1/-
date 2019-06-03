# pytho切片 书54页

# 4.4.1 切片

players = ['charles','martina','machael','florence','eli']
print(players[0:3])                     # 输出列表0-3的元素  元素位置相对-1

players = ['charles','martina','machael','florence','eli']
print(players[1:4])                     # 输出列表2-4的元素  始于martina，终于florence  python中元素位置从0开始依次往后

players = ['charles','martina','machael','florence','eli']
print(players[:4])                      # 如果没有指出从哪里开始索引，列表将会从头开始索引元素位置

players = ['charles','martina','machael','florence','eli']
print(players[2:])                      # 反之如果没有指出到哪里停止，则列表会输出到列表末尾

players = ['charles','martina','machael','florence','eli']    # 从列表末尾开始挨个索引
print(players[:-3])                     # 负数是从列表末尾开始索引，这是从末尾开始索引后三个元素

# 4.4.2 遍历切片

players = ['charles','martina','machael','florence','ele']

print("\n\there are the first three players on my team:")
for player in players[:3]:              # 从列表开头开始索引
    print(player.title())

# 4.4.3 复制列表

my_food = ['pizza','falafel','carrot cake']
friend_foods = my_food[:]               # 这里没有明确指定列表里的元素，所以是从列表的开始索引到列表末尾
# 没有[:]行不通
print("my favorite foods are:")
print(my_food)

print("\nMy friend's favorite foods are:")
print(friend_foods)

friend_foods.append('shit')             # 将shit加入到friend_foods的列表中
del my_food[2]                          # 将my_food列表中的第二个元素删除

print("my favorite foods are:")         # 打印
print(my_food)

print("\nMy friend's favorite foods are:")
print(friend_foods)

# 练习 书58页

# 4-10
nummbers = ["1",'2','3','4','5','6','7']
print(nummbers[:3])

nummbers = ["1",'2','3','4','5','6','7']
print(nummbers[2:5])

nummbers = ["1",'2','3','4','5','6','7']
print(nummbers[-3:])


# 4-11
my_food = ['pizza','falafel','carrot cake']
friend_food = my_food[:]

my_food.append('coke')
friend_food.append('apple')

print(my_food);print(friend_food)

for my_foods in my_food:
    print("My fav food are" + " " + my_foods + " " + "!")

for friend_foods in friend_food:
    print("My friend fav food are" + " " + friend_foods + " " + "!")


# 4-11

my_foods = ['pizza','falafel','carrot cake']
for my_food in my_foods:
    print(my_food.title())