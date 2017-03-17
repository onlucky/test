


import os

while True:
    try:
        num=int(input("请输入数字:\n"))
        break
    except ValueError:
        print("That was no valid number.  Try again")

fo=open("aa.txt","w")
count=0
while count<num:
    str="test123456\n"
    fo.write(str)
    count+=1
fo.close()

print("###########")
os.unlink("bb.txt")
os.rename("aa.txt","bb.txt")
pwd=os.getcwd()
print("当前工作目录:",pwd)

f=open("bb.txt","r")

str=f.read()
print("read()",str)
print("\n")
print("pos:",f.tell())
f.seek(0,0)
str2=f.read(10)
print("read(10)",str2)
print("pos:",f.tell())
str3=f.read(20)
print("str3",str3)
print("pos:",f.tell())
f.seek(0,0)
line=f.readline()
print("readline()",line)
print("pos:",f.tell())
f.seek(0,0)
lines=f.readlines()
print("readlines",lines)
print("pos:",f.tell())
f.seek(0,0)
for x in lines:
    print("x:",x)
f.close()


