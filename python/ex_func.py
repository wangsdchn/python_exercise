# -*- coding: utf-8 -*-
"""
This is exercises about functions and class.
"""
def extendList(val,list=[]):
    list.append(val)
    return list
list1=extendList(10)
list2=extendList(123,[])
list3=extendList('a')
print "list1=%s" %list1
print "list2=%s" %list2
print "list3=%s" %list3

"""
object是一个基类，或称之为元类。
在python2.x上，不继承object类的称之为经典类，继承了object类的称之为新式类
在多继承模式中，新式类采用广度优先搜索，旧式类采用深度优先搜索
新式类新加了很多方法
"""
class Parent(object):
    x=1
class Child1(Parent):
    pass
class Child2(Parent):
    pass

print Parent.x, Child1.x, Child2.x
Child1.x=2
print Parent.x, Child1.x, Child2.x
Parent.x=3
print Parent.x, Child1.x, Child2.x