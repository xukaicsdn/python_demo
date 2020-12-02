import time
import random
import pdb
from faker import Faker
import requests

f=Faker(locale='zh_CN')
# print(f.name())
a = time.strftime("%Y-%m-%d %H:%M:%S")
print(a,type(a))




"""
    在控制台输入秒数
    输出时分秒

"""
"""
def totle_second_to_HMS(totle_second):
    totle_second = int(totle_second)
    int_hour = totle_second // 3600
    int_minute = totle_second % 3600 // 60
    int_second = totle_second % 3600 % 60
    print("时：" + str(int_hour) + "     分：" + str(int_minute) + "     秒：" + str(int_second))

totle_second_to_HMS(3661)
"""


"""
    购买商品，总价达到100元打八折，缺少提示还缺多少钱，多了提示找您多少钱

"""

"""
def buy(float_money,float_goods_price,int_num):
    if not isinstance(float_money,float):
        print(str(float_money) + '  付出金额数据类型不正确，请重新尝试')
    elif not isinstance(float_goods_price,float):
        print(str(float_goods_price) + '  商品单价数据类型不正确，请重新尝试')
    elif not isinstance(int_num,int):
        print(str(int_num) + '  商品个数数据类型不正确，请重新尝试')
    else:
        totle_money = float(float_goods_price) * int(int_num)
        # print(type(totle_money))
        if  totle_money >= 100 :
            totle_money *= 0.8
            print("应收您{0}元".format(str(totle_money)))
            if float_money < totle_money :
                print("还缺%s"%(totle_money - float_money))
            elif float_money > totle_money :
                print("找您%s"%(float_money - totle_money))

        elif totle_money < 100 :
            print("应收您{0}元".format(str(totle_money)))
            if float_money < totle_money :
                print("还缺%s"%(totle_money - float_money))
            elif float_money > totle_money :
                print("找您%s"%(float_money - totle_money))


buy(100.7,60.0,3)
"""


"""
# round保留几位小数   且四舍五入
num = round(3.1415926,3)
print(num)
"""



"""
    获取月份。判断是哪一季节（春夏秋冬）

"""
"""
def month(int_month):
    if not isinstance(int_month, int):
        print('输入格式不正确，格式必须为整数且范围为 1-12，请重新尝试')
    else:
        if  int_month < 1 or  int_month > 12 :                       # 此条件放在第一个可以提高性能
            print('月份：  ' + str(int_month) + '  输入数据不正确，请重新尝试')
        elif int_month in (1,2,3):
            print(str(int_month) + '月是：春天')
        elif int_month in (4,5,6):
            print(str(int_month) + '月是：夏天')
        elif int_month in (7,8,9):
            print(str(int_month) + '月是：秋天')
        elif int_month in (10,11,12):
            print(str(int_month) + '月是：冬天')



month(3)
"""


"""
    输入月份，得出该月有多少天

"""


"""
def month_to_day(int_month):
    if not isinstance(int_month,int) :
        print('输入格式不正确，格式必须为整数且范围为 1-12，请重新尝试')
    else :
        if  int_month < 1 or  int_month > 12 :                       # 此条件放在第一个可以提高性能
            print('月份：  ' + str(int_month) + '  输入数据不正确，请重新尝试')
        elif int_month in (1,3,5,7,8,10,12) :
            print(str(int_month) + ' 月31天')
        elif int_month in (4,6,9,11) :
            print(str(int_month) + ' 月30天')
        elif int_month == 2 :
            print(str(int_month) + ' 月28天')

month_to_day(2)

#  注意：in里面不能是一个元素，如in(2)就会报错，in(2,3)就不报错
"""

"""
    四个值取最大值

"""

"""
num01 = 1
num02 = 2
num03 = 3
num04 = 4

max_value = num01
if max_value < num02 :
    max_value = num02
if max_value < num03 :
    max_value = num03
if max_value < num04 :
    max_value = num04
print(max_value)
"""
"""====================================================================================================="""
"""
    若有多个条件给变量赋值，那么可以一句话搞定____用条件表达式
    语法：
        变量 = 结果1 if 条件 else 结果2
    作用范围：
        根据条件(True/False)来决定返回结果1还是结果2
    如：
        sex = None
        if input('请输入性别：') == '男':
            sex = 0
        else:
            sex = 1
      变换
        sex = 0 if input('请输入性别：') == '男' else 1

"""
"""
sex = None
if input('请输入性别：') == '男':
    sex = 0
else:
    sex = 1
"""
"""
sex = 0 if input('请输入性别：') == '男' else 1
"""
"""
def fuck(sex = ''):
    if sex == '男' :
        return True
    elif sex == '女' :
        return  False
"""

"""
num = int(input('请输入整数：'))
if  num % 2 :
    print('奇数')
else :
    print('偶数')
"""





"""====================================================================================================="""
"""
    while循环
    while True :
        执行

"""
"""
    控制台输入开始值和结束值，输出开始值和结束值的中间值   比如  开始8   结束13   输出9，10,11,12

"""
"""
begin = int(input('请输入开始整数值：'))
end = int(input('请输入结束整数值：'))
while begin < end - 1 :
    begin += 1
    print(begin)
"""

"""
    一张纸厚度0.01毫米
    请问对折多少次，可以超过珠穆朗玛峰的8844.43米

"""
"""
float_thickness = 0.01 / 1000
count = 0
while float_thickness <= 8844.43 :
    float_thickness *= 2
    count += 1
    print('第%s折叠厚度为%s'%(count,float_thickness))
"""

"""
    猜数字1.0
    规则：
        系统产生1-100的随机数，让用户重复猜，直到用户才对为止，并给出对应提示

    猜数字2.0
    规则：
        最多只能猜10次

"""
"""
random_number = random.randint(1,100)
print(random_number)

def number():
    while random_number:
        int_number = int(input('请输入：'))
        if int_number == random_number:
            print('猜对了就是%s'%(random_number))
            break
        else:
            print('猜错了，继续猜')

number()
"""
"""
# 2.0
random_number = random.randint(1,100)
print(random_number)

def number():
    count = 0
    while count < 10:
        count += 1
        int_number = int(input('请输入：'))
        if int_number == random_number:
            print('猜对了就是%s'%(random_number))
            break
        else:
            print('猜错了，继续猜')
            print('第%s次猜'%(count))
    else:
        # 适用场景，只有while条件结束，才会执行else里面的语句**************************************
        print('没机会了哦')

number()
"""











"""======================================================================================================"""
"""
    for 变量名 in 可迭代对象

"""

"""
for i in range(5, -1 ,-1):    # 543210
    print(i)
"""

"""
    随机产生两个数字加法考试
    一共五道题
    答对加10分
    打错扣5分


"""
"""
def topic():
    score = 0
    for i in range(5):
        number1 = random.randint(1,50)
        number2 = random.randint(1,50)
        print('第%s道题number1 + number2 = %s'%( i + 1,number1 + number2) )
        result = int(input('请输入你得结果：'))
        if result == number1 + number2 :
            score += 10
            print(score)
        else:
            score -= 5
            print(score)
    print('最终成绩为%s'%(score))

topic()
"""




"""
    累加1-100之间能被3整除的整数和

"""

# 下面先看下从1加到100等于4950的代码
"""
sum = 0
for i in range(1,101):
    sum += i
    print(i)

print(sum)
"""

# 第一种方法
"""
sum = 0
for i in range(1,101):
    if i % 3 == 0:
        sum += i
print(sum)
"""

# 第二种方法
"""
sum = 0
for i in range(1,101):
    # 不满足条件跳过
    if i % 3 != 0:
        continue
    sum += i
print(sum)
"""

"""
    一个球从100米高空落下，每次弹起高度是原始高度的一半，假设最小弹起个度为0.01米，
    那么请问能弹多少次，期间一共弹出多少米
    ****************************重要的逻辑思想****************************

"""

"""
# 单位都是米
hight = 100
count = 0
sum = hight
while hight * 0.5 >= 0.01:          # 值得深思 hight * 0.5 每次弹起的高度做条件
    count += 1
    hight *= 0.5
    sum += hight * 2   # 乘以2的目的是一下一上一下的距离   还要加上一开始的100米  尼玛挺细
    print('第%s次弹出高度为%s'%(count,hight))
else:
    print('第%s次将不会再弹起，且一共弹了%s米'%(count + 1 ,round(sum)))
"""










"""======================================================================================================"""


"""
    字符串

"""

"""
name = "悟空"
name = "孙悟空"
print (name)
# 不是将字符串“悟空"改变为“孙悟空"
# 而是创建了新字符串对象"孙悟空",替换变量name中存储的地址.
"""

"""
#字符-->编码値
print (ord("天"))
#编码值-->字符
print (chr (9763))
"""

"""
#练习1：在控制台中获取一个字符串，打印每个字符的编码值.
str_input = input ("请输入文字:")
for item in str_input:
    print(ord(item))


#练习2:在控制台中循环输入编码值,显示字符.直到输入负数时,退出.
while True:
    number = int (input ("请输入编码值:"))
    if number < 0:
        break
    print (chr (number))
"""
"""
print('大家\n好') # \n换行
print(r'C:\Drivers') # r取消转义
print('覅爽\t肤水') # \t制表符(一个tab键四个空格)
"""
"""
    1.定义:生成一定格式的字符串。
    2.语法:字符串%(变量).
            "我的名字是%s,年龄是%"% (name, age)
    3,类型码: %s字符串 %d整数 %f浮点数.
    4,格式: %[- + 0 宽度 精度]类型码.
    - : 左对齐(默认是右对齐).
    + : 显示正号.
    0 : 左侧空白位置补零.
    宽度 : 整个数据输出的宽度.
    精度 : 保留小数点后多少位.

"""
"""
print('发撒会发生的骄傲放假哦到%100s付'%('uhsauhd'))
# 可以完美解决时间显示的问题
print('整数是：%02d'%(2000))  # 宽度为2   不足两位补0
print('整数是：%02d'%(12))
"""
"""
    #练习：在控制台中显示120秒倒计时:
    02:00     01:59 ........ 00:

"""
"""
for i in range(120,0,-1):   # //取整    %取余
    print('%2d:%2d'%(i // 60,i % 60))
    print('%02d:%02d'%(i // 60,i % 60))
"""

"""
    字符串成员运算

"""
"""
str1 = '我叫许凯'
print('许' in str1)   # 必须从前往后 许凯行   凯许就不行
"""

"""
#切片
str04 = 'abcde'
#切片
print (str04 [0:3])  # abc
print (str04[0:3:2]) # ac
print (str04[::])    # abcde
print (str04[::-1])  # edcba
print (str04[-2:-5:-1]) # dcb
print(str04[1:10])   # bcde        切片即使越界也不会错误
"""



