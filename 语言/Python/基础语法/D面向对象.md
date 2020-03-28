# 面向对象

>   将现实中的事物映射到程序中，以事物为依据编程
>
>   在计算机中的映射（行为， 特征）   像模版一样 （对象则是一个个有主题的成品）

-   变量的作用域，全局变量，局部变量

-   在函数，类，循环中定义的变量作用于逻辑内部，

-   python语法中，是将变量名作为标签贴在变量上（与C语言不同）

    ```python
    c = 50      #全局变量， 作用域为 整个模块，若被引用，可作用域整个包
    
    def plus(x,y):
        c = x + y           # 局部变量, 为函数中定义的变量，在函数外可被引用
        print(c)
    
    plus(1,2)
    print(c)                # 函数内部定义的变量只作用与函数内部
    
    print('~~~~~~~例子~~~~~~~')
    
    def demo():
        a = 10
    #print(a)                #会 显示为 a 未被定义
    ```



-   两者转换

    ```python
    def demo():
        global c        # global  定义一个全局变量，  可被引用 
        c = 2
    
    demo()          
    print(c)        # 先调用函数，再输出
    ```

## 类

>   每个类对应每个对象，下面有类变量
>
>   起到封装变量，封装函数，代码的作用

-   定义一个类

    ```python
    class Student():               #命名，首字母大写
        name = '名字'
        age = 0
    
        def __init__(self):
            #构造函数, 无需调用直接运行      在给对象的赋值语句中即可运行
            print('先运行构造函数')
            return None     #只能返回none 不可人为指定
        
        def grape(self,score):
            print("该学生的成绩是" + str(score))
    ```


-   实例化类，给类赋值

    ```python
    student = Student()              #实例化
    student.grape(100)             #调用
    ```

-   调用构造函数时，通过 在类后面（）的方式调用

-   调用实例方法时，通过对象调用

    ```python
    class School():               #命名，首字母大写
        name = '未定义'                 
        age = 0                   
    
        def __init__(self,name1,age1):             
        #可在（）内，  加变量    在引用时，定义变量的值
        #在构造函数中， 初始化对象的属性  （此函数中初始化 name age）
            
            name = name1
            print(name)                   
            age =  age1                   
            return None     #只能返回none 不可人为指定
    
    #调用构造函数时，通过  在类后面（）的方式调用
    #调用实例方法时，通过对象调用
    School1 = School(name1 = '中华小学',age1 = '80')
    School2 = School(name1 = '安徽小学',age1 = '70')
    print(School1.name)                         #此时打印出结果为初始值   
    #这里出错原因与前面的 局部变量   全局变量 概念不同
    #这里是  类变量   实例变量   的区别
    ```

-   类中函数的实例变量与实参不同

    ```python
    def __init__(self,name1,age1):             
            #可在（）内，  加变量    在引用时，定义变量的值
            #通过 self 来保存特征值
            self.name = name1              
            #通过 self 来定义实例变量和访问实例变量
            self.age =  age1       
            #self.变量属性 = 变量名（形参）
    ```

-   关于self

    >   实例方法中出现 self
    >
    >   self不是关键字
    >
    >   与对象有关，与类无关 代表的是一个对象 如 school1 = School()  self 代表  school1  这个对象
    >
    >   在类下的函数（方法）为实例方法， 在后面（）里固定显示有一个变量 self （内置参数）不需要传值
    >
    >   在函数内部，定义实例变量      
    >
    >   self的名字不唯一  可为其他名字（this）
    >
    >   实例方法 与 对象 关联 
    >
    >   类方法  与 类本身 关联

-   一个例子

    ```python
    class School():               #命名，首字母大写
        name = '未定义'                 
        age = 0          
        sum = 0                    # 与类相关的变量
        color = 'yellow'
        squire = '面积'
    
        def __init__(self,name1,age1,color1,squire1):            
            
            name = name1                    
            age =  age1     
            self.color = color1
            self.squire = squire1
            return None     
    
    School1 = School(name1 = '中华小学',age1 = '80',color1 = 'blue',squire1 = '1000')
    print(School1.name,'    ', School1.age)     #此时打印出了 类变量 (先在  实例变量  中查找，无， 则到类变量中找)
    print(School1.__dict__)                     #以字典的形式输出 School1 的变量
    print(School.name)     
    print(School1.color,'    ', School1.squire) 
    print(School.__dict__)   
    ```


## 实例方法

```python
def plus_sum(cls):
    pass
```

### 类方法

```
#类方法     基本格式
@classmethod            #为装饰器
def plus_sum(cls):      #cls  为class 的缩写
    pass
```

-   一个例子

```python
class classroom:
sum = 0
    age = 0
    def __init__(self,name,age):
        self.__class__.sum += 1
        self.age = age
        self.__class__.age += self.age
        age = self.__class__.age/self.__class__.sum
        print('当前班级学生总人数为:' + str(self.__class__.sum))
        print('当前班级的平均年龄为:' + str(age))

    # 定义一个    类方法
    @classmethod            #为装饰器
    def plus_sum(cls):      #cls  为class 的缩写   名字不唯一   也可为 self
        cls.sum += 1
        print(cls.sum)
        print('班级总人数为: ' + str(cls.sum - 1))

classroom.student1 = classroom(name = '憨批', age = 10)
classroom.student2 = classroom(name = '小逗比', age = 9)  
classroom.student3 = classroom(name = '土豆',age = 8)           
classroom.plus_sum()                # 通过类来调用 方法
classroom.student1.plus_sum()       # 通过对象来调用方法
```

## 静态方法          

-   用的不多   与类 实例方法 关联不大   与普通函数区别不大  

```python
@staticmethod       # 装饰器
def add(x,y):
    print('This is a static method')
class Company:
    sum = 0
    bass_name = '刘大钞'
    def __init__(self,staff_a,staff_b,staff_c):
        self.staff_a = staff_a
        self.staff_b = staff_b
        self.staff_c = staff_c
        Company.sum = staff_a + staff_b + staff_c
    
    @staticmethod                   # 装饰器
    def add(x,y):                       # 与类方法实例方法不同，（）内无需强制添加变量
        print('This is a method')
        print(Company.bass_name)        #  正常引用类变量
        print(x + y)                #引用形参
        print(self.staff_a)             #报错
        print(staff_a)                  #报错
    
    Company1 = Company(staff_a = 10,staff_b = 20,staff_c = 30)
    Company1.add(1,2)
    Company.add(1,2)                #可正常被调用

```