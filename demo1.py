# '''
# 判断
# '''
# a=10
# b=20
# if a>b:
#     print("a比b大")
# print("a比b小")    
# username=input("请输入账号:")
# password=input("请输入密码：")
# if len(username)>5:
#     if len(password)>8:
#         print("注册成功")
#     else:
#         print("您的密码不正确，请重新输入")
# else:
#     print("您输入的账号不正确，请重新输入")        
# a=[1,2,5,5,6,5,5]
# for i in a:
#     print("哈")
# for i in range(1,10):
#     for j in range(1,i+1):
#         print(i,"x",j,"=",i*j,end="  ")
#     print()    
a=1
sum=0
while(a<=10):
    sum=sum+a
    a=a+1
    if a ==3:
        break
    if a ==2:
        continue
    print(sum)
print("-------")    