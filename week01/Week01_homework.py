import logging
import time
import os


def log():
    # 获取当前时间
    nowDay = time.strftime('%Y-%m-%d')
    # 拼接文件路径
    filePath = '/var/log/python-%s' % (nowDay)
    # 判断当前路径是否存在
    if not os.path.exists(filePath):
        # 不存在则创建
        os.makedirs(filePath)
    # 切换操作目录
    os.chdir(filePath)
    # 日志格式
    logging.basicConfig(filename='xxxxx.log',
                        level=logging.WARNING,
                        datefmt='%Y-%m-%d %H:%M:%S',
                        format='%(asctime)s %(message)s')
    logging.warning('函数被调用了')


if __name__ == '__main__':
    log()
