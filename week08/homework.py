# 作业一：
# 区分以下类型哪些是容器序列哪些是扁平序列，哪些是可变序列哪些是不可变序列：
# 容器序列----可以存放不同类型的数据。即可以存放任意类型对象的引用。
# 扁平序列----只能容纳一种类型。也就是说其存放的是值而不是引用。
# list  容器序列 可变序列
# tuple  容器序列 不可变序列
# str  扁平序列 不可变序列
# dict  容器序列  可变序列
# collections.deque  容器序列  可变序列

# 作业二：
# 自定义一个 python 函数，实现 map() 函数的功能。
def map(func,*iterators):
    try:
        i = 0
        while True:
            yield func(*[j[i] for j in iterators])
            i+=1
    except Exception as e:
        print(e)
        
# 作业三：
# 实现一个 @timer 装饰器，记录函数的运行时间，注意需要考虑函数可能会接收不定长参数。
import time
def timer(func): 
    def run(*args,**kwargs):
        starttime = time.time()
        ret = func(*args,**kwargs)
        endtime = time.time()
        print(f'函数运行时间：{endtime-starttime}')
        return ret
    return run

@timer
def test():
    time.sleep(1)

test()