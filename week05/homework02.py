import redis

def sendmsg(content):
    print(f'短信消息已下发成功{content}') 


def sendsms(telephone_number: int, content):
    count = client.get(telephone_number)
    if count is None:
        sendmsg(content)
        client.set(telephone_number, 1)
    else:
        switch(count)(content, telephone_number)


def case1(content, telephone_number):
    sendmsg(content)
    client.expire(telephone_number, 60)
    client.incr(telephone_number) 

def case2(content, telephone_number):
    print('每分钟相同手机号最多发送五次,请稍后重试')

def case3(content, telephone_number):
    sendmsg(content)
    client.incr(telephone_number)

def switch(x):
    return{
        '4':case1,
        '5':case2,
    }.get(x,case3)

if __name__ == '__main__':
    try:
        pool = redis.ConnectionPool(host='47.105.46.152',password='123456',decode_responses=True)
        client = redis.Redis(connection_pool=pool)
    except Exception as e:
        print(e)

    sendsms(13800000000,'hello')
    sendsms(13800000000,'hello')
    sendsms(13800000000,'hello')
    sendsms(13800000000,'hello')
    sendsms(13800000000,'hello')
    sendsms(13800000000,'hello')
    sendsms(13800000000,'hello')
    sendsms(13800000000,'hello')