"""
    # 练习：在控制台中输入一个整数,根据整数打印一个矩形
    如：整数：4
                ****    *****   ******
                *  *    *   *   *    *
                *  *    *   *   *    *
                ****    *   *   *    *
                        *****   *    *
                                ******

"""
"""
def number(int_number):
    # 头
    print('*' * int_number)     # 头尾都是这样，中间的怎么整呢
    # 中间
    for i in range(int_number - 2):   # 中间的
        print('*' + ' ' * (int_number - 2) + '*')
    # 尾
    print('*' * int_number)

number(40)
"""











"""====================================================================================================="""
"""
    列表
    定义:
        由一系列变量组成的可变序列容器。
    列表在内存是怎样存储的     重要

"""
"""
list01 = ['a','b','c',1,9000000000000000000000000,0.1,True,False]
for i in list01:
    print(i,type(i))

# 在列表末尾追加元素（可迭代对象）
# list01.append('d')
# print(list01)

# insert 插入（索引，元素）
list01.insert(1,'f')
print(list01)

# 删除元素
# 移除指定元素
list01.remove('c')
print(list01)

# 删除指定索引的元素
del list01[1]
print(list01)
"""

"""
    在控制台输入学生成绩，计算总分，最高分，最低分
    “请输入学生姓名：”
    “请输入第一个学生成绩”

"""
"""
def stu_score(int_stu_count):
    list_stu = []
    for i in range(int_stu_count):
        score = int(input("请输入第%s个学生成绩："%(i + 1)))
        list_stu.append(score)
    print(max(list_stu))

stu_score(3)
"""

"""
    找出列表最大值    利用for    不能用max     假设第一个元素是最大值，    这种思想要掌握

"""
"""
list02 = [30,33,60,15,13,16,90]
max_value = list02[0]
for i in range(1,len(list02)):
    if list02[i] > max_value:
        max_value = list02[i]
print(max_value)
"""


"""
    字符串 VS 列表

"""
"""
# 根据某些逻辑   拼接字符串
result = ''
for i in range(10):
    result += str(i)
print(result)
#每次拼接,创建一个新对象,替換变量地址   垃圾太多了   内存受不了  此方法不采用----------  所以下面用列表拼接
"""

"""
result = []
for i in range(10):
    result.append(str(i))
print(result,type(result))
# join:将列表使用连接符,合成一个字符串
str_result = '+'.join(result)       # 返回字符串
print(str_result,type(str_result))

# split:根据分隔符拆分字符串
list01 = str_result.split('+')      # 返回列表
print(list01,type(list01))
"""


"""
    练习：
    1.在控制台中循环录入字符串,输入q时退出
    然后显示一个新的字符串.

    2.判断字符串是否是回文:·
    上海自来水来自海上
    牛产牛奶
    提示:字符串翻转

    3.一注彩票7个球
    前六个是红球 ： 1  -- 33 之间的数字，且不能重复
    最后一个是篮球 ： 1 -- 16之间的数字
    （1）在控制台中购买彩票
    （2）随机产生一注彩票

    import random
    random.randint(1,16)


"""
"""
# 练习1
list_str = []
while True:
    str001 = str(input("请输入字符串："))
    if str001 != 'q':
        list_str.append(str001)
    else:
        print(list_str)
        str_list_str = ''.join(list_str)
        print(str_list_str)
"""


"""
# 练习2   # 第一种方法
while True:
    list_str = []
    str001 = str(input("请输入字符串："))

    for i in str001:
        list_str.append(i)
    if list_str[::] == list_str[::-1]:
        print("回文字符串为：%s"%("".join(list_str)))
        break
    elif list_str[::] != list_str[::-1]:
        continue
"""
"""
# 练习2   # 第二种方法
ss = 'U盾发红奥世纪东方iOS就ofois都'
if ss == ss[::-1]:
    print("是回文")
else:
    print("不是回文")
"""



"""
# 练习3-（1）
ticket = []
while len(ticket) < 6:  # 等于6的时候停止循环
    number = int(input("请输入第%s个红球号码："%(len(ticket) + 1)))
    if number < 1 or number > 33:
        print("输入号码不在范围内")
    elif number in ticket:
        print("%s号码已选"%(number))
    else:
        ticket.append(number)


while True:
    number = int(input("请输入蓝球号码："))
    if 1 <= number <= 16:
        ticket.append(number)
        break
    else:
        print("号码不在范围内")

print(ticket)
"""



"""
# 练习3-（2）
ticket = []
while len(ticket) < 6:
    number = random.randint(1,33)
    if number not in ticket:
        ticket.append(number)
    print(len(ticket))

print(ticket)
"""
"""
list001 = []
for i in range(10):
    number = random.randint(1,10)
    list001.append(number)
print(tuple(list001))
"""







"""见微信笔记列表内存图"""
"""
list01 = [1,2]
# 将列表中元素复制一份 等同list01.copy()
list02 = list01[::]   # 切片之后其实是产生一个新的列表
list01[0] = 100
print(list01)
print(list02)
print(list02[0])
"""

"""
list01 = [1,2]
list02 = list01
list01[0] = 100
print(list02[0])
"""

"""
list01 = [1,2]
list02 = list01
list01 = [100]
print(list02[0])
print(list01)
"""

"""
list01 = [1,[2,3]]
list02 = list01.copy()  # 浅拷贝
list01[1][0] = 200
print(list02[1][0])
"""

"""
import copy
list01 = [1,[2,3]]
list02 = copy.deepcopy(list01)  # 深拷贝   所有依赖关系全部拷贝过来，只不过得全部换内存地址
list01[1][0] = 200
print(list02[1][0])
"""



"""
    列表推导式

"""

"""
list01 = [3,5,6,7,9]
# 创建新列表，每个元素是list01中元素的平方
list02 = []
# for i in list01:
#     list02.append(i ** 2)
# print(list02)

for i in list01:
    if i % 2 == 0:
        list02.append(i ** 2)
print(list02)

# 语法: [对变量的操作 for 变量名 in 可迭代对象]
list03 = [i ** 2 for i in list01]
list04 = [i ** 2 for i in list01 if i % 2 == 0]
"""


"""
        #练习：使用range生成1--10之间的数字，存入列表list0l中使用列表推导式，
            将List01中所有奇数存入List02将list0l中所有偶数存入List03


"""

"""
list01 = []
for i in range(10):
    number = random.randint(1,10)
    list01.append(number)
print(list01)

list02 = [i for i in list01 if i % 2 != 0]
print(list02)
list03 = [i for i in list01 if i % 2 == 0]
print(list03)
"""













"""========================================================================"""

"""
    元组
    定义：
        由一系列变量组成的不可变序列容器。
        不可变是指一但创建,不可以再添加/删除
    作用：
        元组与列表都可以存储一系列变量,由于列表会预留内存空间,
        元组会按需分配内存,所以如果变量数量固定,建议使用元组,
    应用:
        变量交换的本质就是创建元组: x, y=y, x..格式化字符串的本质就是创建元祖: "姓名:%s,年龄:%d"

"""

"""
#2．创建具有默认值的元组
t01 = (1,2,3)
t01 = tuple("abcd")
t01= (1,2,[4,5])
print (t01)

#修改
#t01[2]=100      元组元素不能修改
t01[2][0] = 100      #修改的是元素第三个元素(列表)的元素
print(t01)

#3.获取元素（索引  \  切片）
print(t01[:2])


# 获取元祖所有元素

for i in t01:
    print(i)

# 倒序获取元祖所有元素
for i in range(len(t01) - 1,-1,-1):
    print("==============")
    print(t01[i])
"""



"""
t02 = ("a","b")
l02 = ["a","b"]

t03 = t02
l03 = l02

t02 += ("c","d")     #创建了新元组对象，改变了t02存储的地址.
l02 += ["c","d"]     #将["c","d"]追加到原列表中.

print(t03)  #?   ('a', 'b')
print(l03)  #?   ['a', 'b', 'c', 'd']
print(l02)
"""


"""
# 如果元组只有一个元素，必须多写一个逗号,否则视为普通对象,不是元组对象.
t04 = (1)   # 认为为整数1
print(t04)
t05 = (1,)
print(t05)
"""

"""
month = int (input ("请输入月份:"))
if month < 1 or month > 12:
    print ("输入有误")
else:
    # 将每月的天数，存入元组
    day_of_month = (31,28,31,30, 31,30, 31, 31,30, 31, 30, 31)
    print(day_of_month[month -1])
"""



"""
# 练习2： 在控制台输入月，日
#             计算这是这一年的第几天
#             例如：3月5日
#             累加1月，2月总天数，在累加三月的5天



month = int (input ("请输入月份:"))
day = int (input ("请输入日:"))

if month < 1 or month > 12:
    print ("月份输入有误")
elif day < 1 or day >31:
    print ("日输入有误")
else:
    # 将每月的天数，存入元组
    day_of_month = (31,28,31,30, 31,30, 31, 31,30, 31, 30, 31)
    # print(day_of_month[month -1])
    res = 0
    # for i in range(month -1):
    #     # print(day_of_month[i],'yyyyyyyyyyyyy')
    #     res += day_of_month[i]
    res = sum(day_of_month[:month - 1])  # 和上边那个for循环一样的效果

    res += day
    print(res)
"""









"""======================================================================="""


"""
    字典   字典是无序的


"""


"""
# 创建空字典
d01 = {}
d01 = dict()

d01 ={"a":"A","b":"B"}
#d01= dict("ab")   #分不清key value
d01 = dict([(1,2),(3,4)])   # {1: 2, 3: 4}
print(d01)


# 第一次增加
d01["c"] = "C"
# 第二次修改
d01["c"] = "CC"
print(d01)

# 读取元素（如果不存在则异常)
# 建议：在宇典中读取元素，先判断存在，在进行读取
if "d" in d01:
    print (d01["d"])


# 删除
del d01["c"]

# 获取字典中所有元素
for key in d01:
    print(key)

for k in d01.items():
    print(k)    #(1, 2)  (3, 4)   结果是元组


for k,v in d01.items():
    print(k)  # 1 2   3 4
    print(v)

# 获取所有的键
for k in d01.keys():
    print(k)    # 1    3

# 获取所有的值
for v in d01.values():
    print(v)
"""



"""
seasons ={
    1: "有1,2,3月",
    2: "有4,5,6月",
    3: "有7,8,9月",
    4: "有10,11,12月"
}

season = int(input ("请输入季度:"))
if season not in seasons:
    print ("输入有误")
else:
    print(seasons[season])
"""

