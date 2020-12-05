import time

def main():
    try:
        f = open('E:\\data\\tmp\\新建文本文档.txt', 'r', encoding='utf-8')
        print(f.read())
    except FileNotFoundError:
        print('文件未找到')
    except LookupError:
        print('未知编码')
    except UnicodeDecodeError:
        print('读取文件时解码错误!')
    finally:
        if f:
            f.close()

def readlines():
    # 一次性读取整个文件内容
    with open('E:\\data\\tmp\\新建文本文档.txt', 'r', encoding='utf-8') as f:
        print(f.read())

    # 通过for-in循环逐行读取
    with open('E:\\data\\tmp\\新建文本文档.txt', mode='r',encoding='utf-8') as f:
        for line in f:
            print(line, end='')
            time.sleep(0.5)
    print()

    # 读取文件按行读取到列表中
    with open('E:\\data\\tmp\\新建文本文档.txt',encoding='utf-8') as f:
        lines = f.readlines()
    print(lines)

if __name__ == '__main__':
    readlines()