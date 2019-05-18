import random
import string

import redis

# 创建redis链接对象
r = redis.Redis(host='127.0.0.1',port=6379,decode_responses=True)

for j in range(200):
    chars = string.digits + string.ascii_uppercase
    chosen_char = [random.choice(chars) for i in range(12)]
    promo_code = ''.join(chosen_char)
    # 存储键值对
    r.sadd("promo_code", promo_code)
