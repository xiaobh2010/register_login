from mysqlhelper import MysqlHelper
from hashlib import sha1
from getpass import getpass
import string

mysql=MysqlHelper('db5')

#给字符串进行加密
def update_pwd(passwd):
    s=sha1()
    s.update(passwd.encode())
    passwd=s.hexdigest()
    return passwd

#注册函数
def register():
    while True:
        #接收用户名
        username=input('请输入用户名:')
        #依次把用户名中的每个字符遍历出来做判断
        all_chars=string.punctuation+string.whitespace
        for i in username:
            if i in all_chars:
                print('用户名中不能包含特殊字符')
                break
        #使用标志位也行
        else:
            break

    sel='select username from user where username="%s"'%username
    r=mysql.get_all(sel)
    if r:
        print('用户名已存在')
        return
    else: 
        #用户名可用接受用户输入密码
        passwd=getpass('请输入密码:')
        #查询用户是否已存在
        re_passwd=getpass('请再次输入密码:')
        if passwd==re_passwd:
            #把用户信息存放到user表，并提示注册成功
            #加密
            re_passwd=update_pwd(re_passwd)
            # s=sha1()
            # s.update(re_passwd.encode())
            # re_passwd=s.hexdigest()

            ins='insert into user values ("%s","%s")'%(username,re_passwd)
            mysql.execute_sql(ins)
            print('注册成功')
        else:
            print('密码输入不一致')
            return

#登录函数
def loign():
    while True:
        username=input('请输入用户名:')
        if username=='':
            print('退出登录')
        passwd=getpass('请输入密码:')
        sel='select passwd from user where username="%s"'%username
        r=mysql.get_all(sel)
        if r:
            passwd=update_pwd(passwd)
            # s=sha1()
            # s.update(passwd.encode())
            # passwd=s.hexdigest()

            # print(passwd)
            # print(r[0])
            #fetchall函数的返回值是元祖里面包含元祖
            if passwd==r[0][0]:
                print('登录成功')
                return
            else:
                print('密码输入错误，请重新输入')
        else:
            print('用户名不存在')
#
if __name__=='__main__':
    while True:
        menu='''
(1)注册
(2)登录
(3)退出
请选择(1/2/q)：'''
        choice=input(menu)
        if choice.strip() in ['1','2','q']:
            if choice=='1':
                print('进行注册中...')
                register()
            elif choice=='2':
                print('进行登录中...')
                loign()
                break
            else:
                print('退出菜单')
                break


