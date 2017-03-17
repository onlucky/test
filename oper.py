
# 该实例演示了数字猜谜游戏
number = 7
guess = -1
print("数字猜谜游戏!")
while guess != number:
    try:
        guess = int(input("请输入你猜的数字："))
        if guess == number:
            print("恭喜，你猜对了！")
        elif guess < number:
            print("猜的数字小了...")
        elif guess > number:
            print("猜的数字大了...")
    except ValueError:
        print("that is not a valid number,try again")

##
print("打印集合\n")
seta={"a","b","c","d","a","1","2"}
print(seta)
setb=set('12345678901')
print(setb)
#print("a+b",seta + setb)
print("a-b",seta - setb)
print("a&b",seta & setb)
print("a|b",seta|setb)
print("a^b",seta ^ setb)

dt={"id":123,"name":"hmx"}
dt[234]="test"

for k,v in dt.items():
    print(k,v)
