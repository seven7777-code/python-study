#输入
name=input("请输入你的名字：")
age=input("请输入你的年龄：")

print("你好，",name)
print("你的年龄是",age)

#类型转换（重点）
age=input("年龄：")#得到的是字符串
age=int(age)
age=int(input("请输入年龄："))
print(age+1)
