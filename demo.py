import requests
import json 

url = r'https://iam.cn-north-4.myhuaweicloud.com/v3/auth/tokens'

d = '{"auth":{"identity":{"methods":["password"],"password":{"user":{"domain":{"name":"*"},"name":"*","password":"*"}}},"scope":{"domain":{"name":"*"}}}}'

r = requests.post(url=url,data=d) # requests.post() 中利用 data 属性
token=r.headers.get("X-Subject-Token")

#解绑MFA 

url = r'https://iam.cn-north-4.myhuaweicloud.com/v3.0/OS-MFA/virtual-mfa-devices'
header = {
    "Content-Type": "application/json",
    "X-Auth-Token": token
}


r = requests.get(url=url,headers=header)
serial_number=r.json().get("virtual_mfa_devices")[0]['serial_number']
user_id=r.json().get("virtual_mfa_devices")[0]['user_id']
print(serial_number)
print(user_id)

url = r'https://iam.cn-north-4.myhuaweicloud.com/v3.0/OS-MFA/mfa-devices/unbind'
header = {
    "Content-Type": "application/json",
    "X-Auth-Token": token
}

r = requests.put(url=url,headers=header,data=json.dumps({"user_id":user_id,"serial_number":serial_number}))
print(r.status_code)