"""
# 练习2 ： 在控制台录入一个字符串
#         打印这个字符串中的字符以及这个字符出现的次数
#         abcdbcdb
#         a字符1次
#         b    3

# 思路：  字符  in  字符串

# 注意：
#      # 第一次增加
#      d01["c"] = "C"
#      # 第二次修改
#      d01["c"] = "CC"
#      print(d01)

str_words = input("请输入字符串：")
# str_words = ['a','b','c','d','b','c','d','b']
# key 字符   value 次数
d02 = {}
# 逐一判断字符出现的次数
for i in str_words:
    # print(str_words[i])
    # 如果没统计过该字符串
    if i not in d02:    # 判断字典中有没有某些键
        d02[i] = 1
    else:
        # 否则次数加一
        d02[i] += 1
print(d02)
"""

"""
    字典推导式

"""


"""
dic01 = {}
for i in range(1,10):
    dic01[i] = i ** 2
print(dic01)

dic01 = {i : i ** 2 for i in range(1,10)}
print(dic01)
"""


"""
dic01 = {}
for i in range(1,10):
    if i % 2 == 0:
        dic01[i] = i ** 2
print(dic01)

dic01 = {i : i ** 2 for i in range(1,10) if i % 2 == 0}
print(dic01)
"""



"""
list01 = ["张三丰","无忌","赵敏"]
# d01 = {}
# for i in list01:
#     if i not in d01:
#         print(i,"============")
#         d01[i] = len(i)
#         print(d01)
# print(d01)

d02 = {i:len(i) for i in list01}
print(d02)
"""



#练习2：
#[“张三丰",“无忌”, "赵敏"]
#[101, 102, 103]
#(1)根据两个列表形成一个字典:key姓名, value房间号
#(2)将字典的健与值进行翻转·即: key房间号,value姓名
"""
list01 = ["张三丰","无忌","赵敏"]
list02 = [101, 102, 103]
d01 ={}


# 第一种方法
for i in list01:
    for j in list02:
        d01[i] = j
# 第二种方法
for i in range(len(list01)):
    d01[list01[i]] = list02[i]

# 第三种方法
d01 ={list01[i] : list02[i] for i in range(len(list01))}
print(d01)

#(2)将字典的健与值进行翻转·即: key房间号,value姓名
d02 = {}
for k,v in d01.items():
    d02[v] = k

d02 = {v:k for k,v in d01.items()}
print(d02)

# {'张三丰': 101, '无忌': 102, '赵敏': 103}
# {101: '张三丰', 102: '无忌', 103: '赵敏'}

# 有一种情况如果说是值是相同的，会覆盖  如：{101: '张三丰', 102: '赵敏'}  怎么办！！！！
list03 = [(v,k) for k,v in d01.items()]
print(list03)
# [(101, '张三丰'), (102, '无忌'), (103, '赵敏')]
"""



#

"""
day05作业
1,三合一
2·当天练习独立完成
3,内存图:*****************重要*********************8
"""

# list01 = ["a", (1,2,3),{"b":"B", "c":"C"}]
# list02 = list01
# list03 = list01[:]
# list02[0] = "b"
# print(list01[0])# ?
# list02[2] ["b"]= "BB"
# print (list02[2]["b"])# ?
# list03[0] = "bb"
# print (list01[0])# ?

# 4,在控制台中录入学生信息(姓名/年龄/性别)  用字典加列表
"""
[
    {
        "name":xx,
        "age":xx,
        "sex":xx

    },
    {
        "name":xx,
        "age":xx,
        "sex":xx

    }

]
"""
"""
def student_info(str_sex = ""):
    list_student_info = []
    for i in range(3):
        dict_student = {}
        dict_student["name"] = f.first_name()
        dict_student["age"] = random.randint(5,30)
        dict_student["sex"] = str_sex
        list_student_info.append(dict_student)
    print(list_student_info)

student_info("男")
"""




"""
    5.扩展练习:
          猜拳规则:
                       系统随机出拳,在控制台中循环猜测
     提示：(1)将胜利的策略存入容器
     （
        ("石头","剪刀"),
        ("剪刀","布"),
        ("布","石头")
      ）
           (2)将用户猜的拳与系统出拳形成一个元组
"""
#将用户猜的拳与系统出拳形成一个元组
"""
wins = (
        ("石头","剪刀"),
        ("剪刀","布"),
        ("布","石头")
       )

user_input_index = int(input ("请输入整数(0表示石头, 1表示剪刀, 2表示布:"))
items = ("石头","剪刀","布")
user_input_item = items[user_input_index]
sys_input_index = random.randint (0,2)
sys_input_item = items[sys_input_index]

#逻辑处理
if user_input_item == sys_input_item:
    print ("平局")
elif (user_input_item, sys_input_item) in wins:
    print ("赢啦")
else:
    print ("输啦")
"""


"""
5·群讨论:
(1) == is的区别:
(2)谈论列表中的元素,如果根据条件批量删除.[1,2,34,5,5,6,79,0,8]删除大于3的数字

"""











"""=========================================================================="""

"""
    集合

"""

"""
#1,创建空集合
s01 = set()
#2,创建具有默认值的集合
s01 = {1,2,3,4}
print (type(s01))
#3,其他容器
s02 = set ("abcdace")
s02 = set ([1,7,56,8,7,8])
#集合-->其他容器
l02 = list (s02)
t02 = tuple(s02)
print (t02)
"""




"""=================================================================================================="""
"""
    能力提升      for循环嵌套

"""

"""
4行 内层循环索引
#
##
###
####

"""

"""
# 推理
# for c in range(1):
#     print("#",end="")
# print()
# for c in range(2):
#     print("#",end="")
# print()

for r in range(4):
    for c in range(r + 1): # 0 01 012 0123
        print("#",end="")
    print()   # 换行
"""


"""
4行 内层循环索引
####
 ###
  ##
   #

"""

"""
for r in range(4):
    for c in range(r):
        print(" ",end="")
    for c in range(4 - r):
        print("#",end="")
    print()
"""

"""
    列表中是否有相同元素
    [1,4,7,4,8,0,6]
    核心：所有元素间两两对比
    思想：
        取出第一个元素，与后边（1,2,3......）进行比较
        取出第二个元素，与后边（2,3,4......）进行比较
        取出第三个元素，与后边（3,4,5......）进行比较

        .......

"""

"""
list01 = [1,4,7,4,8,0,6]
# 推导
# for c in range(1,len(list01)):
#     if list01[0] == list01[c]:
#         print("有相同元素")
#
# for c in range(2,len(list01)):
#     if list01[1] == list01[c]:
#         print("有相同元素")

def elements_compare_in_pairs():
    res = False # 假设没有相同元素
    # 取出前几个元素
    for r in range(len(list01) - 1):
        # 与后边几个元素进行比较
        for c in range(r + 1,len(list01)):
            if list01[r] == list01[c]:
                res = True
                break   # 只能退出就近循环体
    if res:
        print("有相同元素")
    else:
        print("没有相同元素")

elements_compare_in_pairs()
"""










"""==========================================================================================================="""

"""
    练习

"""

"""
# 1
s1 = "Welcome to China"
# 请生成列表L为["Welcome" "to" "China"]
L = s1.split(" ")
print(L)
"""

"""
# 2
s2 = ['hello', 'tar', 'gz']
# 请生成字符串S为"hello.tar.gz"
S = ".".join(s2)
print(S)
"""

"""
# 3
# 请创建一个元组 T 为(20,30,40,50,40,30,20)
# 请计算t中元素30的个数

T = (20,30,40,50,40,30,20)
count = 0
for i in range(len(T)):
    if T[i] == 30:
        count += 1
print(count)
"""



"""
# 3
# 请创建一个字典D为{"name": "Bob","age" : 30}
#    请在字典D中创建新的键值对 "score" : 90
#    请把字典D中Bob的age改为: 25
#    如何查看字典D中"age"的值
#    #要求会用两种方法创建

D = {"name": "Bob","age" : 30}
D = dict({"name": "Bob","age" : 30})

D["score"] = 30
# print(D)
D["age"] = 25
print(D)
print("Bob的age:",D["age"])
"""













# def is_jishu(number):
#     return True if number % 2 == 1 else False

"""
def get_day_by_month(year,month):
    if month < 1 or month >12:
        return 0
    elif month == 2:
        if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
            return 29
        else:
            return 28
    elif month in (4,6,9,11):
        return 30
    else:
        return 31




# 优化
def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or year % 400 == 0

def get_day_by_month1(year,month):
    if month < 1 or month >12:
        return 0
    if month == 2:
        return 29 if is_leap_year(year) else 28
    if month in (4,6,9,11):
        return 30
    return 31   # 没进入3个if分支则返回31
"""


"""
# 得到列表中的最小值
def get_min(list_target):
    min = list_target[0]   # 假设第一个就是最小值
    for i in range(1,len(list_target)):
        if min > list_target[i]:
            min = list_target[i]
    print(min)
    return min

get_min([4,3,6,6,11])
"""


"""
#4.定义函数，判断字符串中存在的中文字符数量.·
#中文编码范围: 0x4E00         ord(字符)         0x9FA5

def get_chinese_char_count(str_target = ""):
    count = 0
    for i in str_target:
        if 0x4E00 <= ord(i) <= 0x9FA5:   # 其实进入这个if则count加1
            count += 1
    return count

chinese_char_count = get_chinese_char_count("dshfo你好见风使舵")
print(chinese_char_count)
"""




"""
from urllib.parse import urlencode,unquote,quote

str = {'name':'zhangshuaibao','age':16}
raw = '&'.join('%s=%s' % (k, v) for k, v in str.items())
print(raw,type(raw))


str = {'name':'汉子','age':16}
print(urlencode(str))

print(unquote("idNo=411402199606078519&address=%E6%B2%B3%E5%8D%97%E7%9C%81%E5%95%86%E4%B8%98%E5%B8%82%E6%A2%81%E5%9B%AD%E5%8C%BA&areaId=9324&cityId=9323&provinceId=9175&fullName=%E8%AE%B8%E5%87%AF&telephone=17610117329&id=4889074&identify=0&provinceName=%E6%B2%B3%E5%8D%97%E7%9C%81&cityName=%E5%95%86%E4%B8%98%E5%B8%82&areaName=%E6%A2%81%E5%9B%AD%E5%8C%BA&idCardFo=&idCardRe=&selected=1&isCustomer=0"))
print(quote("idNo=411402199606078519&address=河南省商丘市梁园区&areaId=9324&cityId=9323&provinceId=9175&fullName=许凯&telephone=17610117329&id=4889074&identify=0&provinceName=河南省&cityName=商丘市&areaName=梁园区&idCardFo=&idCardRe=&selected=1&isCustomer=0"))
"""




