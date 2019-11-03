from django.db import models

class User(models.Model):

    email = models.EmailField()
    password = models.CharField(max_length=18)
    username = models.CharField(max_length=32)
    age = models.CharField(max_length=4, null=True, blank=True)
    gender = models.CharField(max_length=4, null=True, blank=True)
    phone_number = models.CharField(max_length=11, null=True, blank=True)
    address = models.CharField(max_length=128, null=True, blank=True)
    picture = models.ImageField(upload_to='img', null=True, blank=True)

    user_type = models.CharField(max_length=4, null=True, blank=True)


class Shop(models.Model):

    c_title = models.CharField(max_length=128)
    c_price = models.CharField(max_length=8)
    c_weight = models.CharField(max_length=8)
    c_CO = models.CharField(max_length=128)#产地
    c_taste = models.CharField(max_length=32)#口味
    c_picture = models.ImageField()

    """
    0 零食
    1 生肉
    2 熟食
    3 坚果
    4 巧克力
    5 海鲜
    6 酒水
    7 水果
    8 茶叶
    9 餐具
    """
    c_classify = models.CharField(max_length=4)#商品分类

# Create your models here.
