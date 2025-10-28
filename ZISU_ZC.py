import requests

# --------- 你只需要修改这里⚠ ---------  
# 注意，学工平台的网络方法中无明确的用户信息，疑似用以下信息来判断用户

# 用户认证也可能会发生改变
# 获取用户认证的方法：需要在已经登陆的学工平台中，找到自身的用户认证，在开发者工具-网络正确响应中可以获得用户认证信息
headers = {
    'Authorization': 'Basic cGN3ZWI6cGN3ZWJfc2VjcmV0',
    'Blade-Auth': 'bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0ZW5hbnRfaWQiOiIwMDAwMDAiLCJ1c2VyX25hbWUiOiIyMjA4MDUwMTAzOSIsInJlYWxfbmFtZSI6Iuazruazk-S8nyIsImF2YXRhciI6IiIsImF1dGhvcml0aWVzIjpbInN0dWRlbnQiXSwiY2xpZW50X2lkIjoicGN3ZWIiLCJyb2xlX25hbWUiOiJzdHVkZW50IiwibGljZW5zZSI6InBvd2VyZWQgYnkgYmxhZGV4IiwicG9zdF9pZCI6IiIsInVzZXJfaWQiOiIxNTY5ODk3MTAyNzIwODUxOTc0Iiwicm9sZV9pZCI6IjExNjk4MjAyOTU3MDQ0Mjg1NDYiLCJzY29wZSI6WyJhbGwiXSwibmlja19uYW1lIjoi5rOu5rOT5LyfIiwicm9sZV9pZF9uYW1lIjoiMTE2OTgyMDI5NTcwNDQyODU0NizlrabnlJ8sc3R1ZGVudCIsImRldGFpbCI6eyJ0eXBlIjoid2ViIn0sImV4cCI6MTc1NTQ2NDYzOSwiZGVwdF9pZCI6IjE0NjU5NjEzMzI0MzMwNDM0NjYiLCJqdGkiOiJjZjNkMmY3Yi0wZjNlLTRiODgtOTAzNy02NWJiZTVmNGMyNjMiLCJhY2NvdW50IjoiMjIwODA1MDEwMzkifQ.nmecfWg8jiXonyRkmT2zC20EqChpAIYrBZvQUzUfT3c'
}

# --------- 你只需要修改这里⚠ ---------  

# 查询年份
years = [ 2022 , 2023 ]

def ParseSelect(response):
    items = response['data']
    for item in items:
        indexName = item['indexName']
        indexScore = item['indexScore']
        superIndexScore = item['superIndexScore']
        print(f'{indexName}: 合计 {superIndexScore} 总分 {indexScore}')

def ParseGet(response):
    item = response['data']
    schoolYear = item['schoolYear']
    score = item['score']
    studentName = item['studentName']
    gradeSort = item['gradeSort']
    majorSort = item['majorSort']
    classSort = item['classSort']
    # ?不知道代表什么意思的数据
    majorPerNum = item['majorPerNum']
    classNum = item['classNum']
    print(f'''
学年: {schoolYear} 姓名: {studentName} 综测总分: {score}\n
班级排名: {classSort} 专业排名: {majorSort} 年级排名: {gradeSort}''')


try:
    print("\n-----访问开始-----")
    for year in years:
        print(f"\n-----正在查询{year}年的综测数据-----")
        url_select = f'https://stuworkpc.zisu.edu.cn/api/newcapec-stuwork-evaluation/stuextradetail/selectAllIndexesAndExtraList?schoolYear={year}&schoolTerm=0&endPoint=web'
        url_get = f'https://stuworkpc.zisu.edu.cn/api/newcapec-stuwork-evaluation/score/getScore?schoolYear={year}&endPoint=web'
        # 请求第一个API
        response_select = requests.get(url_select, headers=headers)
        print("\n-----正在生成四项分数详情-----")
        ParseSelect(response_select.json())
        # print("第一个API响应数据:", response_select.json())

        # 请求第二个API
        response_get = requests.get(url_get, headers=headers)
        print("\n-----正在生成排名及总分-----")
        ParseGet(response_get.json())
        # print("第二个API响应数据:", response_get.json())

except requests.exceptions.RequestException as e:
    print("请求出错:", e)
except ValueError as e:
    print("JSON解析出错:", e)

print("\n-----访问结束-----")