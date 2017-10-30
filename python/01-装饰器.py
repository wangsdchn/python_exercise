def func_arg(arg="hello"):
	def w1(func):
		print("----正在装饰1----")
		def inner():
			print("---正在验证权限1---")
			func()
		return inner
	return w1
def func_arg(arg="hello"):
	def w2(func):
		print("----正在装饰2----")
		def inner():
			print("---正在验证2---")
			func()
		return inner
	return w2

@func_arg("haha")
def f1():
    print("---f1---")
@func_arg("heihei")
def f2():
    print("---f2---")
f1()
f2()

