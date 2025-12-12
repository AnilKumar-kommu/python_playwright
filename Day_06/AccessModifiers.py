class student():
    def __init__(self, name,age,rollno):
        self.name = name # public variable
        self.__age = age
        self._rollno = rollno  # Protected variable
    def diplay(self):
        print(f'hi m name  {self.name} im from student class ')
class Branch(student):

    pass


s1 = student("anil",20,20)
#b1 = Branch('Branch1',1,2)
print(dir(s1))
#s1=student('anil')
# print(s1.name)
# s1.diplay()

