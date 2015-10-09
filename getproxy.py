import urllib.request

proxy_url = 'http://www.kuaidaili.com/proxylist/'
user_agent = "Mozilla/5.0 (iPhone; CPU iPhone OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A5376e Safari/8536.25"

def BuildReq(url):
    req = urllib.request.Request(url)
    req.add_header('User-Agent',user_agent)
    return req

if __name__ == '__main__':
    fp = open('proxy.html','w',encoding='utf-8')
    for i in range(10):
        n = i+1
        url = proxy_url + str(n)
        req = BuildReq(url)
        data = urllib.request.urlopen(req).read()
        fp.write(data.decode('utf-8'))

