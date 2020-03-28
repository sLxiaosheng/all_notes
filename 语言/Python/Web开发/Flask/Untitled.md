# Flask

>   Flask是一个使用 [Python](https://baike.baidu.com/item/Python) 编写的轻量级 Web 应用框架。
>
>   微框架中的“微”是指Flask旨在保持代码简洁且易于扩展，Flask框架的主要特征是核心构成比较简单，但具有很强的扩展性和兼容性，程序员可以使用Python语言快速实现一个网站或Web服务
>
>   https://dormousehole.readthedocs.io/en/latest/index.html

**关于flask的虚拟环境在C:\Users\DELL\myproject\中**

通过命令行   venv\scripts\activate   来激活



```python
from flask import Flask
#app = Flask(文件所在的包)
app = Flask(__name__)

#/代表根目录，当用户访问时，执行函数hello_world
@app.route('/')
def hello_world():
   return 'Hello World'

if __name__ == '__main__':
   app.run()

#运行后，输出为
Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
在浏览器中打开上述URL（localhost：5000）。

将显示“Hello World”消息。
```





Flask类的**route()**函数是一个装饰器，它告诉应用程序哪个URL应该调用相关的函数。

```
app.route(rule, options)
```

-   **rule** 参数表示与该函数的URL绑定。
-   **options** 是要转发给基础Rule对象的参数列表。

在上面的示例中，'/ ' URL与**hello_world()**函数绑定。因此，当在浏览器中打开web服务器的主页时，将呈现该函数的输出。

最后，Flask类的**run()**方法在本地开发服务器上运行应用程序。

```
app.run(host, port, debug, options)
```

所有参数都是可选的

| 序号 | 参数与描述                                                   |
| ---- | ------------------------------------------------------------ |
| 1    | **host** 要监听的主机名。 默认为127.0.0.1（localhost）。设置为“0.0.0.0”以使服务器在外部可用 |
| 2    | **port** 默认值为5000                                        |
| 3    | **debug** 默认为false。 如果设置为true，则提供调试信息       |
| 4    | **options** 要转发到底层的Werkzeug服务器。                   |



### 调试模式？

通过调用**run()**方法启动**Flask**应用程序。但是，当应用程序正在开发中时，应该为代码中的每个更改手动重新启动它。为避免这种不便，请启用**调试支持**。如果代码更改，服务器将自行重新加载。它还将提供一个有用的调试器来跟踪应用程序中的错误（如果有的话）。

在运行或将调试参数传递给**run()**方法之前，通过将**application**对象的**debug**属性设置为**True**来启用**Debug模式**。

```python
app.debug = True
app.run()
app.run(debug = True)
```



### Flask 路由

现代Web框架使用路由技术来帮助用户记住应用程序URL。可以直接访问所需的页面，而无需从主页导航。

Flask中的**route()**装饰器用于将URL绑定到函数。例如：

```python
@app.route(‘/hello’)
def hello_world():
   return ‘hello world’
```

在这里，URL **'/ hello'** 规则绑定到**hello_world()**函数。 因此，如果用户访问**http：// localhost：5000 / hello** URL，**hello_world()**函数的输出将在浏览器中呈现。

application对象的**add_url_rule()**函数也可用于将URL与函数绑定，如上例所示，使用**route()**。

装饰器的目的另一种表示形式：

```python
def hello_world():
   return 'hello world'
app.add_url_rule('/', 'hello', hello_world)
```



### Flask 变量规则



通过向规则参数添加变量部分，可以动态构建URL。此变量部分标记为<variable-name>。它作为关键字参数传递给与规则相关联的函数。

在以下示例中，**route()**装饰器的规则参数包含附加到URL **'/hello'**的<name>。**因此，如果在浏览器中输入**http://localhost:5000/hello/w3cschool**作为**URL**，则**'w3cschool'**将作为参数提供给**hello()函数。

```python
from flask import Flask
app = Flask(__name__)

@app.route('/hello/<name>')
def hello_name(name):
   return 'Hello %s!' % name

if __name__ == '__main__':
   app.run(debug = True)
```

将上述脚本保存为**hello.py**并从Python shell运行它。接下来，打开浏览器并输入URL **http:// localhost:5000/hello/w3cschool。

以下输出将显示在浏览器中:

```
Hello w3cschool!
```

除了默认字符串变量部分之外，还可以使用以下转换器构建规则：

| 序号 | 转换器和描述                      |
| ---- | --------------------------------- |
| 1    | **int**接受整数                   |
| 2    | **float**对于浮点值               |
| 3    | **path **接受用作目录分隔符的斜杠 |

在下面的代码中，使用了所有这些构造函数：

```python
from flask import Flask
app = Flask(__name__)

@app.route('/blog/<int:postID>')
def show_blog(postID):
   return 'Blog Number %d' % postID

@app.route('/rev/<float:revNo>')
def revision(revNo):
   return 'Revision Number %f' % revNo

if __name__ == '__main__':
   app.run()
#运行后，输出为
Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
在浏览器中打开上述URL（localhost：5000）。
因为@app.route('/blog/<int:postID>')@app.route('/rev/<float:revNo>')
两个函数都需要输入，需要在http://127.0.0.1:5000/后面加上/blog/一个int型数据来执行show_blog函数显示对应页面，加上/rev/一个float型数据来执行revision函数显示对应页面
将显示“Hello World”消息。
```

从Python Shell运行上面的代码。访问浏览器中的URL **http://localhost:5000/blog/11**。

给定的数字用作**show_blog()**函数的参数。

浏览器显示以下输出：

```python
Blog Number 11
```

在浏览器中输入此URL - **http://localhost:5000/rev/1.1**

**revision()**函数将浮点数作为参数。

以下结果显示在浏览器窗口中：

```python
Revision Number 1.100000
```

Flask的URL规则基于**Werkzeug**的路由模块。这确保形成的URL是唯一的，并且基于Apache规定的先例。

考虑以下脚本中定义的规则：

```python
from flask import Flask
app = Flask(__name__)

@app.route('/flask')
def hello_flask():
   return 'Hello Flask'

@app.route('/python/')
def hello_python():
   return 'Hello Python'

if __name__ == '__main__':
   app.run()
```

这两个规则看起来类似，但在第二个规则中，使用斜杠**（/）**。因此，它成为一个规范的URL。因此，使用 **/python** 或 **/python/**返回相同的输出。但是，如果是第一个规则，**/flask/ URL**会产生“404 Not Found”页面。