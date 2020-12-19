from django.shortcuts import render
from .models import File_comment
import requests
from lxml import etree
# Create your views here.


def film_evaluation(request):
    """
    docstring
    """
    # urls = tuple(
    #     f'https://movie.douban.com/subject/34894753/comments?start={ page * 20 }&limit=20&status=P&sort=new_score' for page in range(2))

    # for url in urls:
        # spider = Spider(url)
        # spider.get_data()

    url = 'https://movie.douban.com/subject/34894753/comments?start=0&limit=20&status=P&sort=new_score'
    spider = Spider(url)  
    spider.get_data()
    all_info = File_comment.objects.all()
    comments = File_comment.objects.filter(star__gt=3)

    return render(request, 'index.html', locals())


class Spider(object):
    def __init__(self, url):
        self.headers = {
            "User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'}
        self.url = url

    def get_data(self):
        try:
            response = requests.get(self.url, headers=self.headers)
            selector = etree.HTML(response.text)
            comment = selector.xpath('//span[@class="short"]/text()')
            time = selector.xpath(
                '//span[@class="comment-info"]/span[3]/text()')
            star = selector.xpath(
                '//span[@class="comment-info"]/span[2]/@title')
            for i in range(len(comment)):
                num = 0
                print(f'电影：{time[i]}')
                if star[i] == '力荐':
                    num = 5
                elif star[i] == '推荐':
                    num = 4
                elif star[i] == '还行':
                    num = 3
                elif star[i] == '较差':
                    num = 2
                elif star[i] == '很差':
                    num = 1
                else:
                    num = 0
                new_time = time[i].replace(" ", "")
                model = File_comment(
                    star=num, comment=comment[i], comment_time=new_time)
                model.save()
        except Exception as e:
            print(e)