"""
# d02转换成d03
d02 = {'d':'zhhangshuaibao ','c':'dsfafda','a':'jfakdsjf','b':'1'}
d03 = {'a': 'jfakdsjf', 'b': '1', 'c': 'dsfafda', 'd': 'zhhangshuaibao '}

# print(ord('a') < ord('b'))

list01 = [(k,v) for k,v in d02.items()]
list02 = [(ord(k),v) for k,v in d02.items()]
list02.sort()

list_res = []
for k ,v in list02:
    # print(chr(k),v)
    list_res.append((chr(k),v))
print(list_res)
"""
































"""==========================================================================================================="""

"""
    方法

"""

"""
# 内存图见笔记

def fun01(num01):
    nun01 = 2
    print ("num01:" + str(num01))



number01 = 1
#调用方法
fun01 (number01)
print ("number01:" + str (number01))
"""



"""
# 内存图见笔记

def fun0l(a,b,c):
    a= 100
    # 修改的是列表对象，
    b[0]=200
    #修改的是栈帧中的变量
    c=300
num01= 1
list01 = [2]
list02 = [3]
fun0l(num01,list01,list02)
print (num01)#?  1
print(list01)#?  200
print(list02)#?  3
"""



"""
    方法作用域

    1. 作用域:变量起作用的范围。
    2. Local局部作用域:函数内部。
    3. Enclosing外部嵌套作用域:函数嵌套。
    4. Global全局作用域:模块(.py文件)内部。
    5. Builtin内置模块作用域: builtins.py文件。

    变量名的查找规则:
    由内到外: L->E->G->B.在访问变量时,先查找本地变量,然后是包裹此函数

"""

"""
#全局变量：当前.py文件内部都可访问
g01 = 100

def fun01():
    # #方法内部可以读取全局变量
    # #print (g01)
    # #局部变量:在方法内部创建的变量,只能在方法内部使用
    # l01 = 200
    # # 在方法内部创建了局部变量g01，没有修改全局变量g01
    # g01 = 300
    # print(g01)   # 300

    #如果需要在方法内部，修改全局变量
    global g01
    g01 = 300


fun01()
print(g01)  # 100
"""


"""
# 练习1 ： 统计一个方法的调用次数

count = 0

def fun01():
    global count
    count += 1
    pass

fun01()
fun01()
fun01()
print(count)
"""


"""
    实参传递方式
        位置传参
            --序列传参:可以运行时,根据某些逻辑决定传入的数据(列表)

        关键字传参
            --字典传参:可以运行时,根据某些逻辑决定传入的数据(字A形参传递方式默认（缺省）参数：让调用者可以有选择性的传递需要的信息


"""

"""
def fun0l(a, b, c):
    print (a)
    print (b)
    print (c)

#位置传参:实参与形象的位置依次对应
fun0l(1,2, 3)

#序列传参：用*将序列拆分后与形参的位置依次对应
fun0l (*[4,5,6])

# 关键字传参：实参根据形参的名称进行对应
fun0l (b=2,a=1,c=3)

#字典传参:用**将字典拆分后与形参的名字进行对应
fun0l (**{"b":20,"c":"cc","a":1.2})





#默认参数
def fun02 (a =0, b=0, c=0):   # 缺省参数必须自右至左依次存在 如：(a =0, b, c=0)会报错(a, b, c=0)或(a, b=0, c=0)就不会报错
    print (a)
    print (b)
    print(c)

#不写参数,使用默认值
fun02 ()
fun02(1)
fun02 (*[2,3])
fun02 (b = 20)
fun02 (** {"c":"cc"})
"""




"""
# 练习：定义函数。根据天/小时/分钟，计算总秒数

def get_total_seconds(day = 0,hour = 0,minutes = 0):
    return day * 24 * 60 * 60 + hour * 60 * 60 + minutes * 60


s01 = get_total_seconds(1,2)
s02 = get_total_seconds(hour = 2)
print(s02)



# 星号元祖传参

def add(*args):
    # 对于方法内部而言，就是元祖
    print(args)  # (1, 2, 3)
    sum = 0
    for i in args:
        sum += i
    print(sum)

add(1,2,3)
"""

"""
# 双星号字典形参
def fun5(**kwargs):
    # 对于方法内部而言，就是字典
    # 对于调用者而言，可以传递数量无限的关键字实参
    print(kwargs)

fun5(**{"name":"xukai","age":"24"})
fun5(a = 1 ,b = 2)


def fun6(*args,**kwargs):
    print(args)
    print(kwargs)

fun6(1,2, 3 , a = "xukai",b = 1.5)
"""


"""
    参数自左至右的顺序
    位置形参-->星号元组形参-->命名关键字形参-->双星号字典形参

"""
"""
# 参数自左至右的顺序
# 重要： 位置形参-->星号元组形参-->命名关键字形参-->双星号字典形参
# 如第一个参数是星号元组形参，后边都要用命名关键字形参
# 如一个参数是命名关键字形参，后边都要用双星号字典形参
def fun7(a,b,*args,c,d,**kwargs):
    print("a:",a)
    print("b:",b)
    print("args:",args)
    print("c:",c)
    print("d:",d)
    print("kwargs:",kwargs)

fun7(1,2,3,4,c = 5,d = 6,name = "xukai",age = 24)
"""


"""
    day07作业:
    1,自定义列表的排序函数
        温馨提示:返回值需要吗?

    2,自学字符串,列表,字典常用函数

    3,英文单词反转
       how are you -->you are how

    4.预习面向对象

    5,玩游戏2048

"""

"""
str = "how are you"
# print(str,sep="#")
list_str = str.split(" ")
print(list_str)
list_str = list_str[::-1]
print(list_str)
res_str = " ".join(list_str)
print(res_str)
"""

"""
# 内存图一定要牢记
g01=1
g_list=[1]
def fun02():
    print(g01)
    #没有修改变量g_list，修改的是指向的列表对象，所以不用global.
    g_list[0]=2
    # g_list = 1
    #修改全局变量,必须使用global关键字声明
    #global g01
    #g01=2

fun02()
print(g_list) #[2]
"""







"""
# day08 homework
# (2).请用关键字参数形式生成字典
# (3).s = set(d) 请问 s 的值是什么
def generate_dictionary(**kwargs):
    print(kwargs)


d = generate_dictionary(name = "Lucy",age = 20,number = 1)

# s = set(d)
# print(s)
"""





# 1.自定义列表排序
#    温馨提示：返回值需要吗    （内存图很重要）
"""
def sort(list_target):
    # 传入的是可变类型
    # 修改的是栈中的变量  还是  传入的对象----》》修改的是传入的对象
    for r in range(len(list_target) - 1):
        for c in range(r + 1 ,len(list_target)):
            if list_target[r] < list_target[c]:
                list_target[r] , list_target[c] = list_target[c] , list_target[r]
    # return list_target    # 因为修改的是传入的对象，所以没必要返回

# list01 = [2,4,4,5,6,7]
# res = sort(list01)
# print(res)

# 不需要返回 就可以这样写
list01 = [2,4,4,5,6,7]
sort(list01)
print(list01)

# 总结 变量如果是可变的，改完他就不需要return他了
"""
























"""+++++++++++++++++++++++++++++++++++++++++++++++++"""
    # """第一阶段至此结束"""

"""+++++++++++++++++++++++++++++++++++++++++++++++++"""



"""
    2048 核心算法

"""




"""
# 练习1 ： 定义函数，将元素0 移动到末尾
# [2,0,2,0]  --> [2,2,0,0]

def zero_to_end(list_target):
    # 将传入的列表中非零元素，拷贝到新列表中
    # list = []
    # for i in list_target:
    #     if i != 0:
    #         list.append(i)

    list = [i for i in list_target if i != 0]
    count_0 = list_target.count(0)
    list += [0] * count_0
    # print(list)
    # return list
    # 3,将新列表中元素赋值给传入的列表
    list_target[:] = list

list01 = [2,0,2,0]
zero_to_end(list01)
print(list01)
"""



"""
# 第二种方法
def zero_to_end(list_target):
    # 删除零元素   注意：列表里面删东西从后往前,因为如果从前往后删每删一个，元素都会往前跑，所以遍历的时候都漏掉
    #[2,0,2,0]-->[2,2]1
    count = 0
    list = []
    for i in list_target[::-1]:
        if i == 0:
            list_target.remove(0)
            count += 1
        else:
            list.append(i)
    list += [0] * count
    # return list
    list_target[:] = list


list01 = [2,0,2,0]
zero_to_end(list01)
print(list01)
"""




"""
# 第三种要和一下内容连用

# 第三种方法
def zero_to_end(list_target):
    #删除零元素#[2, 0, 2, 0] --> [2, 2]  --> [2, 2,0,0]
        # for i in range(4 - 1,-1,-1):
        # print(i)
    for i in range(len(list_target) -1, -1, -1):
        if list_target[i] == 0:
            del list_target[i]
            list_target.append(0)

list01 = [2, 0, 2, 0]
zero_to_end(list01)
print(list01,99999)



# 练习2：定义合并函数 1,2  2,3  3,4

# [2,2,0,0] ---> [4,0,0,0]
# [2,0,2,0] ---> [4,0,0,0]
# [2,0,0,2] ---> [4,0,0,0]
# [2,2,2,0] ---> [4,2,0,0]

def merge(list_target):
    zero_to_end(list_target)

    for i in range(len(list_target) - 1):
        # 相邻且相同
        if list_target[i] == list_target[i + 1]:
               list_target[i] += list_target[i + 1]
               list_target[i + 1] = 0

    zero_to_end(list_target) # [4,0,2,0] ---> [4,2,0,0]


list02 = [2,2,2,0]
merge(list02)
print(list02,2222)



#练习3:将二维列表，以表格的格式显示在控制台中
list01 =[
    [2,0,0,2],
    [2,2,0,0],
    [2,0,4,4],
    [4,0,0,2]
]

def print_map(map):
    for r in range(len(map)):
        for c in range(len(map[r])):
            print(map[r][c],end=" ")
        print()

print_map(list01)






#练习4：定义向左移动函数.

# [2,0,0,2]        [4,0,0,0]
# [2,2,0,0]        [4,0,0,0]
# [2,0,4,4]        [2,8,0,0]
# [4,0,0,2]        [4,2,0,0]


def move_lift(map):
    # 获取行数
    for r in range(len(map)):
        # 从左往右获取行
        # 交给merge合并处理
        merge(map[r])

move_lift(list01)
print(list01,1111111111)
print_map(list01)



def move_right(map):
    # 获取行数
    for r in range(len(map)):
        # 从右往左获取行
        # 交给merge进行合并
        list_merge = map[r][::-1]
        # print(list_merge,"000001")
        merge(list_merge)
        # 倒着往里放
        map[r][::-1] = list_merge


move_right(list01)
print(list01)


list000 = [2,3,4]
list001 = list000[:]
list000[:] = list001
print(list000)
print(list001)
"""



