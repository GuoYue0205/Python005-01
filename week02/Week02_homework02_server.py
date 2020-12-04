import socket
import struct
HOST = 'localhost'  # 设置主机名称
PORT = 10000  # 设置端口号


def echo_server():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 将对象绑定到指定的主机和端口上
    s.bind((HOST, PORT))
    # 只接受一个连接
    s.listen(1)
    # accept表示接收用户端的连接
    conn, addr = s.accept()
    print(addr)
    while True:
        fileinfo_size = struct.calcsize('128sl')
        buf = conn.recv(fileinfo_size)
        if buf:
            filename, filesize = struct.unpack('128sl', buf)
            fp = open('/Users/guoyue/' + str(filename), 'wb')
            recvd_size = 0 
            while not recvd_size == filesize:
                if filesize - recvd_size > 1024:
                    data = conn.recv(1024)
                    recvd_size += len(data)
                else:
                    data = conn.recv(filesize - recvd_size)
                    recvd_size = filesize
                fp.write(data)
            fp.close()
        s.close()


if __name__ == '__main__':
    echo_server()
