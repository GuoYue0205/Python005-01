import redis

def conuter(video_id: int):
    result = client.get(video_id)
    if not result:
        client.set(video_id, 1)
        return 1
    else:
        count_number = client.incr(video_id)
        return count_number
    

if __name__ == '__main__':
    try:
        pool = redis.ConnectionPool(host='47.105.46.152',password='123456')
        client = redis.Redis(connection_pool=pool)
    except Exception as e:
        print(e)
    
    print(conuter(1001)) # 返回 1
    print(conuter(1001)) # 返回 2
    print(conuter(1002)) # 返回 1
    print(conuter(1001)) # 返回 3
    print(conuter(1002)) # 返回 2