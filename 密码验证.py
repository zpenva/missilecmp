temp = 19092
realpasscord =str(temp)
i=1
while True:
    passcord = str(input('请输入您的密码：'))
    if passcord != realpasscord:
        i+=1
        if i>3:
            print("您输入的次数已经用完")
            break
    else:
        print("输入正确")
        break
