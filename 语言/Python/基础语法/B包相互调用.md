# 包之间的相互调用

## 1.常见的查文件属性方式

```PYTHON
print(__name__)   #路径
print(__file__)     #内存路径
print(__doc__)      #文档的多行注释
print(__package__ )  #所在的包
```

## 2.调用

### 第一种方式

\#文件夹是包（包含_init_.py文件），可包含子包

\#文件是模块

\#class是类

\#代码是函数，变量

\#命名： 命名空间：1junor.a7  1junor.a6  seven.a7

\#        _init_.py文件名为包名1junor

\#同一个包下的模块可相互调用，如

\#调用a4.py下的变量,先引用，再使用,方法一

```python
import f.c2		# import  包.模块
import a4		#import只能引入模块
import f.c2 as m    #用m来代替f.c2  减少代码长度
print(m.e)
```

调用时，直接运行调用文件

已知f.c2为

```python
print(__name__)   #路径
print(__file__)     #内存路径
print(__doc__)      #文档的多行注释
print(__package__)  #所在的包
```

在t.a9 中引用为

```python
import f.c2	
#输出为
f.c2
d:\M\python\1junor\f\c2.py
None
f
```

若在t.a9 中直接运行

```python
print(__name__)   #路径
print(__file__)     #内存路径
print(__doc__)      #文档的多行注释
print(__package__)  #所在的包
#结果为
name:__main__     #在文件中直接运行，系统会将此模块当作入口文件，入口					文件名字为__main__,且不属于任何包
d:/M/python/1junor/a9.py

文档注释

None

#若命令行输入为 python -m a9.py
#可按模块执行，而不是入口文件
```

方法二：

```python
#from 模块 import 变量
from f.c1 import a
print(a)
#调用包的模块，import 包名.模块
#import gao.a as m  
# print(m.a)
#引入模块中指定的变量，在引入模块中加入__all__=['需要引入的变量']
from  b.b1  import *   # *代表引入全部变量
print(a)
print(b)
```

附加：

```python
#包与模块导入是一次性的，不重复
#避免循环导入，两个或多个模块互相导入，导入时，会运行该文件，导致死循环
#同一个包下的不同文件之间可调用
#一次调用多个模块
from a4 import a

#引入多个变量，换行加\,或给变量加括号(a,b,c)
from a4 import a,c,\
d
print(c)
print(d)
#调用__init__文件，直接引用即可,当引用该包下的其他模块时，自动引用__init__下的变量
from f import *    #导入d的全部变量
print(f.a)
#print(c2.e)         #因为f包中的__init__文件给了限制，c2无法导入
#__init__可批量导入，若多个模块需要导入大量相同的模块或库，如t包下的#__init__的三个库
import t
```

```
#__all__问题
from f import *    #当f下的模块无__all__时，导入全部变量
print(f.a)
#若在f的__init__文件中，有__all__ = ['变量名']的形式
# *只可引用__all__中的变量
```



## id问题

```python
ac='LMC'
password='123456'
print('please input account')
user_ac=input()
print('please input password')
user_password=input()
if (ac == user_ac) and (password == user_password) :
    print('success')
else :
     print('fail')
c=id(ac)
d=id(password)
e=id(user_ac)
f=id(user_password)
print(c)
print(d,   e,    f)
#若正确赋值后
please input account
LMC
please input password
123456
#输出结果为
success
2454248703536
2454249408624 2454248606000 2454249410288
#给变量提前赋值，与输入后赋值，id不同，
#python赋值时，是将值作为标签贴到id上

```

代码块，可分层次，同一结构，统一层次为一块代码块（缩进）

## 一些内置函数

### if

```python
a = input()
print(a)
print(type(a))
if a == 1:
    pass
else:
    print('error')
```

\#elif应与if一起使用，避免过多嵌套（与switch类似）也可用字典方式代替switch

```python
a=input()
print('a' is a  )
if a == 1:
    print('apple')
elif a == 2:
    print('orange')
elif a== 3:
    print('banana')
else:
    print('shopping')
#会报错
#错误原因：input()输入的是str，‘1’！= 1
```

小技巧

```python
#返回a,b中的真值
#方法一，可用if,else实现
#更好是用
a=1
b= 0
c= 3
d= 6
#print(a or b)  返回值为就近原则
#or and not 也可看作函数s
```

### while

```python
con = True
ter = 0
while con:
    print('I an while')  #ctrl+c 可终止程序运行
else:
    print('in')
#多应用于递归中
```

### for

```python
#for
#主要用来遍历/循环 序列或者集合，字典
a=[['apple','orange','banana','grape'],(1,2,3)]
for x in a:
    for y in x:
        print(y,end = ',')              #若不进行end操作，则默认为end='\n'
else:
     print('fail')                     #当for 语句遍历完所有元素后，执行else
#break结束循环，continue结束当前循环，进行下个循环
#python中的for(i=0；i<20;i++)
for x in range(0,10):                  #(0,10)中的0为起始数字，10为切片长度
    print(x)
for x in range(0,10,2):
    print(x,end = ' | ')                 #以行的方式打印
for x in range(0,10,-2):                #递减数列的方式
    print(x, end = ' | ')    
#输出为
apple,orange,banana,grape,1,2,3,fail
0
1
2
3
4
5
6
7
8
9
0 | 2 | 4 | 6 | 8 |

#思考：从数组中隔一个一取
a=[1,2,3,4,5,6,7,8]     #方法1
for x in a:
    if x%2:
       continue
    print('\n')
    print(x,end = '')
    #结果
    
2

4

6

8

a =[1,2,3,4,5,6,7,8]			#方法2
for i in range(0,len(a),2): 
    print(a[i],end =' | ')
#结果
1 | 3 | 5 | 7 |

b = a[0:len(a):2]           #方法3
print(b)
c=7
#结果
[1, 3, 5, 7]
```

## 相对导入与绝对导入

```python
#顶级包与main.py的位置有关
#main.py 为入口文件，执行文件
#运行代码
print(__package__)
#此时main.py不属于任何包
import package2.c1
#此时的c1的顶级包是package2,与main.py同级
#绝对路径，绝对引用
#是从顶级包开始的路径，
#相对导入
#. 代表当前目录
#..代表上级目录
#... 代表上上级目录
#通过 . 的数量表示被导入模块与此文件的位置关系，实现相对导入
#在入口文件中不可用相对导入,在相对导入时，使用的是__name__,而入口文件的__name__变为__main__,所以不可
# import 后不可加相对导入
#用 from 进行相对导入
from package2.c1 import a
```

