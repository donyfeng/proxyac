import re
import os

proxylist = []
port_flag = 0
ip = ''
htmlfn = 'proxy.html'

def ParseProxy(line):
    global port_flag
    global ip

    if not port_flag:
        ip = re.findall(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}',line)
        if ip:
            ip = ip[0]
            port_flag = 1
    else: 
        port_flag = 0
        port = re.findall(r'\d+',line)
        if port:
            port = port[0]
            proxy = ip+':'+port
            proxylist.append(proxy)

if __name__ == '__main__':
    proxyhtml = open(htmlfn,'r',encoding='utf-8')
    proxys = []
    if os.path.isfile('proxy.txt'):
        proxytxt  = open('proxy.txt','r')
        proxys = proxytxt.readlines()
        for i in range(len(proxys)):
            proxys[i] = proxys[i].strip('\n')
    
    proxytxt = open('proxy.txt','a')
    
    new_num = 0
    same_num = 0
    for line in proxyhtml.readlines():
        ParseProxy(line)
    for proxy in proxylist:
        if proxy in proxys:
            same_num += 1
        else:
            proxytxt.write(proxy+'\n')
            new_num += 1
    print(str(same_num)+' proxys are the same!')                    
    print(str(new_num)+' proxys added!')
    
