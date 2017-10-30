def func_arg(arg="hello"):
    def print_(func):
        print("---正在装饰%s----"%arg)
        def inner():
            print("----1-----")
            func()
        return inner
    return print_
#f1=print_(f1)
@func_arg("haha")
def f1():
    print("---f1---")
@func_arg("heihei")
def f2():
    print("---f2---")
f1()
f2()
