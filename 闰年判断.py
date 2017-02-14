temp = input("输入年份:")
while not temp.isdigit():
    temp = input("抱歉，请输入一个整数：")
year = int(temp)
if year%400 == 0:
    print("是闰年")
else:
    if (year % 4 == 0) and (year % 100 != 0):
        print(temp+'是闰年')
    else:
        print(temp+'不是闰年')
