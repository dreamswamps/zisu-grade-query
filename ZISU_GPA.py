import requests

# --------- 你只需要修改这里⚠ ---------  

# 该脚本旨在一次性获取所有课程信息。数量可能较多。
# 如何修改查看ZISU.py
# Cookie可能也需要修改
gnmkdm = "N305005"
Cookie = "JSESSIONID=5EB239D800851EEBF99CF4E0C8E540AD; _gscu_1377608482=43001041vxtmge80; route=baea72139749e3a8f14890547a15b498"

# --------- 你只需要修改这里⚠ ---------  

url = "https://portaljw.zisu.edu.cn/jwglxt/cjcx/cjcx_cxXsgrcj.html"
params = {
    "doType": "query",
    "gnmkdm": gnmkdm,
    "xnm": "",
    "xqm": "",
    "queryModel.showCount": 100,
}
# 如果出现查询信息过多的情况，直接修改为比100更大的值

headers = {
    "Host": "portaljw.zisu.edu.cn",
    "Content-Type": "application/json;charset=UTF-8",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
    "Cookie": Cookie
}

# response = requests.get(url, params=params, headers=headers)

def ItemParse(response):
    items = response['items']
    print("查询到",len(items),"条信息")
    xfj_sum = 0
    xf_sum = 0
    id = 0
    for item in items:
        id+=1
        cj = item['cj']
        jd = item['jd']
        kccjpm = item['kccjpm']
        kcmc = item['kcmc']
        xf = item['xf']
        xfj_sum += float(xf) * float(jd)
        xf_sum += float(xf)
        print('ID:'+str(id)+'  课程名称:'+kcmc+'  成绩:'+cj+'  绩点:'+jd+'  排名:'+str(kccjpm)+'  学分:'+xf)
    gpa = xfj_sum / xf_sum
    print(f'总GPA:{gpa:.2f}')

response = requests.get(url, params=params, headers=headers)

print(f"\n=== 总成绩 ===")
if response.status_code == 200:
    ItemParse(response.json())
else:
    print(f"请求失败，状态码：{response.status_code}")

