import pymongo
# 创建数据库连接
client = pymongo.MongoClient(host='localhost', port=27017)
# 指定数据库db1，没有则创建数据库db1
db = client.db1
#在数据db1中创建collection名为mid_fingertable_notice
collection=db.support_retrieve2notice
# count=collection.count()
# print(count)
data=collection.find({"fragment_type" : "01"}).limit(2000)
for json_data in data:
    for json_data1 in json_data["content"]:
        page=json_data1["page"]
        print(page)
