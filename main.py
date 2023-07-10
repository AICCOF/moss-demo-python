import json
import http.client

# TODO 请将api_key替换成您的api_key
api_key = 'moss-jp5vpvrrcgliju1a10q078isme5rhed834rp6hc9q3dvak2e'

host = 'api.aihao123.cn'
conn = http.client.HTTPConnection(host = host)

body = dict()
body['model'] = 'gpt-3.5-turbo-16k-0613'
body['prompt'] = 'Human: 你好\nAI:你好！很高兴和你交谈，有什么可以帮助你的吗？\nHuman:你是谁？'
# 将body转成json字符串
payload = json.dumps(body)

headers = {
    'Authorization': api_key,
    'content-type': 'application/json'
    }

conn.request('POST', '/moss/v1/completions', payload, headers)

res = conn.getresponse()
data = res.read()

print(data.decode('utf-8'))