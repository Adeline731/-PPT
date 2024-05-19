#1.错误的示例 m,n=int(input().split())  int转化出来只能是一个数
m,n=map(int,input().split())
print(m+n)
#2.int(a,b)转成十进制数的时候a的类型是字符串，若a本来为字符串，不能用"a" 即使是数字，也不能直接加“”变为字符串
#3.int(input()) 输入时用整形
#4.-2**4 优先级是** 所以是-16
#5.print(0 and 'hello')  答案：是0  输出的是最后一个计算的值
#第三周练习题：print不是关键字  如果print事先被赋值了，那就会失去print作为输出函数的作用
#1.{0:.nf}前面数字代表后面format的编号，从0开始
#2.print("{:3.2f}".format(12.345))  输出长度超过三 不影响
#print("{:6.2f}".format(12.345))    前面用空格补上
#字符串转换成列表 list函数 若列表里是整形 可用sum求和 如果不是 则可以 for i in list,c+=int(i)
#a=input().split(" ") 创建的a是列表
#对于列表a.remove(元素）会改变a,但是对于字符串，不改变，必须重新赋值  a=input()  a=a.strip() 如果前面不加a=,那print(a)以后还是原来的
#from math import* 引用了math库中的所有  log(x[,base])
#a=input().split()  用于一行中输入字符串并可以用一个或多个空格
#format和round的区别是format一定会输出对应的小数点位数 但是round如果是0他会省略（精确不到那一位）
#list函数会把“”里面所有的内容全部拆解 包括[]，也会被拆解
#乘号连接成大序列
#asicc码大写在前面
#print(0xA + 0xB)  21
#i=j=[] 后续i的改变会影响j
#占位符也必须用顺序
#元组数据类型和int不能运算
#print函数（，）就代表有一个空格 但是如果是冒号外的空格不管用
#round函数运算完为浮点数
#bin输出来是有0b的
#print("programming".find("r",1)) 会从序号1开始  输出结果是1
#下面的语句的作用是读入"33 48"，赋值给变量s。
#s = input("33 48")  错误的
#s="abcd'12'34"
#print(s[-6:])  如果没说方向，不能是[-6：-1]  而且最后一个不输出
data=[[1]*3]*3
data[0][1]=45  # 单独data[0][1]是1，但因为乘三，一改都改 不管改后面还是改前面，都是一改都改
print(data[2][1])
#用循环可以避免
data=[[1,1,1] for i in range(3)]
data[0][1]=24
print(data)
#print(32.6//6-24//6)  注意浮点 1.0
#注意输出格式
a=34
b=23
print("{first}-{second}={0}".format(34-23,first=a,second=b))
#变量输出的是赋的值，不是字符串34-23会计算出来
##负数运算：得补码 运算  求正数值 加负号
#python乘法运算要加*号
#week5作业：
#用for遍历时遍历的是索引号，若用remove，后面的元素可能会因索引号改变而检索不到
#eval函数去除“”的外衣   所以它可以从str变成其他类型
#  若输入“”，eval后的类型还是str
num=input("请输入学生成绩：")
a=eval(num)
print(type(a))
#A 65 a 97
#程序1
lst=[1,2,3]
for i in lst:
    lst=lst+[1]
print(lst)   #只会执行三次

#程序2
lst=[1,2,3]
for i in lst:
    lst.append(1)
print(lst)    #会无限次执行
#  L=""1","2","3","4""
S="1,2,3,4"
L = S.split(sep=',')
print(L)
#无限执行
words=['cat','window', 'defenestrate']
for w in words:
    if len(w)>6:
        words.append(w)
print(words)
# set表示集合，不能包含重复元素
#seen.add(i)会执行
lst=[2,3,5,8,3,6,8]
seen=set()
lst1=[i for i in lst if i not in seen and not seen.add(i)]
print(lst1)
#if语句具有排他性 如果进入了一个if,与它同级地else还有elif就不会再执行
x,y,z=1,-1,1
if x > 0:
    if y > 0:
        print("x > 0 and y > 0")
elif z > 0:
    print("x < 0 and z > 0")
#n=x if x<y else n=y 不可以这样写
#"0"说明不是空的字符串，等于True 而且print("yes")本来错误，但因为false进不去，所以不会报错
if 0:
    print(yes)
