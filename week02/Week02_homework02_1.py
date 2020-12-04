# 使用 requests 库抓取知乎任意一个话题下排名前 15 条的答案内容 (如果对前端熟悉请抓取所有答案)，并将内容保存到本地的一个文件
# 什么值得买
import requests
from lxml import etree
import json
from time import sleep
def getInfoWithUrl(film_url):
    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'
    header = {'user-agent':user_agent}
    try:
        response = requests.get(film_url, headers=header)
        selector = etree.HTML(response.text)
        # 用户名
        user_name = selector.xpath('//a[@class="a_underline user_name"]/span[1]/text()')
        # 获取用户评论
        user_comment = selector.xpath('//p/span[@itemprop="description"]/text()')
        # zip方法 将两个列表进行一对一的关联  dict-将结果强制转换为字典类型
        film_info = dict(zip(user_name, user_comment))
        filename='comments.json'
        with open(filename,'w', encoding='utf-8') as file_obj:
            json.dump(film_info,file_obj)
    except Exception as e:
        print(e)

if __name__ == '__main__':
    urls = tuple(f'https://www.smzdm.com/p/27711661/p{page}/#comments' for page in range(1,4))
    for url in urls:
        getInfoWithUrl(url)
        # 为防止触发网站的防爬虫机制，每次请求间隔5秒钟
        sleep(5)