"""
    作业：
    #作业1：定义向上移动函数
    #从上往下获取列
    #交给合并方法还给原列

    #作业2：定义向下移动番数
    #从下往上获取列
    #交给合并方法还给原列



# 定义向上移动函数
# 从上往下获取列
# 交给合并方法
# 还给原列
# [0][0]
# [1][0]
# [2][0]
# [3][0]
def move_up(map):
    for c in range(4):  # 0  1  2  3
        list_merge = []
        for r in range(4):  # 0  1  2  3
            list_merge.append(map[r][c])

        merge(list_merge)

        # 将合并后的list_merge还原给原二维列表
        for r in range(4):
            map[r][c] = list_merge[r]

def move_down(map):
    for c in range(4):  # 0  1  2  3
        # 从上往下获取列，影城以为列表（从左到右）
        list_merge = []
        for r in range(3,-1,-1):  # 0  1  2  3
            list_merge.append(map[r][c])    # 断点研究一下和2114行的关系
        # 交给合并方法
        merge(list_merge)

        # 将合并后的list_merge还原给原二维列表
        for r in range(3,-1,-1):
            map[r][c] = list_merge[3 - r] # 0 1 2 3

"""







"""
    第二阶段

"""




"""面向对象"""

"""
类：       汽车                   狗:

        （启动、行驶、停止）        (叫、吃饭、摇尾巴)
对象      红旗H7 宝马X5            哈士奇 拉布拉多3


3,类是创建对象的"模板” 。
  --数据成员:名词类型的状态。
  --方法成员:动词类型的行为。

4,类与类行为不同,对象与对象数据不同。
  例如: (1)学生student是一个类,具有姓名,年龄等数据;
              具有学习study,工作work等行为.
              对象:悟空同学, 28岁。
                   八戒同学，29岁

"""


"""
    面向对象:考虑问题,从对象的角度出发
    类：模板       抽象
    对象： 具体

"""

"""
class Wife:

        # 老婆

    # 1.数据成员 姓名   年龄   性别  。。。
    def __init__(self,name,age,sex):
        # __init__方法作用： 接收信息，给到对象
        print(id(self))
        self.name = name
        self.age = age
        self.sex = sex



    # 2.方法成员 做饭。。。
    def cooking(self):
        print(self.name + "做饭")


# 创建对象（实例化）
# 调用 __init__(self,name,age,sex) 方法
w01 = Wife("丽丽",21,"女")
print(id(w01))
# 调用对象的方法
w01.cooking()




w02 = Wife("芳芳",20,"男")
print(id(w02))
# 调用对象的方法
w02.cooking()
"""


"""
class Student(object):
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def study(self):
        print(self.name + "学习")

    def work(self):
        print(self.name + "工作")

# s01 悟空对象的地址
s1 = Student("悟空",21)
# 通过对象地址，调用对象方法，会自动传递对象地址
s1.study()


s01 = Student ("悟空",28)
s02 = s01
s01.name = "孙悟空"
print(s02.name,66666666) #?
"""








"""
class Enemy:

        # 敌人

    def __init__(self,name,hp = 0,atk = 0.0,atk_speed = 0.0):
        self.name = name  # 敌人姓名
        self.hp = hp # 血量
        self.atk = atk  # 攻击力
        self.atk_speed = atk_speed  # 攻速

    def print_self(self):
        print(self.name,self.hp,self.atk,self.atk_speed)

"""

"""
#1,在控制台中输入3个敌人,存入列表
#2,将敌人列表输出(调用print_self)到控制台

list_enemy = []
for i in range(3):
    e01 = Enemy("许凯")
    e01.name = input("请输入姓名：")
    e01.hp = input("请输入血量：")
    e01.atk = input("请输入攻击力：")
    e01.atk_speed = input("请输入攻速：")
    list_enemy.append(e01)

print(list_enemy)


for item in list_enemy:
    item.print_self()
"""



"""
#练习3:定义函数,在敌人列表中,根据姓名查找敌人对象.
# 内存图见笔记
# e01 = Enemy("zs",100,10,2)
# e02 = Enemy("ls",200,5,3)
# e03 = Enemy("ww",300,30.5)
#
# list_enemy = [e01,e02,e03]



list01 = [
    Enemy("zs",100,10,2),
    Enemy("ls",200,5,3),
    Enemy("ww",300,30.5)
]

def get_enemy_for_name(list_enemy,name):
    # 遍历敌人列列表
    for item in list_enemy:
        # 如果有指定名称的敌人对象
        if item.name == name:
            # 则返回对象地址
            return item

re = get_enemy_for_name(list01,"zs")
if re != None:
    re.print_self()
else:
    print("没有找到")
"""




"""
#2.创建学生类
#     --数据:姓名,性别,年龄,成绩.
#     --行为: print_self()
#    画出学生列表内存图定义函数：
#                   -- 定义函数,在学生列表中,根据姓名查找学生对象
#                   -- 定义函数,在学生列表中,根据性别查我所有学生对象
#                   -- 查找年龄大于20，成绩大于60的所有学生对象

class Student:
    def __init__(self,name,sex,age,score):
        self.name = name
        self.sex = sex
        self.age = age
        self.score = score

    def print_self(self):
        print(self.name,self.sex,self.age,self.score)


list_stu = [
    Student("zs","男",95,10),
    Student("ls","女",25,60),
    Student("ww","男",58,30),
    Student("zl","女",65,50)
]

def get_student_for_name(list_target,name):
    for stu in list_target:
        if stu.name == name:
            return stu

# re01 = get_student_for_name(list_target = list_stu,name = "ww")
# re01.print_self()

def get_students_for_sex(list_target,sex):
    result = []
    for stu in list_target:
        if stu.sex == sex:
            result.append(stu)
            return result

# list_re02 = get_students_for_sex(list_target = list_stu,sex = "男")
# for i in list_re02:
#     i.print_self()



# result = []
# for stu in list_stu:
#     if stu.age > 20 and stu.score >60:
#         result.append(stu)

result = [stu for stu in list_stu if stu.age > 20 and stu.score >60]
"""










# list_levels = [1,1,2,2,0,2,2,3]
# def aa():
#     for i in range(len(list_levels)):
#
#         if list_levels[i] == 2 and list_levels[i + 1] == 2:
#             print(i + 1)
#             return True
#
# aa()
# del list_levels[:2]
# print(list_levels)


# list_res = [[{'id': 2, 'agent_no': '39018121', 'telephone': '2', 'up_id': 457702, 'customer_level': 1, 'nick_name': '丹丹'}], [{'id': 457702, 'agent_no': '83314727', 'telephone': '457702', 'up_id': 213112, 'customer_level': 1, 'nick_name': '朱凯迪'}], [{'id': 213112, 'agent_no': '75363', 'telephone': '213112', 'up_id': 180401, 'customer_level': 2, 'nick_name': '张瑞杰'}], [{'id': 180401, 'agent_no': '61678', 'telephone': '180401', 'up_id': 124242, 'customer_level': 3, 'nick_name': '吕婷婷'}], [{'id': 124242, 'agent_no': '29359', 'telephone': '124242', 'up_id': 56761, 'customer_level': 3, 'nick_name': '范范'}], [{'id': 56761, 'agent_no': '23870', 'telephone': '56761', 'up_id': 198166, 'customer_level': 3, 'nick_name': '双胞妈'}], [{'id': 198166, 'agent_no': '7178', 'telephone': '198166', 'up_id': 115796, 'customer_level': 3, 'nick_name': '陈小琳'}], [{'id': 115796, 'agent_no': '2538', 'telephone': '115796', 'up_id': 226306, 'customer_level': 3, 'nick_name': '可乐妈'}], [{'id': 226306, 'agent_no': '000', 'telephone': '13989707398', 'up_id': None, 'customer_level': 3, 'nick_name': '金蛋'}]]
# print( list_res[0][0]["id"],list_res[0][0]["agent_no"])



"""
class ICBC:

        # 工商银行

    # 类变量
    moneys = 999999

    @classmethod
    def print_total_moneys(cls):
        print(ICBC.moneys,cls.moneys)

    def __init__(self,name,money):
        # 实例变量
        self.name = name
        self.money = money
        # 从总行中，扣除当前支行的现金
        ICBC.moneys -= money


ic1 = ICBC("广渠门支行",100000)
print(ICBC.moneys)
ic2 = ICBC("磁器口支行",100000)
print(ICBC.moneys)

# 调用类方法，此时会自动传递类名进入方法
ICBC.print_total_moneys()
"""





"""
练习：对象计数器
            创居老婆类（名字。。。），随意实例化对象
             统计老婆数量（定义方法）

             画出内存图
"""

"""
class Wife(object):

    wife_count = 0

    @classmethod
    def wife_number(cls):
        return cls.wife_count

    def __init__(self,name = ""):
        self.name = name
        Wife.wife_count += 1


    def print_self(self):
        print(self.name)


w01 = Wife("ll")
w02 = Wife("yy")

print(Wife.wife_number())
"""






"""
class Vector2:
    # 向量
    # 00  01  02  03
    # 10  11  12  13
    # 20  21  22  23

    # 需求：在某个元素基础上，获取每个方向，指定数量的元素

    def __init__(self,x = 0,y = 0):
        self.x = x
        self.y = y

    # 实例方法
    def fun01(self):
        pass

    #类方法
    @classmethod
    def fun02(cls):
        pass

    #静态方法：得不到对象地址/也得不到类名
    @staticmethod
    def fun03():
        pass

    # 什么时候用到静态方法，就是做成函数也行，但是做成函数就不是面向对象了，而我又不想要对象（即传入self）************************
    # 将函数转移到类中,就是静态方法.
    @staticmethod
    def right():
        return Vector2(0,1)

    @staticmethod
    def up():
        return Vector2(-1,0)

    @staticmethod
    def lift():
        return Vector2(0,-1)

    @staticmethod
    def down():
        return Vector2(1,0)

    @staticmethod
    def right_up():
        return Vector2(-1,1)



    # 向量
    # 00  01  02  03
    # 10  11  12  13
    # 20  21  22  23

    # 需求：在某个元素基础上，获取每个方向，指定数量的元素



class DoubleListHelper:

    # 二维列表助手类
    #     定义：在开发过程中，所有对二维列表的常用操作（二位列表获取元素）

    # 在某个元素基础上，获取每个方向，指定数量的元素

    # 这个函数一不需要用到这个类的实例成员，二不需要用到这个类的类成员，所以据面向对象的思想放到类里做成静态方法
    @staticmethod
    def get_elenments(list_target,v_pos,v_dir,count):

        # :param list_target:
        # :param v_pos:   向量类型的位置
        # :param v_dir:   方向
        # :param count:   取得数量
        # :return:

        # 位置 10   ——》》 11     方向  01      不变的是0
        result = []
        for i in range(count):
            # 位置  +=  方向
            # 10    01  ——》》11
            # 11    01  ——》》12
            # 12    01  ——》》13
            v_pos.x += v_dir.x  # 1+0=不变
            v_pos.y += v_dir.y
            result.append(list_target[v_pos.x][v_pos.y])
        return result


list01 = [
    ["00","01","02","03"],
    ["10","11","12","13"],
    ["20","21","22","23"],
]

# #   10                   向右（行不变，列加一）    3   ——》11 12 13
# re01 = get_elenments(list01,Vector2(1,0),Vector2(0,1),3)
# print(re01)
#
# #   10                   向上（列不变，行加一）    2   ——》11 01
# re02 = get_elenments(list01,Vector2(2,1),Vector2(-1,0),2)
# print(re02)


# r03 = get_elenments(list01,Vector2(1,0),right(),3)
# print(r03)



re05 = DoubleListHelper.get_elenments(list01,Vector2(1,0),Vector2.right(),3)
print(re05)

re06 = DoubleListHelper.get_elenments(list01,Vector2(2,3),Vector2.lift(),2)
print(re06)
"""











