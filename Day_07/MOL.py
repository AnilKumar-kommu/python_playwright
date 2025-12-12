class Demo:
    def add(self,*args):    #this way we achieve method overloading
        total = 0
        for i in args:
            total = total + i
        return total

d=Demo()
print(d.add(1,2))
print(d.add(1,2,3,3,5,))
