import requests

# --------- 你只需要修改这里⚠ ---------  

# 进入"学生成绩查询"。在该界面，查看当前网址，其中包含当前帐号的gnmkdm=...将其值替换到以下的变量中
# 例如我的网址为https://portaljw.zisu.edu.cn/jwglxt/cjcx/cjcx_cxDgXscj.html?gnmkdm=N305005&layout=default
# 那么我需要修改为gnmkdm = "N305005"
gnmkdm = "N305005"

#  每日的cookie都会改变，这个方法有待改进=-=
#  获取cookie的方法：将完整的带有路径参数的网址置入浏览器中，并使用开发者工具，可以在网络方法中找到Cookie的值，对变量值进行替换即可
Cookie = "JSESSIONID=0A4552D918D30CA25F37E0DAA2D8FA5E; _gscu_1377608482=43001041vxtmge80; route=baea72139749e3a8f14890547a15b498"

# --------- 你只需要修改这里⚠ ---------  

# 需要查询的年份
year_list = ["2022", "2023", "2024"]

# 配置请求参数
# 以下参数:
# xnm决定查询哪个学期
# xqm不填入数据表示查询全部，但是查询第一学期不是1。
# queryModel.showCount决定一页展示多少数据，由于我不会写这里的分页解包，这里30的意思是故意设置大数字强迫所有数据展示到一页中，不能保证哪个学期课程>30
url = "https://portaljw.zisu.edu.cn/jwglxt/cjcx/cjcx_cxXsgrcj.html"
params = {
    "doType": "query",
    "gnmkdm": gnmkdm,
    "xnm": "2023",
    "xqm": "",
    "queryModel.showCount": 30,
}

#  网络中会有"Connection": "keep-alive"但是这里加上会导致一直占线无法访问下一学年的信息，因此需要删除
headers = {
    "Host": "portaljw.zisu.edu.cn",
    "Content-Type": "application/json;charset=UTF-8",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
    "Cookie": Cookie
}

# 发送GET请求
# response = requests.get(url, params=params, headers=headers)

def ItemParse(response):
    # print(response)
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
    print(f'该学年GPA:{gpa:.2f}')

for year in year_list:
    params["xnm"] = year  # 动态修改学年参数
    response = requests.get(url, params=params, headers=headers)
    
    print(f"\n=== {year}学年成绩 ===")
    if response.status_code == 200:
        ItemParse(response.json())
    else:
        print(f"请求失败，状态码：{response.status_code}")