"""**************************** 封装 ********************************"""


"""
    封装数据优势：
        1·符合人类思考方式
        2．将数据与对数据的操作封装起来
"""



# class Wife01:
#     def __init__(self,name,age):
#         self.name = name
#         # 缺点：外界可以随便赋值
#         self.age = age
#
#
#
#
# w01 = Wife01("芳芳",26)
# w02 = Wife01("铁锤",86)




"""
class Wife02:
    def __init__(self,name = "",age = 0):
        self.set_name(name)
        # self.__name = name   # 没有逻辑判断也生写，方便修改维护
        # 私有成员: 障眼法（解释器会将双下划线开头的变量改变）
        # self.__age = age  # 如果这么写，还是没有做到对数据限制，因为他通过构造函数执行了86的铁锤也娶回了家     下边改变写法
        self.set_age(age)

    def get_name(self):  # 读写
        return self.__name

    def set_name(self,value):
        self.__name = value

    def get_age(self):   # 读写
        return  self.__age

    def set_age(self,value):
        if 22 <= value <= 30:
            self.__age = value
        else:
            print("我不要")


w03 = Wife02("铁锤",86)
w03.set_age(1)

# 通过下划线 + 类名可以访问双下划线开头的数据
# print (w03._Wife02__age)
print(w03.__dict__)
"""

"""
class Wife02:
    def __init__(self,name = "",age = 0):
        self.name = name   # 调用@name.setter修饰的方法     self.name(name)
        self.age = age     # 调用@age.setter修饰的方法      self.age(age)

    @property    # 拦截读取变量的操作
    def name(self):  # 读写   # get_name()
        return self.__name

    @name.setter # 拦截写入变量的操作
    def name(self,value):
        self.__name = value

    @property
    def age(self):   # 读写   # set_name()
        return  self.__age

    @age.setter
    def age(self,value):
        if 22 <= value <= 30:
            self.__age = value
        else:
            self.__age = 0
            print("我不要")


w03 = Wife02("铁锤",87)
print(w03.name)
print(w03.age)

# 通过下划线 + 类名可以访问双下划线开头的数据
# print (w03._Wife02__age)
# print(w03.__dict__)
"""





"""
class Enemy:
    def __init__(self,name,atk,spend,hp):
        self.set_name(name)
        self.set_atk(atk)
        self.set_spend(spend)
        self.set_hp(hp)

    def get_name(self):
        return self.__name

    def set_name(self,value):
        self.name = value

    def get_atk(self):
        return self.__atk

    def set_atk(self,value):
        self.atk = value

    def get_spend(self):
        return self.__spend

    def set_spend(self,value):
        self.spend = value

    def get_hp(self):
        return self.__hp

    def set_hp(self,value):
        if 0<= value <= 100:
            self.hp = value
        else:
            print("血量不在范围内，赋值失败")


# e01 = Enemy("zs",200,50,200)
# print(e01.get_name(),e01.set_name(),e01.get_atk(),e01.set_atk(),e01.get_spend(),e01.set_spend(),e01.get_hp(),e01.set_hp())
"""






"""
# day09 作业：
# 1、消化2048 核心算法

# 2.以面向对象的思想，描述下列场景
#     提示： 对象与对象数据不同，类与类行为不同
#         张三   教  李四  学习python
#         李四   教  张三  玩游戏
#         张三   工作   挣了 8000元
#         李四   工作   挣了 3000元

# 3.创建技能类（技能名称，冷却时间，持续时间，攻击距离。。。。）
#     创建技能列表（技能对象的列表）
#       -- 查找名称是"降龙十八掌"的技能对象
#       -- 查找名称是持续时间大于10秒的所有技能对象
#       -- 查找攻击距离最远的技能对象
#       -- 按找持续时间，对列表升序排列（列表里面放的是技能对象）



class Person:
    def __init__(self,name):
        self.name = name
        self.__skills = []
        self.__total_money = 0

    # 拦截读取操作
    # 本质:创建property对象,name存储对象地址.
    # 注意：创建对象时,会指定读取方法
    # 相当于: name = property(get_name, None)
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self,value):
        self.__name = value

    @property
    def skills(self):
        # return self.__skills   # 返回可变对象地址,意味着类外仍然可以操作可变对象
        return self.__skills[:]  # 返回新的可变对象地址,意味着类外仍然可以操作  ,但不影响原对象
        # 备注:每次通过切片返回新对象,都会另外开辟空间创建新对象,占用过多内存

    @property
    def total_money(self):
        return self.__total_money

    def teach(self,person_other,str_skill):
        # person_other 的技能列表，增加str_skill
        person_other.__skills.append(str_skill)
        print(self.name,"教了",person_other.name,str_skill)

    def work(self,money):
        self.__total_money += money
        print(self.name,"工作挣了",money,"钱")


zs = Person("张三")
ls = Person("李四")
zs.teach(ls,"python")
ls.teach(zs,"玩游戏")
zs.work(8000)
ls.work(3000)
# 张三   教  李四  学习python

#***********************************************8
#zs.skills = []   这样是不行   但是zs.skills.append就能，为了绝对数据封装
#不能改#如果skills属性,返回的是__skills,那么仍然可以操作私有列表
#                           __skills[:],那么操作的是新列表






class skill:
    #__slots__限制当前类,创建的对象,只能具有的实例变量.
    # 4,优点:访止用户因错写属性的名称而发生程序错误。
    # 5,缺点:丧失了动态语言可以在运行时为对象添加变量的灵活

    __slots__ = ("__skill_name","__cooling_time")

    def __init__(self,skill_name,cooling_time,duration_time,striking_distance):
        self.skill_name = skill_name
        self.cooling_time = cooling_time
        self.duration_time = duration_time
        self.striking_distance = striking_distance

    @property
    def skill_name(self):
        return self.__skill_name

    @skill_name.setter
    def skill_name(self,value):
        self.__skill_name = value

    @property
    def cooling_time(self):
        return self.__cooling_time

    @cooling_time.setter
    def cooling_time(self,value):
        self.__cooling_time = value

    @property
    def duration_time(self):
        return self.__duration_time

    @duration_time.setter
    def duration_time(self,value):
        self.__duration_time = value

    @property
    def striking_distance(self):
        return self.__striking_distance

    @striking_distance.setter
    def striking_distance(self,value):
        self.__striking_distance = value


    def print_self(self):
        print(self.skill_name,self.cooling_time,self.duration_time,self.striking_distance)




# 3.创建技能类（技能名称，冷却时间，持续时间，攻击距离。。。。）
#     创建技能列表（技能对象的列表）
#       -- 查找名称是"降龙十八掌"的技能对象
#       -- 查找持续时间大于10秒的所有技能对象
#       -- 查找攻击距离最远的技能对象
#       -- 按找持续时间，对列表升序排列（列表里面放的是技能对象）

list_skill = [
    skill("降龙十八掌",5,20,30),
    skill("九阴白骨爪",3,10,60),
    skill("九阳神功",6,50,10)
]


for skill in list_skill:
    # print(skill)
    if skill.skill_name == "降龙十八掌":
        skill.print_self()






def get_skill_for_duration_time(list_target,duration_time = 10):
    result = []
    for skill in list_target:
        if skill.duration_time > duration_time:
            result.append(skill.skill_name)
    return result

res02 = get_skill_for_duration_time(list_skill)
print(res02)

# 查找攻击距离最远的技能对象
result = list_skill[0]
for i in range(1,len(list_skill)):
    if result.striking_distance < list_skill[i].striking_distance:
        result = list_skill[i]

print("result:",result.skill_name)
result.print_self()


# a = {"title":"接龙主题001","notice_close":"1","notice":"接龙公告001","image":"https://static5.zgmmtuan.com//mmt/image/20200822/ppnyKVrcF92tAfstfmzFroTi8w0_n0qU.png","solitaire_date":["2020-08-22 00:00:00","2020-09-30 00:00:00"],"start_time":"2020-08-22 00:00:00","end_time":"2020-09-30 00:00:00","product":[{"product_id":29363,"title":"商品主题001","intro":"商品主题001","sort":0,"poster":["https://static5.zgmmtuan.com//mmt/image/20200822/GO-Xr02NlLWMJnkKqHzdbCAGYAbyt8d4.png",""],"material":["https://static5.zgmmtuan.com//mmt/image/20200822/lR_PCZPkka9lPX-_7NlHUMzWBdESESzs.jpg"]},{"product_id":29362,"title":"商品主题002","intro":"商品主题002","sort":1,"poster":["https://static5.zgmmtuan.com//mmt/image/20200822/dJ7KRhMZpmjY9aCKKBBvJzQOpy_jEruH.jpg",""],"material":["https://static5.zgmmtuan.com//mmt/image/20200822/RGqjIxd-zpZt-NKHQCydd0k7iF26x67Y.png"]}],"is_bounty":"1","person_bounty":"1"}
# from pprint import pprint
# pprint(a)


# 按找持续时间，对列表升序排列（列表里面放的是技能对象
for r in range(len(list_skill) - 1):
    for c in range(r + 1,len(list_skill)):
        if list_skill[r].duration_time > list_skill[c].duration_time:
            list_skill[r], list_skill[c] = list_skill[c], list_skill[r]

# 请用调试,查看列表的取值。
print(list_skill)
"""





