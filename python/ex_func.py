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
object��һ�����࣬���֮ΪԪ�ࡣ
��python2.x�ϣ����̳�object��ĳ�֮Ϊ�����࣬�̳���object��ĳ�֮Ϊ��ʽ��
�ڶ�̳�ģʽ�У���ʽ����ù��������������ʽ����������������
��ʽ���¼��˺ܶ෽��
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