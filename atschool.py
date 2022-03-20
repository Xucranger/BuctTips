import requests
from bs4 import BeautifulSoup
import re
import urllib3
import execjs

data = {
    "sch_id": 143,
    "stud_no": "2019030160",
    "stud_name": "徐鹤翔",
    "sign": "e28e69de5b9a6e00fe50b5fad940de4a"
}

header = {
    "Host": "wechat.v2.traceint.com",
    "Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat(0x63030532)",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Accept-Encoding": "gzip, deflate",
    "Cookie": "Hm_lvt_7ecd21a13263a714793f376c18038a87=1634180809,1634640932,1634649114; Hm_lpvt_7ecd21a13263a714793f376c18038a87=1634652733; wechatSESS_ID=102cfbcf220ce2fd5a7d7097cbf9e4d77614f44879544bb2; SERVERID=b9fc7bd86d2eed91b23d7347e0ee995e|1634689716|1634689713",
    "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7"
}

url = "http://wechat.v2.traceint.com/index.php/schoolpush/registerLogin?sch_id=143&stud_no=2019030160&stud_name=%E5%BE%90%E9%B9%A4%E7%BF%94&sign=e28e69de5b9a6e00fe50b5fad940de4a"

resp = requests.get(url, headers=header, data=data)

print(resp)

resp.close()