"""
    封装思想      重要！！！！！！！！！！！！
    （1）分而治之
        一个类中，一个方法，一条语句。
        --将一个大的需求分解为许多类,每个类处理一个独立的功能。
        --拆分好处:便于分工,便于复用,可扩展性强。
    （2）封装变化
        --变化的地方独立封装,避免影响其他类。
    （3）高内聚
        --类中各个方法都在完成一项任务(单一职责的类)
    （4）低耦合
        --类与类的关联性与依赖度要低(每个类独立),让一个类的改



"""



"""
    需求：老张开车去东北
    分而治之   --分解
    变化点
"""


# 老张开车去东北

"""
class Person:
    def __init__(self,name):
        self.name = name

    def go_to(self,type,str_pos):
        print(self.name)
        type.run(str_pos)

class Car:
    def run(self,str_pos):
        print("行驶到",str_pos)


p01 = Person("老张")
c01 = Car()
p01.go_to(c01,"东北")




# 练习  ：小明在招商银行取钱

class Person:
    def __init__(self,name,money = 0):
        self.name = name
        self.money = money


class Bank:
    def __init__(self,name,money):
        self.name = name
        self.total_money = money

    # 考虑:取钱逻辑,应该由银行决定.所以取钱方法,定义在了银行.
    def draw_money(self,person,value):
        if self.total_money >= value:
            self.total_money -= value
            person.money += value
            print("取钱成功")
        else:
            print("取钱失败")

p01 = Person("小明")
b01 = Bank("招商银行",100000)

b01.draw_money(p01,5000)
"""



"""
day10复习
封装:
1.封装获据：将多个基本类型复合为一个自定义类型
           --优势:复合人类的思考方式
                    体现对数据的操作方式

2.封装功能:对外提供必要的功能,隐藏实现细节.
           --模块化的编程思想

3,分而治之,  封装变化,  高内聚,       低耦合.
  分解       变化点    类职责单一     类与类的关系松散
"""


# day10作业
# 1,使用面向对象思想,写出下列场景:
#   玩家(攻击力)攻击敌人,敌人受伤(血量)后掉血,还可能死亡(播放动画）
#   敌人(攻击力)攻击力攻击玩家,玩家(血量)受伤后碎屏,还可能死亡（游戏结束）
#  程序调试,画出内存图.

# 2.完成学生管理器之-添加学生.

"""
class Person:
    def __init__(self,name,atk,hp):
        self.name = name
        self.atk = atk
        self.hp = hp

    def damage(self):  # value:掉血量
        if self.hp <= 0:
            print("game over")
            return False
        else:
            self.hp -= self.atk
            print("受伤啦,剩余血量：",self.hp)

    # def death(self):
    #     print(" ")

class Player(Person):
    def damage(self):
        super().damage()

class Enemy(Person):
    def damage(self):
        super().damage()

p01 = Player("玩家1",10,100)
e01 = Enemy("敌人1",60,50)
p01.damage()
e01.damage()
"""


"""
class Player:

        # 玩家类

    def __init__(self,atk,hp):
        self.atk = atk
        self.hp = hp

    def attack(self,enemy):
        print("打死你")
        enemy.damage(self.atk)

    def damage(self,value):
        self.hp -= value
        print("玩家受伤啦，屏幕碎了")
        if self.hp <= 0:
            self.__death()

    def __death(self):
        print("玩家死亡，游戏结束")

class Enemy:

        # 敌人类

    def __init__(self,hp,atk):
        self.hp = hp
        self.atk = atk

    def damage(self,value):
        self.hp -= value
        print("受伤啦！！！")
        if self.hp <= 0:
            self.__death()

    def attack(self,player):
        player.damage(self.atk)

    def __death(self):
        print("死了，播放动画")
"""













"""
    继承

"""

"""
class Pet:
    def eat(self):
        print("吃")

class Dog(Pet):
    def house_keeping(self):
        print("看家")

class Bird(Pet):
    def fly(self):
        print("飞")

p01 = Pet()
d01 = Dog()
b01 = Bird()



print(isinstance(p01,Pet))
print(isinstance(d01,Pet))

print(isinstance(p01,Dog))
"""



"""
class Person:
    def __init__ (self,name):
        self.name = name

class Student(Person):
    def __init__ (self,name,score):
        # 通过函数,调用父类方法
        super().__init__(name)
        self.score = score

class Teacher(Person):
    def __init__ (self,name,salary):
        super().__init__(name)
        self.salary = salary


s01 = Student ("zs", 100)
print (s01.score)
print (s01.name)

p02 = Person("ww")
# 内存图见收藏
"""







"""
    继承  -- 设计思想
    面向对象设计原则
    1.开闭原则
        开放                              关闭
        对扩展                            对修改
        允许增加新功能                     不允许修改以前的代码

    2.依赖倒置(抽象)
        使用抽象(父类),而不使用具体(子类)

"""


"""
# 老张开车去东北
# 变化：飞机、火车。。。

class Person:
    def __init__(self,name):
        self.name = name

    def go_to(self,type,str_pos):
        print(self.name)
        type.run(str_pos)

class Car:
    def run(self,str_pos):
        print("行驶到",str_pos)


p01 = Person("老张")
c01 = Car()
p01.go_to(c01,"东北")
"""



"""
#   改进  1.开闭原则   2.依赖倒置(抽象)

class Person:
    def __init__(self,name):
        self.name = name


    def go_to(self,vehicle,str_pos):
        # 写代码期间：
            # 使用的是交通工具的,而不是汽车,飞机等
            # 所以无需判断具体类型
        # 运行期间：
            # 传入具体的交通工具

        # 如果传入的对象,不是交通工具,则退出,
        if not isinstance(vehicle,Vehicle):
            print("传入的不是交通工具")  # 因为继承了，所以是交通工具
            return
        vehicle.transport(str_pos)

class Vehicle:
    # 交通工具
    def transport(self,str_pos):  # 运输的方法
        raise NotImplementedError
        # print("儿子们，必须有这个方法啊")


class Car(Vehicle):
    def transport(self,str_pos):
        print("行驶到",str_pos)

class Airplane(Vehicle):
    def transport(self,str_pos):
        print("飞到",str_pos)



p01 = Person("老张")
# p01.go_to("飞机","东北")
p01.go_to(Airplane(),"东北")
"""




"""
#练习:手雷爆炸了,可能伤害敌人,玩家,还有可能伤害未知事物(鸭子,树,房子).
#要求:如果增加了新的事物,手雷代码不变.

# 星号元祖传参

# def add(*args):
#     # 对于方法内部而言，就是元祖
#     print(args)  # (1, 2, 3)
#     sum = 0
#     for i in args:
#         sum += i
#     # print(sum)
#
# add(1,2,3)



# 只要是大家的共性，都可以往爹的身上提，人和其他实体都会受伤，爹就整个受伤的方法——受伤后都要减血，爹就整个减血的操作代码，只不过不同实体生命值不一样，其他子类继承其父的方法即可
class Grenade:
    # 手雷

    def __init__(self,atk):  # 攻击力
        self.atk = atk

    def explode(self,*args):      # 爆炸
        for item in args:
            # item.受伤()
            item.damage(self.atk)


class Damageable:
    # 可以受伤

    def __init__(self,hp):  # 生命值
        self.hp = hp

    def damage(self,value): # value:掉血量    扣多少血量，能受伤说明有生命hp
        # raise NotImplementedError()          # 约束子类必须有该方法
        self.hp -= value    # 写其他代码必须要把raise NotImplementedError()注释掉，他在方法中只能单独存在
        print(self.hp)


class Player(Damageable):
    def damage(self,value):
        # super().hp -= value
        super().damage(value)
        print("碎屏")

class Enemy(Damageable):
    def damage(self,value):
        # super().hp -= value
        super().damage(value)
        print("播放动画")


g01 = Grenade(10)
p02 = Player(100)
e03 = Enemy(50)

g01.explode(p02,e03)
"""








"""
    有若干个图形（圆形,矩形........）
    每种图形,都可以计算面积。
    定义图形管理器，记录所有图形,提供计算总面积的方法.
    要求:增加新的图形,不改变图形管理器代码,

    内存图见笔记

"""
"""
class GraphicsManager:
    def __init__(self):
        self.__graphics = []

    def add_graphics(self,g):   # g：图形对象
        if not isinstance(g,Graphics):
            print("传入的不是图形对象")  # 因为继承了Graphics，所以是图形
            return
        self.__graphics.append(g)

    def get_total_area(self):
        total_area = 0
        for item in self.__graphics:
            total_area += item.get_area()
        return total_area


class Graphics:        # 计算面积
    def get_area(self):  # 计算面积
        raise NotImplementedError()



class Circle(Graphics):
    def __init__(self,radius):
        self.radius = radius

    def get_area(self):
        return self.radius ** 2 * 3.14

class Rectangular(Graphics):
    def __init__(self,length,width):
        self.length = length
        self.width = width

    def get_area(self):
        return self.length * self.width


manager = GraphicsManager()
manager.add_graphics("ok")
manager.add_graphics(Rectangular(3,4))
manager.add_graphics(Circle(3))
print(manager.get_total_area())
"""




"""
day11作业:
1.  定义父类:武器,数据:攻击力,行为:购买,攻击
    定义子类:枪,数据:射速,行为:攻击
    定义子类：手雷,数据:爆炸范围,行为:攻击
    创建相应对象,调用相应方法.

2.  学生管理系统,实现修改学生信息.

3.  一家公司,有如下几种岗位:
    普通员工:底薪
    程序员：底薪+项目分红
    销售员：底薪+销售额
    定义员工管理器,记录所有员工,提供计算总薪资方法.
    要求：增加新岗位,员工管理器代码不做修改.1

"""

"""
class Weapon:
    def __init__(self,atk):
        self.atk = atk

    def buy(self):
        print("购买武器")

    def attack(self):
        raise NotImplementedError()

class Gun(Weapon):
    # 子类没有构造函数,则自动调用父类构造函数
    # 子类有构造函数,不再自动调用父类构造函数
    def __init__(self,atk,speed):
        super().__init__(atk)
        self.att_speed = speed

    def attack(self):
        print("枪攻击")

class Grenade(Weapon):
    def __init__(self,atk,explode_range):
        super().__init__(atk)
        self.explode_range = explode_range

    def attack(self):
        print("手雷攻击")



g01 = Gun(10,0.1)
g01.buy()
g01.attack()
"""











"""
3.  一家公司,有如下几种岗位:
    普通员工:底薪
    程序员：底薪+项目分红
    销售员：底薪+销售额
    定义员工管理器,记录所有员工,提供计算总薪资方法.
    要求：增加新岗位,员工管理器代码不做修改.
    体会:依赖倒置   见内存图
"""



