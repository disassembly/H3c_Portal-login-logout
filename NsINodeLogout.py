# -*- coding: utf-8 -*-  

welcomeInfo = ''''' 
    作者：马冬亮 
    单位：内蒙古科技大学信息工程学院ACM程序设计协会 
    博客：http://blog.csdn.net/MDL13412 
    邮箱：mdl2009@vip.qq.com 
    Q Q：401074567 
    版权所有 (C) 2012 凝霜.保留所有权利. 

    使用方法： 
    修改当前路径下的config.ini文件，将用户名和密码填写至相应字段 
    登录使用NsINodeLogin.py 
    注销使用NsINodeLogout.py 
    在线时请不要关闭本程序 
    '''  

import http.client  
import base64  
import os  
from configparser import ConfigParser  

requesteaders = {  
            'Connection':'keep-alive',  
            'Cache-Control':'max-age=0',  
            'User-Agent':'Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.79 Safari/535.11',  
            'Content-Type':'application/x-www-form-urlencoded',  
            'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',  
            'Accept-Encoding':'gzip,deflate,sdch',  
            'Accept-Language':'zh-CN,zh;q=0.8',  
            'Accept-Charset':'GBK,utf-8;q=0.7,*;q=0.3',  
            'Cookie':'',  
            'referer':'http://192.168.252.251:8080',
            }  

if __name__ == '__main__':  
    try:  
       # print(welcomeInfo)  

        try:  
            configFile = ConfigParser()  
            configFile.read(filenames=os.getcwd() + '/config.ini', encoding='utf-8')  
            username = configFile.get('Account', 'username')  
            pwd = configFile.get('Account', 'password')  
        except:  
            print('加载用户信息错误')  

        logoutBody = 'userName={0}&userPwd={1}&isQuickAuth=false&language=Chinese&browserFinalUrl=&userip=null'
        requesteaders['Cookie'] = 'JSESSIONID=09AE7BC2BE0862EFE27B78B4322BE362; hello1={0}; hello2=true; hello3=; hello4='.format(username)  

        pwd = base64.encodebytes(pwd.encode(encoding='utf_8', errors='strict'))  
        pwd = pwd.replace('='.encode(encoding='utf_8', errors='strict'), '%3D'.encode(encoding='utf_8', errors='strict'))  
        logoutBody = logoutBody.format(username, pwd)  
        logoutBody = logoutBody.replace("b'", "")  
        logoutBody = logoutBody.replace("\\n'", "")  

        while True:  
            conn = http.client.HTTPConnection('192.168.252.251:8080')  
            #将/portal/pws?t=li改为你的登录地址
            conn.request('POST', '/portal/pws?t=lo', logoutBody, headers=requesteaders)  
            res = conn.getresponse()  
            if res.status == 200:  
                print('下线成功')  
            else:  
                print('下线失败')  

            break  
    except Exception as e:  
        print('出错啦...请检查网络连接...')  
