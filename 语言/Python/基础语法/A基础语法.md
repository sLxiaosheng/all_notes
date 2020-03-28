

# python基础语法

## 1.基本数据类型

Python中的数据类型可以分为五大类：字符串、数字、容器、布尔、None。

### 字符串：

可以使用单引号或双引号创建字符串，可以用加号将两个字符串合并。

```python3
name = '小明'
age = '9岁'
print('合并字符串:', name + age)
```

格式化字符串：%s

```python3
a = "I'm %s." % ('xiaoming')
print(a)
```

### 数字：整型、浮点型和复数。

- 整型：正整数或负整数

```text
number1 = 12        number2 = -3
```

- 浮点型：由整数部分和小数部分组成

```text
score = 96.5
```

- 复数：由实数部分和虚数部分组成

3)容器：List(列表)、Tuple(元组)、Sets(集合)、Dictionary(字典)

- List(列表)

创建一个列表，只要把逗号分隔的不同的数据项使用方括号括起来即可。列表可以修改，可以用于切片、增、删、改、查。

```python3
#创建列表
list1 = ['a', 'b', 'c', 'd', 'e']
print(list1)
```



```python3
#列表切片
#格式：【start:end:step】
#start:起始索引，从0开始，-1表示结束#end：结束索引
#step：步长，end-start，步长为正时，从左向右取值。步长为负时，反向取值
#注意切片的结果不包含结束索引，即不包含最后的一位，-1代表列表的最后一个位置索引

a=[1,2,3,4,5,6]
b=a[0:5:3] 
print(b)
```

```python3
#列表删除
del a[-1]
print(a)
```



```text
#列表修改
print("未修改之前第一个元素为：",a[0])
a[0] = '66'
print("修改之后第一个元素为：",a[0])
```



```text
#列表查询
a1 = a[0]
print("查询出列表第一个元素为：", a1)
```



- Tuple(元组)

元组和列表类似，但是不同的是元组不能修改，元组使用小括号。

```python3
#创建元组
tup = (1, 2, 3, 4, 5)
print(tup)
```



元组中只包含一个元素时，需要在元素后面添加逗号，否则括号会被当作运算符使用。

```python3
#查询元组,下标索引从0开始
print("查询出列表第一个元素为：", tup[0])
```



元组中的元素值是不允许修改的，但可以对元组进行连接组合。

```python3
tup1 = (23, 78);
tup2 = ('ab', 'cd')
tup3 = tup1 + tup2
print (tup3)
```



- Sets(集合)

Set是无序的集合，不能有重复的元素，也不能排序。

```text
#创建集合
s1 = set(['A','B','C','D'])
print(s1)
```



```text
#增加元素:update
s1.update(['E'])
print(s1)
```



```text
#删除元素:discard
s1.discard('E')
print(s1)
```



```text
#修改元素：先删除，后增加
s1.discard('D')
s1.update(['D'])
print(s1)
```



```text
#查询元素
ss = 'B' in s1
print(ss)
```



- Dictionary(字典)

字典是另一种可变容器模型，且可存储任意类型对象。

字典的格式如下所示：d = {key1 : value1, key2 : value2 }

键必须是唯一的，但值则不必。值可以取任何数据类型，但键必须是不可变的，如字符串，数字或元组。

```text
#创建字典
d = {'01': 'xiaoming', '02': 'xiaohong', '03': 'xiaowang'}
print(d)
```



```text
#增加
d['04'] = 'xiangfang'
print(d)
```



```text
#删除
del d['04']
print(d)
```



```text
#修改
print("修改之前：",d['01'])
d['01'] = 'xiaolin'
print("修改之后：",d['01'])
```



```text
#查询
d1 = d['01']
print(d1)
```



4)布尔：True、False

主要应用在条件判断上面，发生即为True，未发生即为False。Python严格区分大小写，所以一定要注意不要写错。

5)None：Python里面特殊的空值，不能理解为0。

2.条件判断

if语句用来检验一个条件， 如果条件为真，我们运行一块语句（称为 if-块 ）， 否则我们处理另外一块语句（称为 else-块 ）。 else 从句是可选的。

