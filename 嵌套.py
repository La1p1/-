# 6.4 字典列表
alien0 = {'color': 'green' , 'points': 5}
alien1 = {'color': 'yeloow' , 'points': 10}
alien2 = {'color': 'red' , 'points': 15}  # 将3个alien字典存入进了aliens这个列表中

aliens = [alien0, alien1, alien2] # aliens中储存了上面3个字典的key-value

for alien in aliens:  # 将aliens存入alien这个变量中
    print(alien)      # 分别循环打印3个字典中的key-value

# 6.4 示例2 在列表中嵌套字典
aliens = [] # 创建一个空的列表
# 这里不用for循环遍历，嵌套进列表的key-value就只有一个
for alien_nummber in range(30): # 将要循环变量alien_nummber 30次
    new_alien = {'color': 'green' , 'points': '5' , 'speed': 'solw'} # 创建new_alien字典及字典中的key-value
    aliens.append(new_alien)  # 我们将创建的字典存入aliens列表中，此时如果打印列表aliens，很明显的看出字典已经循环了30次且保存在列表aliens中

print(aliens)
#### 可以把存入列表中的30个字典看做30个列表中的元素 ####

for alien in aliens[:5]:  #  再将列表aliens存入变量alien里面，现在alien这个变量中就存入有30个new_alien这个字典中的key-value，这里只遍历了列表中的前5个key-value
    print(alien)

print("还有更多......")

print("行数: " + str(len(aliens))) # 输出结果显示，最早那个空列表aliens中有30个new_alien 字典的key-value

# 相当于把字典中的key-value当做列表元素嵌套进aliens列表中，再进行访问及其他的命令
################################################### 分割线 #################################################################################
# 6.4 示例3
aliens = [] # 依旧以上一个示例，我们还是先创建了一个空的列表

for alien_nummber in range(0,30): # 循环30次
    new_alien = {'color': 'green' , 'points': 5 , 'speed': 'slow'} # 创建及定义字典的key-value
    aliens.append(new_alien) # 将30个字典嵌入进aliens这个空的列表中

# 这三个元素分别为字典中key和它相对的value
for alien in aliens[0:3]:  #### 遍历列表中的字典的前3个元素         字典嵌入进列表，当中的key-value就当做是元素 ####
    if alien['color'] == 'green': # 检查条件，如果条件返回True，就会执行下面这三行修改字典的key-value
        alien['color'] = 'yellow'
        alien['speed'] = 'medium' # 3个要修改的key-value
        alien['points'] = 10
    
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15

for alien in aliens[0:5]:  # 最后将aliens列表存入变量alien中及遍历前5个字典
    print(alien) # 打印看输出结果
print("......")

# 6.2.3 在字典中存储列表
pizza = { # 创建一个字典，其中包含pizza的crust和toppings，当toppings这个key需要有多个值的时候可以嵌套列表
    'crust': 'thick',
    'toppings': ['mushrooms' , 'extra cheese'], # 在字典中，当key的value是多个的时候可以使用嵌套列表的方式，把多个值存入列表中，这个值依然成立
    }

print("You ordered a " + pizza['crust'] + "-crust pizza" + "with the following toppings:")

for topping in pizza['toppings']: # 将pizza字典中的key-value存入变量toppings中且遍历，这里提取了字典中toppings的值，toppings的值是嵌套在列表中的两个值
    print("\t" + topping) # 打印结果

# 示例2
fav_languages = {
    'jen': ['python' , 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby' , 'go'],
    'phil': ['python' , 'haskell'], # 这是之前的一个示例，其中字典中包含了有多个value的情况，他们都被嵌套在列表中
    }

for key, value in fav_languages.items(): # 这个遍历了整个字典中的key-value，将它们存入变量中
    print("\n" + str(key.title()) + "'s fav languages are:")
    for values in value: # 因为要列举他们喜欢的语言，语言又被存储在value中，所以单独遍历语言这个value
        print("\t" + str(values.title())) # 打印结果
        
# 6.4.3 字典中嵌套字典 # user 主字典，其中包含有 aeinstein和mcuie 这两个key
user = {
    'aeinstein': { # aeinstein和mcurie 大字典，其中包含着有小字典
        'first': 'albert', # 小字典，作为大字典的value，自己也可以包含key-value
        'last': 'einstenin',
        'location': 'prnceton',
        },
    
    'mcurie': {
        'first': 'marie',
        'last': 'curie',      ###### 两个主字典中分别有两个key-value
        'location': 'paris',  ###### 两个大字典中分别有两个key-value
        },                     ###### 两个小字典中分别有三个key-value
    }

for key, value in user.items(): # 遍历主字典，将主字典的key-value存入变量 变量key为两个大字典，变量value为大字典的value
    print("\nUsername: " + key) # 这里的Username是两个大字典
    full_name = value['first'] + " " + value['last'] # 访问小字典中的key
    location = value['location']

    print("\tFull name: " + full_name.title())
    print("\tLocation: " + location.title()) # 打印两句话

# 练习
# 6-7

people = {
    'human1': {
        'name': 'weilai',
        'city': 'neijiang',
        'age': 17,
        },
    
    'human2': {
        'name': 'weijiang',
        'city': 'mianzhu',
        'age': 17
        },

    'human3': {
        'name': 'wangjin',
        'city': 'guanghan',
        'age': 18,
        },
}

for key, value in people.items():
    print("\nThey are : " + key)
    name = "\nName: " + value['name']
    city = "\nCity: " + value['city']
    age = "\nAge: " + str(value['age'])

    print("They information is: " + 
    name.title() + 
    city.title() + 
    str(age))

print("\nThis all !")

# 6-8
pets = {
    'pet1': {
        'name': 'weiwei',
        'dog': 'bomei',
        'master': 'weixiaojing'
        },

    'pet2': {
        'name': 'pangdun',
        'dog': 'bage',
        'master': 'weilai'
        },
}

for key, value in pets.items():
    print("\nThese are two cute dogs: ")
    print("\nThis is pangdun")

# 6-9
fav_places = {
    'Weijiang': ['Xian' , 'Chengdu' , 'Beijing'],
    'Wangjin': ['Xizang' , 'Tianjin' , 'Hebei'],
    'Changfu': ['Kunming' , 'Shanghai' , 'Hongkong'],
    }

for key , value in fav_places.items():
    print(str(key) + ":")
    if len(value) > 0 :
        for place in value:
            print("\t\n", place)

# 6-10
fav_nummber = {
    'weijiang': [1 , 2],
    'wangjin': [2 , 1],
    'chenchangfu': [3 , 4],
    'chenhaoran': [4 , 5],
    'xiaotianhao': [5 , 6],
    }

for name in fav_nummber.keys():
    print("\n" + str(name.title()) + "fav nummber is :")
    for nummbervalue in fav_nummber.values():
            print("\t" + str(nummbervalue))           # false

# 6-11
cities = {
    'Zizhong': {
        'country': 'China',
        'population': '100W',
        'fact': 'chuancheng',
    },

    'Deyang': {
        'country': 'China',
        'population': 'Unknow',
        'fact': 'Unknow',
    },

    'Chengdu': {
        'country': 'China',
        'population': '300W',
        'fact': 'Unknow',
    },
}

for key , value in cities.items():
    print("\n" + str(key.title()) + ": ")
    for citi_information in value.values():
        print("\t" + str(citi_information))