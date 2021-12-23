import urllib.request
import urllib.parse


######################################################
##########          利用google translate，翻译英文到中文
######################################################

url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule"


# 提交的数据
data = {}
data['i'] = '我是一个好人'
data['from'] = 'AUTO'
data['to'] = 'AUTO'
data['smartresult'] = 'dict'
data['client'] = 'fanyideskweb'
data['salt'] = '16398683723216'
data['sign'] = '4552a342294ee9c4412711c4aa58d5fc'
data['lts'] = '1639868372321'
data['bv'] = 'fdac15c78f51b91dabd0a15d9a1b10f5'
data['doctype'] = 'json'
data['version'] = '2.1'
data['keyfrom'] = 'fanyi.web'
data['action'] = 'FY_BY_CLICKBUTTION'

data = urllib.parse.urlencode(data).encode('utf-8')

# 添加User Agent来隐藏自己的地址
head = {}
head['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'


# 打开网页，然后读取网页
req = urllib.request.Request(url, data)
response = urllib.request.urlopen(req)
html = response.read().decode('utf-8')


print(html)

