'''
def 函数名(参数1，参数2...)
 """文本描述"""
 函数体
 return 值
'''

# 形式一无参函数
# def func():
#     print('hhhh')
#     print('hhhh')
#     print('hhhh')

#定义函数发生的事情
# 1.申请内存空间保存函数体代码
# 2.将上述内存地址绑定函数名
# 3.定义函数不会执行函数体代码，但会检测函数体语法

#调用函数发生的事情
# 1.通过函数名找到函数内存地址
# 2.然后通过括号就是在出发函数体代码的执行
# func()

#示范1
# x=22222
# def foo():
#     print(x)
#     print('hhhhh')
# foo()

#示范2
# def bar():#bar=函数的内存地址
#     print('bar')
# def foo():
#     bar()
#     print('foo')
# foo()


# 形式2有参函数

# def fun(x,y): x=1,y=2
#     print(x,y)
# fun(1,2)

# 形式3空函数--函数体代码为pass
# def func(x,y):
#     pass

# 三种定义方式各用在何处
# 1.无参函数的应用场景
# def xinxi():
#     name=input('usname:>>>')
#     age=input('age:>>>>')
#     mas='姓名：{}年龄：{}'.format(name,age)
# xinxi()
# 2.有参函数的应用场景
# def add(x,y):
#     res=x+y
#     print(res)
# add(2,3)

# 1.空参函数的应用场景-----构思函数
def ls():
    pass

# 二调用函数
# 1.语句的方式
# def()
# def(1,2)
# 2.表达式形式
def add(x,y):#参数-》原材料
    res=x+y
    return res#返回值-》产品
#赋值表达式
res=add(1,2)
print(res)
#数学表达式
res=add(1,2)*10
print(res)#30
#函数调用可以当参数
res=add(add(1,2),10)
print(res)#13


# 三.函数返回值
#return是函数结束的标志，即函数代码一旦运行到return会立刻终止函数的巡行，
# 并且会将return后的值当做本次巡行的结果返回
# 1.返回None：函数体内没有return(return return None)
# 2.返回一个值：return 值
def func():
    return 10
res=func()
print(res)
# 3.返回多个值

def func():
   return 10,'aaa',[1,3]
res=func()
print(res,type(res))



def dunc(x,y):
    print('xxxxxxxx')
