import re
import os

proxyhtml = open('proxy.html','r',encoding='gbk')
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
    if '@' in line:
        data = re.findall(r'\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}:\d+',line) 
        if data: 
            for proxy in data:
                if proxy not in proxys:
                    proxytxt.write(data[0] + '\n')
                    new_num += 1
                else:
                    same_num += 1

print(str(same_num)+' proxys are the same!')                    
print(str(new_num)+' proxys added!')

