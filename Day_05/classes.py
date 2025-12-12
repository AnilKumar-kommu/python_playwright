class Instructor:
    def __init__(self,Instructor_name,Instructor_age,followers):
        self.name = Instructor_name
        self.age = Instructor_age
        self.followers = followers
    def display(self):
        print("Name:",self.name)
        print("Age:",self.age)



obj=Instructor('anil',25,2)
print(obj.name,obj.age,obj.followers)


# print(obj.name)
# print(obj.age)
# print(type(obj))
# obj.name="anil"
# obj.age=25
# obj.phone_number="+155555555"
# obj.email="test@gmail.com"
# obj.id=1
# obj2=Instructor()
# obj2.name="anil kumar"
# print(obj2.name)
# print(obj.name)


