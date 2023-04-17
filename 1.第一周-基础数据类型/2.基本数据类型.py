# python中基本数据类型
"""
常量：在程序运行过程中不发生改变的量，Python不用常量命名
变量：在程序运行过程中会发生改变，可以重新赋值
    在常量中有以下数据类型：
        1. 数字型
           整形(int)：就是整数，包括正整数，负整数，0
               十进制：0-9，-1，0，+1
               八进制：0-7，满8进一，0o100
               十六进制：0-f，满16进一，0o100
           浮点型(float)：就是小数，带有小数点的数
        2. 字符型
             字符串(str)：就是带引号的一句话，单双引号没有区别
             "张飞"    "诸葛孔明"   "54863389@qq.com"  "100" 都是字符串
             注意：多行注释也是字符串，是长字符串
        3. 布尔型
             布尔(bool)：用于表达结果，有两个值：
                True：真，在数值上等于1，表示结果成立
                Flase：假，在数值上等于0，表示结果不成立
"""
# = : 赋值符号，给变量赋值，将右边的赋值给左边变量名
num = 100  # 是变量
name = "王俊凯"
# type()：带括号的是函数，查看数据的数据类型
# 整形数据
print(998)
print(type(998))   # <class 'int'>
# 八进制数据：7+1 = 10
print(0o100)
# 十六进制数据：f + 1 = 10
print(0x100)
# 浮点型数据
print(5.0123)
print(type(5.0123))      # <class 'float'>
print(2.0)
print(type(2.0))
# 字符串数据
print("祝有情人终成眷属！")
print(type("TOM"))  # <class ' str'>
print("15136282191")
print(type("15136282191"))
print("""多行注释也是字符串""")
print("""
孔子曰：有朋自远方来，不亦说乎！
""")


# 布尔型数据
print(True, False)
print(type(True))   # <class 'bool'>
# 表达式：如 a < b
print(1 < 2)  # < ：判断左边是否小于右边
print(10 > 11)  #
# == ：判断左右两边是否相等
print(True==1)
