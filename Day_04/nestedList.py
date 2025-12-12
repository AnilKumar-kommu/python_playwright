

list=[1,2,3,[8,9,10,11],15] # nested list mean list with in  list
lenght=len(list)
#print(L)
#print(list[3])#[8, 9, 10, 11]
#print(list[2]) #3
# we call like this below lenght -1
#print(length(list)-1) #TypeError: 'int' object is not callable
#print(list[lenght-2]) #[8, 9, 10, 11]

print(list[3][0:2]) #[8, 9]
print(list[3][2:4]) #[10, 11]
print(list[3]) #[8, 9, 10, 11]
print(list[3][:]) #[8, 9, 10, 11] printed within the list



