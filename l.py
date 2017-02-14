print('---欢迎进入通讯录程序---')
print('---1：查询联系人资料---')
print('---2：插入新的联系人---')
print('---3：删除已有的联系人---')
print('---4：退出通讯录程序---')

dictory=dict()
temp1 = input('请输入相关指令代码：')

if temp1 == 1:
    temp2 = input('请输入需要查询的联系人姓名：')
    print('name:',temp2)
    print('phonenumber:',dictory['temp2'])
else:
    print('您查找的姓名不在通讯录中')

if temp1 == 2:
    temp2 = input('请输入需要添加的联系人姓名：')
    temp3 = input('请输入需要添加的联系人号码：')
    dictory.setdefault(temp2,temp3)

