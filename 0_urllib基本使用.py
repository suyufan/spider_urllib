import urllib.request

# 1.定义url
url = 'http://www/baidu.com'

# 2.模拟浏览器向服务器发送请求 response响应
response = urllib.request.urlopen(url)

# 3.获取响应中的页面源码
# read方法 返回的是字节形式的二进制数据
# 二进制--》字符串 解码 decode('编码的格式')
content = response.read().decode('utf-8')

# 4.打印数据
print(content)