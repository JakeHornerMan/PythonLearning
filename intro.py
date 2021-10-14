import json

items = json.loads('[{"id": 1, "text": "Item 1"},{"id": 2, "text": "Item 2"}]')

for item in items:
    print(item['text'])

# Print welcome message
print('hello world') 

my_list = [10,20,30,40,50]
for i in my_list:
    print(i)

my_tuple = (1,2,3,4,5,6,7,8,9,10)
for i in my_tuple:
    print(i)

my_dictionary = {'name': 'Jake', 'age': '23', 'occupation': 'Soon to be Software Developer'}
for key,val  in my_dictionary.items():
    print("My {} is {}".format(key, val))

my_set = {10,20,30,40,50,10,20,30,40,50}
for i in my_set:
    print(i)