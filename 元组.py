# 元组 书59页

# 4.6
dimensions = (200,50)        # 和定义列表有点像，索引元素也很像
print(dimensions[0])
print(dimensions[1])
# 无法修改元组内的元素
dimensions[0] = 250          # 定义元组之后，元组中的元素无法修改

# 4.5.2
dimensions = (200,50)        # 和列表一样，同样可以对元组使用for循环
for dimension in dimensions:
    print(dimension)

# 4.5.3
dimensions = (200,50)        # 定义一个元组之后无法直接对元组中的元素进行修改
print("Original dimensions") # 可以重新定义元组对其进行修改
for dimension in dimensions:
    print(dimension)

dimensions = (400,250)
print("Modified dimensions")
for dimension in dimensions:
    print(dimension)
# 如果要一组值需要在程序中一直存在切不被修改，可以使用元组

# 练习
foods = ('beef','ice','chicken','pizza','coke')    # 在元组中，除了数字其他内容都要加 ' '
for food in foods:
    print(food.title())

# 核实确实无法修改
foods[0] = 'cake'

foods = ('beef','ice','chicken','pizza','coke','cake','sushi')
for food in foods:
    print(food.title())