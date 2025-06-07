import requests
import random

url = 'http://yanwan.store/run4/mi20241027.php'

headers = {
    'User-Agent': 'Apache-HttpClient/UNAVAILABLE (java 1.4)',
    'Accept-Encoding': 'identity',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Host': 'yanwan.store',
    'Connection': 'Keep-Alive'
}

data = {
    'user': '1553446978@qq.com',
    'password': 'mq123456',
    'step': str(random.randint(1000, 1200))  # 生成1000-1200之间的随机整数并转为字符串
}

try:
    response = requests.post(url, headers=headers, data=data)
    response.raise_for_status()  # 检查请求是否成功
    print(f"请求成功！step参数值: {data['step']}")
    print('响应内容：')
    print(response.text)
except requests.exceptions.RequestException as e:
    print(f'请求失败：{e}')
