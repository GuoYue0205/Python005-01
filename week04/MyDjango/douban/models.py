from django.db import models

# Create your models here.
class File_comment(models.Model):
    # id autofield(primary_key=true) Django会自动创建自增id，并设置为主键，不需要自己定义
    star = models.IntegerField()
    comment = models.CharField(max_length=400)
    comment_time = models.CharField(max_length=100)