![img](https://pic2.zhimg.com/80/v2-0ebd545a204d7869a95b0c6b634944dd_hd.jpg)

```text
a = 25
if a >= 20:
    print("Yes")
else:
    print ("No")
```



elif 语句

elif语句可以检查多个表达式的真值，并执行一个代码块的条件之一计算结果为true。

if...elif 语句是可选的。然而不像else，对此可以有最多一个语句，if语句下边可以有任意数量elif语句。

```text
x = "上海"
if x == "上海":
    print ("大")
elif x == "北京":
    print ("特别大")
else:
    print("无")
```



3.循环语句

Python中的循环语句有 for 和 while。Python循环语句的控制结构图如下：

![img](https://pic3.zhimg.com/80/v2-3becccd68c1974fa9d52d549456512f6_hd.jpg)

for循环可以遍历任何序列的项目：

```text
x = list(["小明","小红","小张","小李"])
for b in x:
    print (b)
```



while循环，只要条件满足，就不断循环，条件不满足时退出循环：

```text
sum = 0
n = 99
while n > 0:
    sum = sum + n
    n = n - 2
print(sum)
```



break和continue语句：

break可以用来终止当前的循环语句，即使循环没结束，执行了break语句这个循环就终止了，直接跳出整个循环。

```text
for i in range(10):
    print(i)
    if i == 8:
        break
print('end')
```



continue语句是用来告诉程序跳出本次循环，然后执行下一轮循环，不同与break，break是跳出整个循环，continue是结束这一次循环，继续下一次循环。

```text
for i in range(10):
    if i == 6:
        print('good')
        continue
    print(i)    
print('end')
```



4.函数

函数是组织好的，可重复使用的，用来实现单一，或相关联功能的代码段。

在Python中，定义一个函数要使用 def 语句，依次写出函数名、括号、括号中的参数和冒号 : ，然后，在缩进块中编写函数体，函数的返回值用 return 语句返回。

```text
def threeNumAdd(x,y,z):
    numSum = x + y + z
    return numSum

a = threeNumAdd(10,20,30)
print(a)
```



- 函数参数：不可变数据类型，如 整数、字符串、元组。

```text
def ChangeInt(a):
    a = 10
b = 2
ChangeInt(b)
print(b)
```



- 函数参数：可变数据类型，如 列表，字典。

```text
def changelist(alist):
    alist.append([1, 2]);

blist = ['10', '20']
print('调用函数之前的值：', blist)
changelist(alist = blist)
print('调用函数之后的值：', blist)
```



- 变量作用域

一般在函数体外定义的变量成为全局变量，在函数内部定义的变量称为局部变量。

全局变量所有作用域都可读，局部变量只能在本函数可读。

函数在读取变量时，优先读取函数本身自有的局部变量，再去读全局变量。

```python
name = 'Tim' #全局变量

def f1():
    age = 18 #局部变量
    print(age,name)
    
def f2():
    age = 19 #局部变量
    print(age,name)
    
f1()
f2()
```



5.模块

- 模块引入

```python3
#import 语句,用于导入整个模块
import math

#from-import 语句,常用于只导入指定模块的部分属性或模糊导入：
#from 模块名 import 函数名1,函数名2....
from random import choice,random
```

6.数据结构

1)队列

```text
from  collections import deque
#定义队列：排队吃饭人的编号
queue = deque(['001','002','003','004','005'])
#入队：在队列尾部插入元素
queue.append('006')
print(queue)
#出队：在队列头部删除元素
queue.popleft()
print(queue)
```



2)栈

```text
#定义栈：浏览个人知乎主页的顺序
stack = deque(['知乎动态','知乎回答','知乎文章'])
#入栈：在栈顶加入元素
stack.appendleft('知乎专栏')
print(stack)
#出栈
stack.pop()
print(stack)
```



3)排序字典

- Python默认的字典（key无序）

```python3
#6家公司名称及股票代码
gafatadict = {'腾讯':'HK:00700', '阿里巴巴':'baba', '苹果':'Apple', 
                  '谷歌':'GOOGLE', 'Facebook':'fb', '亚马逊':'amzn'}
gafatadict
```



- Collection中的排序字典（key有序）

```python3
from collections import OrderedDict
#定义有序字典
gafataodDict=OrderedDict({'腾讯':'HK:00700', '阿里巴巴':'baba', '苹果':'Apple', 
                  '谷歌':'GOOGLE', 'Facebook':'fb', '亚马逊':'amzn'})
gafataodDict
OrderedDict([('腾讯', 'HK:00700'),
             ('阿里巴巴', 'baba'),
             ('苹果', 'Apple'),
             ('谷歌', ':GOOGLE'),
             ('Facebook', 'fb'),
             ('亚马逊', 'amzn')])
```

4)计数器

```text
from collections import Counter
cdict = Counter('好好学习，天天向上')
cdict
#出现次数最多的2个词
cdict.most_common(2)
```