if "0":
    print("yes")
#d["C"]=[3,4] 修改字典元素
#格式：print("balance is %d" % balance)
#break跳出的是循环 if不是循环，for是循环
#成员运算符就是测定对象是否在给定序列里
#continue不是跳出循环
#不只用for 用函数实现遍历
#循环语句后续语句是循环语句后面的语句 break跳出循环后就执行后续语句
#while循环中，必须要设置循环变量的初值和循环控制语句来控制循环条件，以避免死循环  不一定要设置控制条件
#改1 2也相应的改
list1=[1,43]
list2=list1
list1[0]=22
print(list2[0])
d2=d1.copy()  #d2不会随d1改变
d2=d1[:]  #也不会改变
#根本原因是id会不会变
#print('3//11//2018'.split('//'))
#答案为：["3","11","2018"]
#print('3//11//2018'.split('/'))
#答案为：["3","","11","","2018"]
#pop是弹出最后一个  它的返回值是弹出的那个数  注意要输入的是list还是被弹出的数字
#构建二维列表
students=[(3180102988,"褚好"),
          (3170102465,"王凯亮"),
          (3160104456,"李永"),
          (3171104169,"陈鑫"),
          (318400429,"徐杭诚")]

for row in students: #按行存取
    print(row[0],row[1])
print()

for id,name in students: #按行拆包存取
    print(id,name)
print()

for index in range(len(students)):  #按索引存取
    print(students[index][0],students[index][1])
#row row row与*3没有区别
row=[0]*3
data=[row,row,row]
data[2][2]=7
print(data[0][2])
#算a的时候，t还是1
t=1
t,a=2,t+1
print(a)
#字符串里如果输入”“，会当作一个字符
#*=后面的加号整体进行
#end=""在两个print之间就会有
#continue 跳过当前循环继续循环 i=2后，continue一直循环i不加1
i=1
s=0
while i<10:
    if i%2==0:
        continue
    else:
        s=s+i
    i=i+1
print(s)
#print(sum((1,3,5,7,9))/len((1,3,5,7,9)))  答案为5.0
print(sum((1,3,5,7,9)))  #sum()是函数整体（1，3，5，7，9）是元组整体
print(len((1,3,5,7,9)))   #len()可以在元组上使用
print(25/5)  #答案5.0
print(24/8)   #答案3.0  /运算出的是浮点数
#计算歌手得分
n=int(input())
a=input()
a=a.split()
a=[float(x) for x in a]
a.sort()
a=a[2:len(a)-2]
result=0
for i in a:
    result+=i
aver=result/(n-4)
print(f"aver={aver:.2f}")
#嵌套结构
a=[1,2,[3,4,[5,6],7],8]
b=3
def sum(n,j):
    sums=0
    if isinstance(n,int)and j==b:
        sums+=1
    if isinstance(n,list):
        for i in n:
            sums+=sum(i,j+1)  #运行了sum(i,j+1)得到了返回值sums,但是原函数并没有计算完毕 sums=sum(1,1)+sum(2,1)+sum([3,4,[5,6],7],8],1)+sum(8,1)
        #对于sum([3,4,[5,6],7],8],1)中sums又等于sum(3,2)等等 此时特别注意本函数中j已经被覆盖成1 j+1=2
    return sums
print(sum(a,0))
#函数逻辑：一层层剥去外壳
#创建方阵、表格的方式  不用急于创造方阵，拆成一行一行来计算
for i in range(0,n):
    line=list(input().split())
#yield函数 与return类似
def Fab(n):
    x,a,b=0,0,1
    if x<n:
        yield b
        a,b=b,a+b
        x=x+1
for x in Fab(5):
    print(n)
#{}避免空格
for i in range(1,10):
    for j in range(1,i+1):
        print(f"{i}×{j}={i*j}",end=" ")
    print()
print("","",sep="")  #也可以去除空格
#列表变为字符串  使用join列表里的数据类型必须为字符串  也可以使元组变为字符串
a=["1","2"]
b="".join(a)
print(b)
#一个函数只能有一个返回值  所以返回了一个值，相当于这个函数就结束运行了
def isPrime(num):
    num=int(num)
    for i in range(2,num):
        if num%i==0:
            return False
    if num!=1:
        return True
