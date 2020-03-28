# 函数&方法

## 系统函数

```python

a = 1.12386
result = round(a,2)
print(result)
# round函数，（变量，保留小数点后的位数），自动进行四舍五入
result = round(a,3)
print(result)
# print () 中不可出现两种变量，如： print('a'+ 11)

help(round)         #查看round函数功能
#输出
1.12
1.124
Help on built-in function round in module builtins:

round(number, ndigits=None)
    Round a number to a given precision in decimal digits.

    The return value is an integer if ndigits is omitted or None.  Otherwise
    the return value has the same type as the number.  ndigits may be negative.
```

## 自定义函数

```
#函数定义
def funcname(parameter_list):
    pass
#1.参数列表可以没有
#2.用 return 返回值value， 若无return 语句，则返回none; 函数内部遇到 return 则停止运行
```

```python
def add(x,y):
    result = x + y
    return result

#定义函数时，不可与系统函数同名
def print_code(code):
    print(code)
 
```

## 引用函数

```python
#引用函数
add(1,2)
print_code('python') 

a = add(1,2)
b = print_code('python')

print(a,b)
#结果返回为 3,None   因为print_code函数无返回值，所以 结果为None
```

## 函数返回值

```python
def damage(skill1,skill2):
    damage1 = skill1 * 3
    damage2 = skill2 * 2 + 10
    return damage1, damage2

skill1_damage, skill2_damage = damage(3,6)
print(skill1_damage,skill2_damage)
#用明确的变量组来接受函数输出值，便于后期查看（序列解包），不用元组
#结果为
9 22
```

### 序列解包

```python
d = 1,2,3
type(print(d))      #为元组

a,b,c = d           #将d 拆分为三个值，为序列解包（将元组拆开）
#元素个数要相等
a,b = [1,2,3]       #不可解包
```

## 函数的参数

### 必须参数

```python
def add(x,y):
    result = x + y
    return result
#中的 x,y 为必须参数
#形式参数，实际参数，与c语言中类似
```

## 关键字参数

```python
def add(x,y):
    result = x + y
    return result

c = add(y=3,x=2)            #指定赋值，与顺序无关，可读性


def print_files(name,age,gender,collage):
    print('My name is ' + name)
    print('I am ' + age)
    print('My gender is ' + gender)
    print('My school is '+ collage)

print('~~~~~~~~~~~~默认参数~~~~~~~~~~~~~~')
print_files('阿衰',str(18),'man','怕跌中学')
#print_files('阿衰')                     #此时报错

#结果为

~~~~~~~~~~~~默认参数~~~~~~~~~~~~~~
My name is 阿衰
I am 18
My gender is man
My school is 怕跌中学
My name is 阿衰
I am 18
My gender is 男
My school is 人民路小学
```

### 默认参数

默认参数，即在函数定义中给形参赋值

```
def print_files(name,gender = '男',age = 18, collage = '人民路小学'):
    print('My name is ' + name)
    print('I am ' + str(age))
    print('My gender is ' + gender)     
    print('My school is '+ collage)
print_files('阿衰')
print('~~~~~~~~~~~~~~~~~~~~~~~~~~')
print_files('黄小鸭',age = '19', collage = '实验小学')
#在调用函数时，默认参数，关键字参数要在必须参数后面，以免报错

#结果为
~~~~~~~~~~~~~~~~~~~~~~~~~~
My name is 黄小鸭
I am 19
My gender is 男
My school is 实验小学

```

### 可变参数

对于 可变参数， 可不传实参 ， 输出为对应的空类型 空元组 空字典

```python
print('~~~~~~~~~~~~~~~~可变参数~~~~~~~~~~~~~~~~~~~~~~')
def demo(*param):
    
    print(param)
    print(type(param))
    
a = (1,2,3,4,5,6)
demo(*a)                    # *a 的形式将 a 的元素解包出来
demo(*[1,2,3,4])

#结果为
~~~~~~~~~~~~~~~~可变参数~~~~~~~~~~~~~~~~~~~~~~
(1, 2, 3, 4, 5, 6)
<class 'tuple'>
(1, 2, 3, 4)
<class 'tuple'>

#可与其他参数一同赋值,但 可变 放在 必须参数 后面
def demo(param1,*param,param2 = 2):
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print(param1)
    print(param)
    print(param2)

demo('a',1,2,3,param2 = 'param')

# 尽量让 形参 的种类 简化 

#结果为
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
a
(1, 2, 3)
param
```

## 函数的嵌套

```python
def square(*param):
    sum = 0
    for i in param:
        sum += i*i 
    print(sum)
square(1,2,3)
print('~~~~~~~~~~~~~~~~~')
square(*[1,2,3])               #  两种表现形式

#结果为
14
~~~~~~~~~~~~~~~~~
14

```

```python
d = 1

def func1():
    d = 2
    def func2():
        d = 3
        print(d)
    func2()
# 链式，作用域链       就近原则，逐级寻找的过程
func1()

#
3
```



### 形参可输入 任意个数的关键字参数

```python
def city_temp(**param):				#**
    print(param)
    print(type(param))              # 输出为 字典 

city_temp(bj = '32c', London = '42c', NY = '58c')
```

让 字典 中的元素 成对出现

```python
print('~~~~~~~~~成对出现~~~~~~~~~~~')
def city_temp(**param):
    for key,value in param.items():     # .items()   
        print(key,':',value)

a = {'bj' : '32c','sh' : '31c'}
city_temp(**a)

#结果为
{'bj': '32c', 'London': '42c', 'NY': '58c'}
<class 'dict'>

```