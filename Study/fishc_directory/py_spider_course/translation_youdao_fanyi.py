import urllib.request
import urllib.parse
import json
import time

#############################################
##########          利用有道界面，翻译文字
############################################3
while True:

    content = input('请输入需要翻译的内容(输入q！推出程序)：')
    if content == 'q!':
        break

    url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule"

    # 添加User Agent来隐藏自己的地址
    head = {}
    head['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'


    data = {}
    data['i'] = content
    data['from'] = 'AUTO'
    data['to'] = 'AUTO'
    data['smartresult'] = 'dict'
    data['client'] = 'fanyideskweb'
    data['salt'] = '16000140929134'
    data['sign'] = '104816b59dfc2e7d1bfe9f85d97298ae'
    data['lts'] = '1600014092913'
    data['bv'] = '02edb5d6c6ac4286cd4393133e5aab14'
    data['doctype'] = 'json'
    data['version'] = '2.1'
    data['keyfrom'] = 'fanyi.web'
    data['action'] = 'FY_BY_CLICKBUTTION'

    data = urllib.parse.urlencode(data).encode('utf-8')

    # html 为字符串结构的json格式
    req = urllib.request.Request(url, data, head)
    response = urllib.request.urlopen(req)
    html = response.read().decode('utf-8')

    # 字符串变为python的字典格式
    target = json.loads(html)
    target = target['translateResult'][0][0]['tgt']

    print("翻译结果是：%s"% (target))
    time.sleep(5)

