#dictionary in python
# in dictionaries  are uesd to store the values in key: values pairs
# dictionary alos mutable we can change the update the value by the key values
# in the dictionary doesn't allow the duplicate values

# mydic={
#     "brand": "ford",
#     "model": "new gen",
#     "year" : "2024"
#       }
#
# print(mydic)
# Approach - 2 using the dic() constractor

# dic1=dict(name="anil",age=30,country="india")
# print(dic1)

# by creating the key value pair
dic2={"brand": "aadi",
      "model":"new250",
      "year":2024,
      "color": "red"
      }
# print("after changing the color by bu key value: ",dic2)
# # access the item form the dictionary
#
# dic2["color"] = "green"
# print("after changing the color by bu key value: ", dic2)

#3.Get Key : Keys() method will return the list of all the dictionary
# print("data came fro the by key method: ",dic2.keys())
#
# print("data came from the values of the method: ",dic2.values())

#print(dic2.items()) # printed with the key and values like this : dict_items([('brand', 'aadi'), ('model', 'new250'), ('year', 2024), ('color', 'red')])

# now i want check particular key is existed or not

# if "model" in dic2:
#     print("exist")
# else:
#     print("not exist")

# how we can add item to the dictionary

# dic2["color2"]="red"
# print("after added new item : ",dic2)
# dic2.update({"color":"green3"})
# print("after update by key value : ",dic2)

# now I want Update the two value at time

# dic2.update({"color":"yellow"})
# dic2.update({"model":"tata zest"})
# print("after update two values at a time : ",dic2)
#
# # removing item from the dictionary
#
# dic2.pop("color") # key is mandatory
# dic2.popitem() # it is defaulter deleted last item of the dictionary
#del dic2 # it will delete the complete dictionary n variable level


# copy the dictionary
# dic3=dic2.copy()
# print(dic2)
# print(dic3)

# length of dictionary

# print(len(dic2))

# for x in dic2: # all key value will be printed
#     print(x)

for x in dic2.keys(),dic2.values(): print(x)




