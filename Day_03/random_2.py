import random
#
# a=random.randint(0,1)
# if a==1:
#     print('heads')
# else:
#     print('tails')

name = input('Enter your msg : ')
name_list=name.split(' ')
length = len(name_list)
a=random.randint(0,length-1)
print(f'{name_list[a]} {name_list[a+1]}')

