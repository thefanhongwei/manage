from django.db import models
from django.contrib.auth.models import User
# 导入Django自带用户模块
# Create your models here.


def get_foo():
    return Test_one.objects.get_or_create(id=1)[0].id
# 文章
class Article(models.Model):


    name = models.CharField('姓名', max_length=10)
    gender = models.CharField('性别', max_length=10, blank=True)
    age = models.FloatField('年龄', max_length=10)
    created_time = models.DateTimeField('发布时间', auto_now_add=True)

    height=models.CharField('身高', max_length=10)
    weight=models.CharField('体重', max_length=10)
    waist=models.CharField('腰围', max_length=10)
    fat=models.FloatField('体脂',max_length=10)
    bmi=models.FloatField('BMI', max_length=10)
    spine=models.CharField('脊椎侧弯', max_length=10,default='正常')
    leg=models.CharField('腿型', max_length=10,default='正常')
    flexibility=models.FloatField('柔韧', max_length=10)
    coordinate=models.FloatField('协调', max_length=10)
    balance=models.FloatField('身体平衡', max_length=10)

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='录入者')
    modified_time = models.DateTimeField('修改时间', auto_now=True)

    class Meta:
        verbose_name = '体侧信息'
        verbose_name_plural = '学生管理'

    def __str__(self):
        return self.name