class EmployeeManager:
    # 员工管理器
    def __init__(self):
        self.__all_employee = []

    def add_employee(self,employee):
        if not isinstance(employee,Employee):
            print("添加的不是员工对象")
            return
        self.__all_employee.append(employee)

    def get_total_salary(self):
        # 计算总薪资
        total_salary = 0
        for item in self.__all_employee:
            # 编码期间:item认为是员工
            # 运行期间:item实际是具体员工
            total_salary += item.get_salary()
        return total_salary



class Employee:
    # 员工  这个类的目的——计算薪资()
    # 作用:代表具体员工,隔离员工管理器与具体员工的变化.
    def __init__(self,name,base_salary):
        self.name = name
        self.base_salary = base_salary

    def get_salary(self):   # 从设计思想来说不一样也要想办法弄成一样的
        return self.base_salary


class Programmer(Employee):    # 程序员
    def __init__(self,name,base_salary,bonus):  # bonus分红
        super().__init__(name,base_salary)
        self.bonus = bonus

    def get_salary(self):
        # return self.base_salary + self.bonus
        # 扩展重写   不管从理论还是实践，都要用下边这种方法写
        return super().get_salary() + self.bonus


class Salesman(Employee):    # 销售员
    def __init__(self,name,base_salary,sale_value):  # bonus分红
        super().__init__(name,base_salary)
        self.sale_value = sale_value

    def get_salary(self):
        # return self.base_salary + self.sale_value
        return super().get_salary() + self.sale_value * 0.05


manager = EmployeeManager()
manager.add_employee(Employee("ww",4000))
manager.add_employee(Programmer("zz",2000,5000))
manager.add_employee(Salesman("ls",2000,2000))

print(manager.get_total_salary())







# 练习：
# lw = Salesman("老王",2000,500)
#  老王转岗
# 销售 -->  程序员



#重新创建新对象,替换引用,好比是开除"老王",招聘新"老王"
#要求;对象部分改变,而不是全部改变,   见图笔记(变化点是关键)

class Employee:
    # 员工类
    def __init__(self,name,job):
        self.name = name
        self.job = job

    def calculate_salary(self):   # 从设计思想来说不一样也要想办法弄成一样的
        if not isinstance(self.job,Job):
            return
        return self.job.get_salary()


class Job:
    # 岗位
    def __init__(self,base_salary):
        self.base_salary = base_salary

    def get_salary(self):   # 从设计思想来说不一样也要想办法弄成一样的
        return self.base_salary



class Programmer(Job):    # 程序员
    def __init__(self,base_salary,bonus):  # bonus分红
        super().__init__(base_salary)
        self.bonus = bonus

    def get_salary(self):
        # return self.base_salary + self.bonus
        # 扩展重写   不管从理论还是实践，都要用下边这种方法写
        return super().get_salary() + self.bonus



class Salesman(Job):    # 销售员
    def __init__(self,base_salary,sale_value):  # bonus分红
        super().__init__(base_salary)
        self.sale_value = sale_value

    def get_salary(self):
        # return self.base_salary + self.sale_value
        return super().get_salary() + self.sale_value * 0.05



lw = Employee("老王",Salesman(3000,500))
print(lw.calculate_salary())
#转岗
lw.job = Programmer(8000,10000)
print(lw.calculate_salary())














# customer_levels = [1,1,1,5] # [1,1,1,3,5]
# count = 0;count1 = 0
#
# for i in range(1,len(customer_levels)):
#     # 如果传入的是注册用户下单,他的上级情况 -- >[0,4,4,5]
#     if customer_levels[i] == 1:
#         count += 1
#         print("dddddddddd",count)
#         if count > 1:
#             continue
#
#         print(i,"LLsssssdsdsds",customer_levels.index(customer_levels[i]))
#         print(i - 1,"mmsssssssssssdsds",customer_levels.index(customer_levels[i - 1]))
#         print(22222222222,count)
#
#     elif customer_levels[i] == 5:
#         count1 += 1
#         if count1 > 1:
#             continue
#         print(customer_levels.index(customer_levels[i]),customer_levels.index(customer_levels[i - 1]))
#         print(11111111111,count1)


""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

"""
    设计原则

"""
res= {}


from pprint import pprint
def get_customer_id():
    # 获取当前用户当前商品可领取的优惠券（品券、类券、通券）
    customer_res =  requests.post(
              url="https://shop.uat.zgmmtuan.com/rapi/coupon/available",
              data ={
                  "product_id":'["29285"]',    # 变量
              },
              headers = {
                  "userToken":"d624e52d2cabfa5f68a90c7912014723",
                  "Content-Type":"application/x-www-form-urlencoded",
                  "platform":"android"
              },
              verify = False
    )
    result = customer_res.json()
    return result

pprint(get_customer_id())


random_number = random.randint(1,5)
print(random_number)

# def get_all_usable_unusable():
#     # 获取当前用户当前订单商品可以使用和不可使用的优惠券（品券、类券、通券、新人券）
#     customer_res =  requests.post(
#               url="https://shop.uat.zgmmtuan.com/rapi/coupon/choose-v2",
#               data={
#                   "cartIds":"7059233|7059234",     # 变量
#               },
#               headers = {
#                   "userToken":"d624e52d2cabfa5f68a90c7912014723",
#                   "Content-Type":"application/x-www-form-urlencoded",
#                   "platform":"android"
#               },
#               verify = False
#     )
#     result = customer_res.json()
#     return result
#
# print(get_all_usable_unusable())
#
# usable_coupons = get_all_usable_unusable()["data"]["usable"]["all"]       # 订单商品可用的券（四种券）
# unusable_coupons = get_all_usable_unusable()["data"]["unusable"]["all"]       # 订单商品不可用的券（四种券）
#
# list3 = []
# list4 = []
# list5 = []
# for item in range(len(usable_coupons)):
#     # print(type(coupons[item]["use_type"]),coupons[item]["coupon_id"])
#     if usable_coupons[item]["use_type"] == "0":
#         list3.append(usable_coupons[item]["coupon_id"])
#
#     if usable_coupons[item]["use_type"] == "1":
#         list4.append(usable_coupons[item]["coupon_id"])
#
#     if usable_coupons[item]["use_type"] == "2":
#         list5.append(usable_coupons[item]["coupon_id"])
# print("当前用户当前订单商品可使用的-->品券",len(list3),list3)
# print("当前用户当前订单商品可使用的-->类券",len(list4),list4)
# print("当前用户当前订单商品可使用的-->通券",len(list5),list5)
# print("*"*160)
#
# list6 = []
# list7 = []
# list8 = []
# for item in range(len(unusable_coupons)):
#     # print(type(coupons[item]["use_type"]),coupons[item]["coupon_id"])
#     if unusable_coupons[item]["use_type"] == "0":
#         list6.append(unusable_coupons[item]["coupon_id"])
#
#     if unusable_coupons[item]["use_type"] == "1":
#         list7.append(usable_coupons[item]["coupon_id"])
#
#     if unusable_coupons[item]["use_type"] == "2":
#         list8.append(unusable_coupons[item]["coupon_id"])
# print("当前用户当前订单商品不可使用的-->品券",len(list6),list6)
# print("当前用户当前订单商品不可使用的-->类券",len(list7),list7)
# print("当前用户当前订单商品不可使用的-->通券",len(list8),list8)


# a = {"use_type":"1","title":"类券李四","money":10,"category_excluded":0,"product_excluded":0,"with_amount":200,"valid_type":"1","valid_days":0,"valid_failure_days":1,"with_special":"0","quota":100,"limit":3,"expire_notify":0,"customer_level":["0"],"use_range":2,"category_category_id":[["1","5","244","337"],["1","5","246"],["1","5","248"],["1","5","254"],["1","5","258"],["1","16","22"],["1","16","23"],["1","16","25"],["1","16","36"],["1","17","27"],["1","17","28"],["1","17","29"],["1","17","271"],["1","18","33"],["1","18","259"],["1","18","260"],["1","18","261"],["1","18","262"],["1","19","37"],["1","19","263"],["1","19","264"],["1","19","265"],["1","20","39"],["1","20","41"],["1","20","266"],["1","21","42"],["1","21","43"],["1","21","45"],["1","21","46"],["1","21","267"],["1","101","108"],["1","101","109"]],"remarks":"哒哒哒哒哒哒多多多多多多多多多多多多多多多多多多多多多多多多多多多多多多"}
# from pprint import pprint
# pprint(a)




import requests,json
from pprint import pprint

def get_all_usable_unusable():
    # 获取当前用户当前订单商品可以使用和不可使用的优惠券（品券、类券、通券、新人券）
    customer_res =  requests.post(
              url="https://shop.uat.zgmmtuan.com/rapi/coupon/choose-v2",
              data={
                  "cartIds":"7059380|7059381",     # 变量
              },
              headers = {
                  "userToken":"d624e52d2cabfa5f68a90c7912014723",
                  "Content-Type":"application/x-www-form-urlencoded",
                  "platform":"android"
              },
              verify = False
    )
    result = customer_res.json()
    return result

usable_coupons = get_all_usable_unusable()["data"]["usable"]["all"]       # 订单商品可用的券（四种券）
print(usable_coupons)
unusable_coupons = get_all_usable_unusable()["data"]["unusable"]["all"]       # 订单商品不可用的券（四种券）
print(unusable_coupons)

list3 = []
list4 = []
list5 = []
for item in range(len(usable_coupons)):
    # print(type(coupons[item]["use_type"]),coupons[item]["coupon_id"])
    if usable_coupons[item]["use_type"] == "0":
        list3.append(usable_coupons[item]["coupon_id"])

    if usable_coupons[item]["use_type"] == "1":
        list4.append(usable_coupons[item]["coupon_id"])

    if usable_coupons[item]["use_type"] == "2":
        list5.append(usable_coupons[item]["coupon_id"])
print("当前用户当前订单商品可使用的-->品券" , str(len(list3)) , list3)
print("当前用户当前订单商品可使用的-->类券" , str(len(list4)) , list4)
print("当前用户当前订单商品可使用的-->通券" , str(len(list5)) , list5)
print("*"*160)

# list6 = []
# list7 = []
# list8 = []
# for item in range(len(unusable_coupons)):
#     # print(type(coupons[item]["use_type"]),coupons[item]["coupon_id"])
#     if unusable_coupons[item]["use_type"] == "0":
#         list6.append(unusable_coupons[item]["coupon_id"])
#
#     if unusable_coupons[item]["use_type"] == "1":
#         list7.append(usable_coupons[item]["coupon_id"])
#
#     if unusable_coupons[item]["use_type"] == "2":
#         list8.append(unusable_coupons[item]["coupon_id"])
# print("当前用户当前订单商品不可使用的-->品券" , str(len(list5)) , str(list5))
# print("当前用户当前订单商品不可使用的-->类券" , str(len(list7)) , str(list7))
# print("当前用户当前订单商品不可使用的-->通券" , str(len(list8)) , str(list8))




