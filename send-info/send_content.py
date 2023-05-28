# coding=utf-8
import urllib.parse
import urllib.request
import hashlib
import requests


def md5(s):
    import hashlib
    m = hashlib.md5()
    m.update(s.encode("utf8"))
    return m.hexdigest()


statusStr = {
    '0': '短信发送成功',
    '-1': '参数不全',
    '-2': '服务器空间不支持,请确认支持curl或者fsocket,联系您的空间商解决或者更换空间',
    '30': '密码错误',
    '40': '账号不存在',
    '41': '余额不足',
    '42': '账户已过期',
    '43': 'IP地址限制',
    '50': '内容含有敏感词'
}

# 短信平台账号
user = '账号'
# 短信平台密码
password = md5('密码')
# 要发送的短信内容
content = '短信内容'
# 要发送短信的手机号码
phone = '发送对象的手机号'

headers = {
    'Host': 'api.smsbao.com',
    'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
}

smsapi = "http://api.smsbao.com/"

# session = requests.session()
# session.headers.update(headers)
# resp = session.get(smsapi)
# print(resp.text)

data = urllib.parse.urlencode({'u': user, 'p': password, 'm': phone, 'c': content})
send_url = smsapi + 'sms?' + data
response = urllib.request.urlopen(send_url)
the_page = response.read().decode('utf-8')
print(statusStr[the_page])
