import re

proxyhtml = open('proxy.html','r')
try:
    proxytxt  = open('proxy.txt','r')
    proxys = proxytxt.readlines()
    for i in range(len(proxys)):
        proxys[i] = proxys[i].strip('\n')
    print(proxys)

proxytxt = open('proxy.txt','a')

for line in proxyhtml.readlines():
    if '@' in line:
        data = re.findall(r'\d+.\d+.\d+.\d+:\d+',line) 
        if data: 
            for proxy in data:
                if proxy not in proxys:
                    proxytxt.write(data[0] + '\n')
                    print(proxy)


