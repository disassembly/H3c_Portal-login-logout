# -*- coding: utf-8 -*-  
  
import http.client  
import time  
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
    'Cookie':''  
}  
  
if __name__ == '__main__':  
    try:  
#        os.system('python3 ./NsINodeLogout.py')  
          
        try:  
            configFile = ConfigParser()  
            configFile.read(filenames=os.getcwd() + '/config.ini', encoding='utf-8')  
            username = configFile.get('Account', 'username')  
            pwd = configFile.get('Account', 'password')  
        except:  
            print('加载用户信息错误')  
  
        loginBody = 'userName={0}&userPwd={1}&isQuickAuth=false&language=Chinese&browserFinalUrl=&userip=null'  
        onlineBody = 'language=Chinese&heartbeatCyc=240000&heartBeatTimeoutMaxTime=3&userDevPort=IAG_5000-vlan-02-0000%40vlan&userStatus=99&userip=null&serialNo=15500&basip='  
        requesteaders['Cookie'] = 'JSESSIONID=09AE7BC2BE0862EFE27B78B4322BE362; hello1={0}; hello2=flase; hello3=; hello4='.format(username)  
         
        pwd = base64.encodebytes(pwd.encode(encoding='utf_8', errors='strict'))  
        pwd = pwd.replace('='.encode(encoding='utf_8', errors='strict'), '%3D'.encode(encoding='utf_8', errors='strict'))  
        loginBody = loginBody.format(username, pwd)  
        loginBody = loginBody.replace("b'", "")  
        loginBody = loginBody.replace("\\n'", "")  
          
        while True:  
            conn = http.client.HTTPConnection('192.168.252.251:8080')  
            print(loginBody)
            print(requesteaders)
            #将/portal/pws?t=li改为你的登录地址
            conn.request('POST', '/portal/pws?t=li', loginBody, headers=requesteaders)  
            res = conn.getresponse()  
  
            if res.status == 200:  
                print('发送验证信息成功')  
                data = res.read()  
                if -1 == data.find(b'3032'):  
                    print('登录信息正确')  
                else:  
                    print('请检查登录信息')  
                    break  
            else:  
                print('发送验证信息失败')  
                continue  
              
            conn = http.client.HTTPConnection('192.168.252.251:8080')  
            conn.request('POST', '/portal/pws?t=gpurl', onlineBody, headers=requesteaders)  
            res = conn.getresponse()  
              
            if res.status == 200:  
                print('发送在线信息成功')  
                break
            else:  
                print('发送在线信息失败')  
                continue  
  
           # time.sleep(60)  
    except Exception as e:  
        print('出错啦...请检查网络连接...')
