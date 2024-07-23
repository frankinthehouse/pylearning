# -*- coding: UTF-8 -*-

# 打印九九乘法表
for i in range(1, 10):
        for j in range(1, i+1):
            # 打印语句中，大括号及其里面的字符 (称作格式化字段) 将会被 .format() 中的参数替换,注意有个点的
            print('{}x{}={}\t'.format(i, j, i*j), end='')  
        print()

LIST = ["A","B","C","D"]

print(LIST[0:2])

print(LIST[2:])