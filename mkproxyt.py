import re

fp = open('proxy.html','r',encoding='utf-8')
proxyfile = open('proxy.txt','a')

lines = fp.readlines()
port_flag = 0
for line in lines:
    if port_flag == 0:
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
            proxyfile.write(proxy+'\n')
        


