#存储数据
# 使用json.dump() 把数字列表存储到文件number.json中

import json

numbers = [2, 5, 3, 4, 12, 32]

filename = 'number.json'
with open(filename, 'w') as f_obj:
    json.dump(numbers,f_obj)