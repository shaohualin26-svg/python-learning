# 爬虫的本质：模拟浏览器向服务器发送请求，获取服务器返回的数据

import requests
# 目标：https://www.baidu.com url--看到的网址不可以缩写
send_url='https://www.baidu.com/'

# 请求头--客户端作为浏览器向服务器发送请求，告诉服务器，我是谁，我在哪，我在做啥，伪装头部信息
send_headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36'
}
# result表示响应结果
result=requests.get(url=send_url,headers=send_headers)
# result.text表示将响应内容输出出来，响应内容是字符串
with open(' 百度.html','w',encoding='utf-8') as f:
    f.write(result.text)
print(result.text)


