def PrimeSum(a,b):
    sum=0
    for i in range(a,b+1):
        if isPrime(i):
            sum+=i
    return sum
m,n=input().split()
m=int(m)
n=int(n)
print(PrimeSum(m,n))
#第七周pta
#1.lambda定义匿名函数 格式：g=lambda x,y,z:想要的运算结果 调用时g作为函数调用
#2.不一定return 如lambda
#3.map()会根据提供的函数对指定序列做映射。例如：map(function,指定序列)
def square(x):
    return x**2
print(list(map(square,[1,2,3,4,5]))) #加了list就可以输出新列表，不加不能呈现运算
#4.filter()过滤 filter(function,指定序列) 加list输出结果
#5.zip() 函数用于将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的列表。
a=[1,2,3]
b=[4,5,6]
print(list(zip(a,b)))
#结果：[(1,4),(2,5),(3,6)]
#6.enumerate()将可遍历对象组合为索引值
seq = ['one', 'two', 'three']
for i, element in enumerate(seq):
      print (i, element)
#结果：
#0 one
#1 two
#2 three
#7. object.sort(分类依据)  sort排序由小到大
t=[2,3,4,5,6]
t.sort()#返回值为none
t = [-8, 3, 6, -4]
a=t
a.sort()
print(a)
print(t)
#a=t的魔力
x  = [ 4 ,  6 ,  2 ,  1 ,  7 ,  9 ]
y  =  sorted (x)
print(y)  #[1, 2, 4, 6, 7, 9]
print(x)  #[4, 6, 2, 1, 7, 9]
#建立副本排序
#8.数据可视化
import plotly.graph_objects as go

fig = go.Figure(data=[go.Table(header=dict(values=['18岁', '未来']),
                               cells=dict(values=[["宋秉睿有无限可能"], ["宋秉睿每天都有好心情"]]))
                      ])

fig.show()
#9.reverse 是将列表倒置 但是不同于sorted(x)可以直接输出排序后，reversed需要加list
a=[1,2,3,4,5]
b=reversed(a)
print(list(b))
#10.python里有严格缩进要求，不是从属关系不能随便缩进
#11.return a,b返回的是元组 两个元组相加是合并
def n(a,b):
    a=a**3
    b=b**3
    return a,b
print(n(10,2))
print(n(5,1))
def m(x=n(10,2),y=n(5,1)):
    return x+y
print(m())
#12.print(函数)出来的是这个函数的返回值
#未解决：
import matplotlib as plt
plt.subplot(324)
plt.subplot(322)
plt.subplot(323)
plt.subplot(325)
#13.关于集合
#创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典；
#set 里边的元素是不可重复的，所以集合可用于元素去重（如：列表去重）；
#set 是无序的，支持并、交、差及对称差等数学运算， 但由于 set 不记录元素位置，因此不支持索引、分片等类序列的操作。
#set 不能嵌套，不能存可以改变的数据类型，如列表，字典；可以存数字、字符串、元组；
#set 和 dict 的唯一区别仅在于没有存储对应的 value，但是，set 的原理和 dict 一样，所以，同样不可以放入可变对象，因为无法判断两个可变对象是否相等，也就无法保证 set 内部“不会有重复元素”。
#python中set集合会自动排序
#列表转字符串
# 定义一个列表
my_list = ['apple', 'banana', 'orange']

# 使用join()函数将列表转换为字符串
my_string = ''.join(my_list)

# 打印结果
print(my_string)
a=[1,2,3,4,5]
a_string = ' '.join(a)
print(a_string)
#出现错误 因为列表中的元素不是字符串形式
#第九周作业
#1.i = 6  # 全局变量i

def f():
    def g():
        print(i)  # 这里尝试引用变量i
    g()
    i = 10  # 这行代码尝试在函数f的局部作用域中创建一个新的局部变量i
f()
#当在函数内部需要改变全局变量时，需要先声明
#2.创建空集合必须是set(),{}建立的是空字典
#3.简要的说可哈希的数据类型，即不可变的数据结构(字符串str、元组tuple、对象集objects)；同理，不可哈希的数据类型，即可变的数据结构 (集合set，列表list，字典dict)，集合元素只能是可哈希的数据类型
#元组，列表可以容纳任何数据类型









