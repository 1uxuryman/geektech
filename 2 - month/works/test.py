class Type():
    pass
class Str(Type):
    def printtype():
        print("str")

class Integer(Type):
    def printtype():
        print("int")




a = Str
b = Integer

a.printtype()
b.printtype()