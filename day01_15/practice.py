import time
import os
import random
from random import randrange, randint, sample


# 跑马灯
def main():
    str = '北京欢迎你......'
    while True:
        os.system('cls')  # os.system('clear')
        print(str)
        time.sleep(0.2)
        temp = str[1:]
        temp2 = str[0]
        str = str[1:] + str[0]


# 设计一个函数产生指定长度的验证码，验证码由大小写字母和数字构成。
def generate_code(code_len=4):
    all_chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    code = ''
    for _ in range(code_len):
        index = random.randint(0, len(all_chars) - 1)
        code += all_chars[index]
    return code


#<editor-fold desc="折叠后要显示的内容">


# 设计一个函数返回给定文件名的后缀名。
def get_suffix(filename):
    index = filename.rfind('.')
    suffix = filename[(index + 1):]
    return suffix


def display(balls):
    """
    输出列表中的双色球号码
    """
    for index, ball in enumerate(balls):
        if index == len(balls) - 1:
            print('|', end=' ')
        print('%02d' % ball, end=' ')
    print()


def random_select():
    """
    随机选择一组号码
    """
    red_balls = [x for x in range(1, 34)]
    selected_balls = []
    selected_balls = sample(red_balls, 6)
    selected_balls.sort()
    selected_balls.append(randint(1, 16))
    return selected_balls


#</editor-fold>


#打印杨辉三角
def yanghui():
    num = int(input('请输入行数:'))
    yh = [[]] * num
    for row in range(len(yh)):
        yh[row] = [None] * (row + 1)
        for col in range(len(yh[row])):
            if col == 0 or col == row:
                yh[row][col] = 1
            else:
                yh[row][col] = yh[row - 1][col - 1] + yh[row - 1][col]

            print(yh[row][col], end='\t')
        print()


if __name__ == '__main__':
    #main()
    #print(f'验证码:{generate_code()}')
    #print('后缀是: '+get_suffix(r'C:\test.log'))
    yanghui()
