import types
class person(object):
    def __init__(self,name):
        self.name=name

def eat(self):
    print("---%s is eat---"%self.name)
p=person("wsd")
print(p.name)
p.eat=types.MethodType(eat,p)
p.eat()
p.age=25
print(p.age)
