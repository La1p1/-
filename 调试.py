import json
information = input('Enter your name: ')

filename = 'C:\d_text\information.json'
with open(filename , 'w') as file:
    json.dump(information , file)
    print("Welconme " + information)