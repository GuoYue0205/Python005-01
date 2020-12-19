from django.db import models

# Create your models here.
# 每一个模型都是一个Python的类，这些类继承django.db.models.Model
# 模型的每一个属性都是表的一个字段

class Type(models.Model):
    # id autofield(primary_key=true) Django会自动创建自增id，并设置为主键，不需要自己定义
    typename = models.CharField(max_length=30)


# 定义完成类之后 需要去执行 python3 manage.py makemigrations
# python3 manage.py migrate

