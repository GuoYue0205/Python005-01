import socket
import sys
import struct
import os
HOST = 'localhost'  # 设置主机名称
PORT = 10000  # 设置端口号


def echo_client():
    '''客户端'''
    try:
        # 第一个参数表示icp4协议 第二个参数表示TCP协议
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 连接到指定服务器与端口
        s.connect((HOST, PORT))
    except Exception as e:
        print(f'客户端连接错误{e}')
        sys.exit(1)
    file = '王座骑士.jpg'
    # 定义文件头信息，包含文件名和文件大小
    fhead = struct.pack('128sl', os.path.basename(file).encode('utf-8'), os.stat(file).st_size)
    # 发送文件名称与文件大小
    s.send(fhead)
    fp = open(file, 'rb')
    while True:
        data = fp.read(1024)
        if not data:
            break
        s.send(data)
    s.close()


if __name__ == '__main__':
    echo_client()