import urllib.request
import random
import time
import socket

user_agent = "Mozilla/5.0 (iPhone; CPU iPhone OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A5376e Safari/8536.25"
access_url = [
             'http://hdcmct.org/promotionlink.php?key=1ce5393e2800789fe80502a9ee1386ef',
             'http://www.hd4fans.org/promotionlink.php?key=fe5aac9e58e45867ebaa1ac44e214505'
             ]

def BuildOpener(proxy_addr):
    proxy_handler = urllib.request.ProxyHandler({'http': proxy_addr})
    opener = urllib.request.build_opener(proxy_handler)
    return opener

def BuildReq(url):
    req = urllib.request.Request(url)
    req.add_header('User-Agent',user_agent)
    return req

if __name__ == '__main__':
    socket.setdefaulttimeout(6)
    while 1:
        fp = open('proxy.txt','r')
        proxys = fp.readlines()
        fp.close()

        num = random.randint(0,len(proxys))
        proxy_addr = proxys.pop(num).strip('\n')

        proxy_fp = open('proxy.txt','w') 
        for proxy in proxys:
            proxy_fp.write(proxy)
        proxy_fp.close()

        print('-------><--------')
        print(time.strftime('%c',time.localtime()))
        print(proxy_addr)

        opener = BuildOpener(proxy_addr)
        
        success_flg = 0

        for url in access_url:
            req = BuildReq(url)
            try:
                data = opener.open(req).read()
            except:
                print('Error!')
            else:
                print('succeeded!')
                success_flg = 1

        if success_flg != 0:
            time.sleep(100)



    

