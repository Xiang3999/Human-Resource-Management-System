# Human-Resource-Management-System
## 一、实验目标

- 掌握数据库应用程序开发步骤
- 掌握数据库驱动加载方法
- 掌握连接数据库的方法
- 掌握SQL执行的方法
- 掌握结果集处理的方法

## 二、基础知识

### 数据库应用 程序开发步骤

- 数据库应用 程序开发步骤
  - 加载驱动
  - 连接数据库
  - 执行SQL语句
  - 处理结果集
  - 关闭连接

![image-20200421185513955](https://picgo-w.oss-cn-chengdu.aliyuncs.com/img/image-20200421185513955.png)

### web原理

- web原理

  - 访问网站的过程：
    用户向web服务器发送请求，然后返回一个HTML文件。
    静态网站：
    				直接返回HTML文件给用户。
    动态网站：
    				用户请求->执行Python程序(与数据库进行交互)->执行结果->返回HTML给用户。

  - 采用mvc设计web应用：

    - m: model模型，存储web应用数据的代码
    - v: view视图，格式化和显示web应用的用户界面的代码
    - c: controller控制器，将web应用粘合在一起并提供业务逻辑的代码。

  - CGI：common gateway interface

    - 可以让一个客户端，从网页浏览器向服务器请求数据。这是描述客户端和服务器程序之间传输数据的一个标准。

    - 应用于web的编程语言：
      - PHP
      - ASP/ASP.net
      - JSP
      - Python

  - web应用的结构

    - web应用结构概览：
      - 前端程序：HTML、CSS、js（混合使用）
      - 后台程序：Python、PHP、JSP（只有一种就可以）
      - 数据库：MySQL（关系型数据库）、mongodb（非关系型数据库）。

    - 前端：
      - HTML  超文本标记语言，不是被执行，而是被渲染
      - CSS 层叠样式表，规定样式
      - js  和JAVA并没有联系。

    - 数据库及静态存储：
      - MySQL
      - sqlite
      - Gaussdb。

    ### 

## 三、实验任务——人力资源管理系统

### 设计人力资源管理系统

- 修改表staffs，增加一列password，并设置数据
- 设置三个角色
  - 员工 staff
  - 部门经理 manager
  - 人事经理 hr_manager

1. 员工具备以下功能
       1）输入staff_id  和 正确的密码，进入员工主页面；
       2）在员工主页面，可以选择查看员工自己基本信息；
       3）在员工主页面，修改员工自己的电话号码；

2. 部门经理具备以下功能
       1）输入staff_id  和 正确的密码，进入部门经理主页面；
       2）在部门经理主页面，可以查看本部门所有员工基本信息（选择按员工编号升序排列，或者按工资降序排列）；
       3）在部门经理主页面，可以按员工编号查询员工基本信息；
       4）在部门经理主页面，可以按员工姓名查询员工基本信息；
       5）在部门经理主页面，可以统计查询本部门员工最高工资，最低工资以及平均工资；

3. 人事经理具备以下功能
       1）输入特定编号hr001  和 特定密码，进入人事经理主页面；
       2）在人事经理主页面，可以查看所有员工基本信息（选择按员工编号升序排列，或者按工资降序排列）；
       3）在人事经理主页面，可以按员工编号查询员工基本信息；
       4）在人事经理主页面，可以按员工姓名查询员工基本信息；
       5）在人事经理主页面，可以统计各部门员工最高工资，最低工资以及平均工资；
       6）在人事经理主页面，可以查询各部门基本信息，并可以根据部门编号修改部门名称；
       7）在人事经理主页面，可以查询各工作地点基本信息，并可以增加新的工作地点；
       8）在人事经理主页面，可以按员工编号查询员工工作信息，包括其历史工作信息，返回员工编号，职位编号和部门编号；

## 四、项目设计

```PYTHON 
______________________________________________
|---》前端(html+css+js)
|  |---》登陆界面——》Day5_0501
|  |---》功能界面——》Day6_0507
|---》后端(python+gaussdb)
|  |---》连接数据库——》DAY 1_0421
|  |---》设计SQL语言——》Day2_0423
|  |---》web后端设计——》Day3_0424、Day4_0430
|  |---》各个功能实现——》Day2_0423
—————————————————————————————————————————————
 ############################################
 ##########     文    件    树     ###########
 ##########  源 码  见  压  缩  包  ###########
 ############################################
—————————————————————————————————————————————
├── __init__.py
├── libzeclient.so#API
├── pyzenith.so#API
├── templates#HTML文件  各个功能界面
│      ├── hr_index.html
│      ├── hr_places.html
│      ├── hr_query.html
│      ├── hr_resection.html
│      ├── hr_staffs.html
│      ├── login.html
│      ├── man_index.html
│      ├── man_salary.html
│      ├── man_section.html
│      ├── phone.html
│      ├── pwd.html
│      ├── salary.html
│      ├── section.html
│      ├── staff_index.html
│      └── staff_inf.html
└── web001.py# 主程序
————————————————————————————————————————————————
```

### DAY 1_0421

```python
/*
实现连接数据库与简单的处理
   --》只能在Linux系统上连接？
   --》可以实现连接与简单处理
*/
#import module
import pyzenith
#db info
host='127.0.0.1'
username='PAO'
password='Gauss147258'
port='1888'
#connect db
conn=pyzenith.connect(host,username,password,port)
#open cursor
c=conn.cursor()
#execute sql
c.execute("select * from EMPLOYMENTS")
#fetch data
row =c.fetchall()
#print data
print(row)
#close cursor
c.close()
#close db connect
conn.close()
```

#### 问题： 

1. 怎么区分各个人员的权限？

2. 怎么实现登陆？

   **这里是使用关键字来实现的，先验证账户是否存在，在验证密码是否正确，然后根据账号(即staff_id)来判断该用户的身份，如果是203号就返回HR的关键字然后有权限进入HR的页面，其他同理。**

   <table><tr>
   <td><img src=https://picgo-w.oss-cn-chengdu.aliyuncs.com/img/image-20200422000450773.png border=0></td>
   <td><img src=https://picgo-w.oss-cn-chengdu.aliyuncs.com/img/image-20200423113012688.png border=0></td>
   </tr></table>

### Day2_0423

通过==command=Check_password(User_id,password)==得到命令后然后使用if语句进行判断，进入相应界面

```python
if command=="STAFF":
    Staff_page(User_id)
elif command=="MAN":
    Man_page(User_id)
elif command=="HR":
    Hr_page()
else:
    print("end")
```

下面是各个功能页面的函数，即SQL语法

```python
def Staff_page(user_id):
    a="x"
    while(a!="exit"):
        a=input("Please your command(a:show information b:Edit phone number exit:exit):")
        if a=="a":
            staff='''
            select * from staffs where staff_id='%d'
            '''%user_id
            c.execute(staff)
            inf=c.fetchall()
            print(inf)
        elif a=="b":
            new_number=input("Please your new phone number:")
            edit='''
            update staffs set staffs.phone_number='%s'
            '''%new_number
            c.execute(edit)
            print("Edit succeed !")
        else:
            continue

def Man_page(user_id):
    a="x"
    section='''
    select section_id from staffs where staff_id='%d'
    '''%user_id
    c.execute(section)
    section_id=int(c.fetchall()[0][0])
    while(a!="exit"):
        a=input("Please your command(a:Show this section's staffs b:query by id c:query by first-name d:show salary exit:exit):")
        if a=="a":
            Man1='''
            select * from staffs where section_id='%d' order by staff_id
            '''%section_id
            c.execute(Man1)
            inf1=c.fetchall()
            print(inf1)
        elif a=="b":
            staff_id=int(input("Please input staff id:"))
            Man2='''
            select * from staffs where staff_id='%d'
            '''%staff_id
            c.execute(Man2)
            inf2=c.fetchall()
            print(inf2)
        elif a=="c":
            staff_name=input("Please input staff's first-name:")
            Man3='''
            select * from staffs where first_name='%s'
            '''%staff_name 
            c.execute(Man3)
            inf3=c.fetchall()
            print(inf3)
        elif a=="d":
            Man4='''
            select max(salary),min(salary),avg(salary) from staffs where section_id='%d'
            '''%section_id
            c.execute(Man4)
            inf4=c.fetchall()
            print("max min avg:")
            print(inf4)
        else:
            continue

def Hr_page():
    a="X"
    while(a!="exit"):
        a=input("a:Show all  b:Query by ID c:Query by name d:max-min-avg e:show section inf f: rename section g:area inf query inf by ID ")
        if a=="a":
            hr1='''
            select * from staffs order by staff_id
            '''
            c.execute(hr1)
            inf1=c.fetchall()
            print(inf1)
        elif a=="b":
            staff_id=int(input("input staff_id:"))
            hr2='''
            select * from staffs where staff_id='%d' 
            '''%staff_id
            c.execute(hr2)
            inf2=c.fetchall()
            print(inf2)
        elif a=="c":
            first_name=input("input first name:")
            hr3='''
            select * from staffs where first_name='%s'
            '''%first_name
            c.execute(hr3)
            inf3=c.fetchall()
            print(inf3)
        elif a=="d":
            hr4='''
            select section_id,max(salary),min(salary),avg(salary) from staffs group by  section_id
            '''
            c.execute(hr4)
            inf4=c.fetchall()
            print(inf4)
        elif a=="e":
            hr5='''
            select * from sections 
            '''
            c.execute(hr5)
            inf5=c.fetchall()
            print(inf5)
        elif a=="f":
            section_id=int(input("input rename section-id:"))
            new_name=input("input new name:")
            hr6='''
            update sections set sections.section_name={} where section_id={} 
            '''.format(new_name,section_id)
            hr66='''
            update sections set sections.section_name=%s where section_id=20
            '''%new_name
            c.execute(hr66)
            print("succeed!")
        elif a=="g":
            hr7='''
            select * from places 
            '''
            c.execute()
            inf7=c.fetchall()
            print(inf7)
        else:
            continue
```

#### 问题：![image-20200423232855434](https://picgo-w.oss-cn-chengdu.aliyuncs.com/img/image-20200423232855434.png) 



> 这里是因为Python**数据库传递参数出现的错误**；
>
> 我尝试了如下的方法：
>
> ```sql
> sql='''
> select %s from stffs where user=%s
> '''(a,b)
> ```
>
> ```sql
> sql='''
> select {} from  user={}
> '''.format(a,b)
> ```
>
> ```sql
> sql'''
> select %s from staffs where user= %s
> '''%[a,b]
> ```
>
> 然后这上面的方法都不可行（猜测可能是gaussdb数据库的原因，API有点问题）
> 想了很久突然想到**字符串拼接**。
> 欣喜若狂，这不是万油精嘛
>
> ```sql
> sql="select"+str(a)+"from staffs where user="+str(b) 
> ```

### Day3_0424

折腾了半天，从寻找python后端库（flask，danjgo,websocket）到确定使用Danjgo（上手比较快，工具比较全，但是是能学到的知识比较少（知乎说的），flask就是从基础做起，比较锻炼人）,然后安装Danjgo是却卡住了，虚拟机上的Centos8出现

```
Failed to download metadata for repo 'epel-modular'
Error: Failed to download metadata for repo 'epel-modular'
```

然后折腾了一个半天也没有解决该问题。。。

但是我突然想到我的目的是安装Danjgo，在改了很多配置之后，居然又可以下载了。**这真的是我上网查资料的一种不好的习惯，特别容易忘记目的是什么，从一个链接跳跃到另外的链接，然后渐行渐远。。。**

![image-20200430000753056](https://picgo-w.oss-cn-chengdu.aliyuncs.com/img/image-20200430000753056.png)

终于成功了！接下来还要接着学习使用Django

### Day4_0430

==先学习了Django ,但是发现这个框架使用的数据库没有Gauss DB的接口，又白折腾了。。。。==

然后又转战Flask，发现有很多模板。链接：https://github.com/FreeCamser/Flask

但是在运行时：libzeclient.so: cannot open shared object file: No such file or directory

![image-20200519161104008](D:\ProgramData\Typora\image-20200519161104008.png)

GaussDB的python包出现问题，我以为是我先折腾Django时把他的依赖包给删除了，就有重装了数据库，结果后面发现是==环境变量的问题==：

```
设置LD_LIBRARY_PATH和PYTHONPATH环境变量
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/home/omm/python_gauss/CLIENT-PYTHON/export PYTHONPATH=/home/omm/python_gauss/CLIENT-PYTHON/
```

然后就恢复了。

总的来说，今天的进展就是最终确定了使用flask框架。但是现在还没有运行一下能否接上数据库。这个问题有点老火。

然后其他的就是前端设计与flask的框架融合了。这里HTML使用的不是html,有一点区别。需要重点学习。

### Day5_0501

三个index界面已经设计好了，接下来就是各个功能实现。

### Day6_0507

零零碎碎的学习了HTML语法，但实现功能的时候还是有一点慢，不是很流畅、高效。

但是终于实现了！！！！！

接下来就是一些收尾工作了，美化界面，使它更加人性化、更用户化。

## 五、界面图片

### 登陆界面

![image-20200513122820937](https://picgo-w.oss-cn-chengdu.aliyuncs.com/img/image-20200513122820937.png)

### HR界面

![image-20200519153749410](https://picgo-w.oss-cn-chengdu.aliyuncs.com/img/image-20200519153749410.png)

![image-20200519153944383](https://picgo-w.oss-cn-chengdu.aliyuncs.com/img/image-20200519153944383.png)

![image-20200519154026287](https://picgo-w.oss-cn-chengdu.aliyuncs.com/img/image-20200519154026287.png)

![image-20200519154159120](https://picgo-w.oss-cn-chengdu.aliyuncs.com/img/image-20200519154159120.png)

![image-20200519154309778](https://picgo-w.oss-cn-chengdu.aliyuncs.com/img/image-20200519154309778.png)

![image-20200519154454149](https://picgo-w.oss-cn-chengdu.aliyuncs.com/img/image-20200519154454149.png)

### 员工界面

![image-20200519155357255](https://picgo-w.oss-cn-chengdu.aliyuncs.com/img/image-20200519155357255.png)

![image-20200519155416363](https://picgo-w.oss-cn-chengdu.aliyuncs.com/img/image-20200519155416363.png)

![image-20200519155450967](https://picgo-w.oss-cn-chengdu.aliyuncs.com/img/image-20200519155450967.png)

![image-20200519155534343](https://picgo-w.oss-cn-chengdu.aliyuncs.com/img/image-20200519155534343.png)

![image-20200519155559545](https://picgo-w.oss-cn-chengdu.aliyuncs.com/img/image-20200519155559545.png)

### 部门老总

![image-20200519155659140](https://picgo-w.oss-cn-chengdu.aliyuncs.com/img/image-20200519155659140.png)

![image-20200519155719358](https://picgo-w.oss-cn-chengdu.aliyuncs.com/img/image-20200519155719358.png)

![image-20200519165426202](https://picgo-w.oss-cn-chengdu.aliyuncs.com/img/image-20200519165426202.png)
