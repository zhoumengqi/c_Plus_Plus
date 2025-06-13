import requests
import random
from datetime import datetime, timedelta, timezone

url = 'http://yanwan.store/run4/mi20241027.php'

headers = {
    'User-Agent': 'Apache-HttpClient/UNAVAILABLE (java 1.4)',
    'Accept-Encoding': 'identity',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Host': 'yanwan.store',
    'Connection': 'Keep-Alive'
}

# 将UTC时间转换为北京时间
def get_beijing_time():
    utc_now = datetime.now(timezone.utc)
    beijing_tz = timezone(timedelta(hours=8))
    return utc_now.astimezone(beijing_tz)

# 根据北京时间计算step值
def calculate_step():
    beijing_time = get_beijing_time()
    hour = beijing_time.hour
    
    # 检查是否在7:00-21:00范围内
    if 7 <= hour <= 24:
        # 计算时段索引（7:00为第0时段，9:00为第1时段，依此类推）
        period_index = (hour - 7) // 2
        # 每个时段增加1000，从7:00的1000开始
        base_step = 1000 + period_index * 1500
        # 添加随机偏移量（±50），使数值更自然
        random_offset = random.randint(-50, 50)
        return base_step + random_offset
    else:
        # 非运行时段返回默认值或抛出异常
        return 1000  # 可以修改为适合非运行时段的值

data = {
    'user': '1553446978@qq.com',
    'password': 'mq123456',
    'step': str(calculate_step())
}

try:
    response = requests.post(url, headers=headers, data=data)
    response.raise_for_status()
    print(f"请求成功！北京时间: {get_beijing_time().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"step参数值: {data['step']}")
    print('响应内容：')
    print(response.text)
except requests.exceptions.RequestException as e:
    print(f'请求失败：{e}')
