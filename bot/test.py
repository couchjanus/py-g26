# 
import requests

result = requests.get('https://api.telegram.org/bot/getMe')

print(result.json())
# (chenv) C:\xampp\htdocs\py-g26\bot>python test.py
# {'ok': True, 'result': {'id': 2146151888, 'is_bot': True, 'first_name': 'myex_bot', 'username': 'myexpy_bot', 'can_join_groups': True, 'can_read_all_group_messages': False, 'supports_inline_queries': False}}

