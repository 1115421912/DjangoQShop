from django.db import models

#创建表时自动创建id，自增、主键
class User(models.Model):

    email = models.EmailField()#邮箱
    password = models.CharField(max_length=18)#密码
    username = models.CharField(max_length=32, null=True, blank=True) #昵称
    age = models.CharField(max_length=4, null=True, blank=True)
    gender = models.CharField(max_length=4, null=True, blank=True)
    phone_number = models.CharField(max_length=11, null=True, blank=True)#手机号
    picture = models.ImageField(upload_to='img', null=True, blank=True)

    user_type = models.CharField(max_length=4, null=True, blank=True)#默认 普通用户0 商家用户 1 管理员 2

# #收获地址
class HarvestAddress(models.Model):
    """
    用户id
	姓名（必填）
	手机号（必填）
	地址（必填）
	邮箱（选填）
	是否设置为默认地址
    """
    name = models.CharField(max_length=32)
    gender = models.CharField(max_length=4, null=True, blank=True)
    phone_number = models.CharField(max_length=32)
    address = models.CharField(max_length=128)
    email = models.EmailField(null=True, blank=True)
    default = models.CharField(max_length=4, default=0)#是否默认 1是表示默认

#品牌/店家
class Retail(models.Model):
    """
    品牌id
    名称
    介绍
    logo
    """
    r_name = models.CharField(max_length=32)
    r_introduction = models.CharField(max_length=128)#介绍
    r_picture = models.ImageField(upload_to='img', null=True, blank=True)

#分类
class ShopType(models.Model):
    """
    糕点点心
    饼干膨化
    熟肉卤味
    豆干辣条
    坚果炒货
    果干蜜饯
    巧克力果冻
    鱿鱼海味
    茶水冲泡
    酒水饮料
      """
    t_classify = models.CharField(max_length=32)  # 商品分类
    t_picture = models.ImageField(upload_to='img')
    r_id = models.ForeignKey('Retail', on_delete=models.CASCADE)  # 品牌id

# 商品
class Goods(models.Model):
    """
    商品id
    类别id
    品牌id
    名称
    标题
    详情
    点击量
    图片路径
    原价
    原价
    库存
    是否热门
    是否新品
    """
    t_id = models.ForeignKey("ShopType",on_delete=models.CASCADE)#类别id
    r_id = models.ForeignKey('Retail', on_delete=models.CASCADE)#品牌id
    g_name = models.CharField(max_length=32)
    g_title = models.CharField(max_length=128)
    g_introduction = models.CharField(max_length=128)  # 详情 （产地，包装，毛重，保质期）

    g_price = models.CharField(max_length=12)#售价
    g_original_price = models.CharField(max_length=12)#原价
    g_inventory = models.IntegerField()#库存
    g_photo = models.ImageField(upload_to='images')

    g_hits = models.IntegerField(null=True, blank=True)  # 点击量
    Whether_the_hot = models.CharField(max_length=4,default=0)#是否热门 0，不是热门
    Whether_the_new = models.CharField(max_length=4,default=0)#是否新品 0，不是新品

#购物车
class ShoppingCart(models.Model):
    """
    用户id
    商品id
    店家id
    商品名称
    商品价格
    商品数量
    商品图片
    总价
    添加时间
    是否有货（库存）
    """
    u_id = models.ForeignKey('User', on_delete=models.CASCADE)
    g_id = models.ForeignKey('Goods', on_delete=models.CASCADE)
    r_id = models.ForeignKey('Retail', on_delete=models.CASCADE)
    c_name = models.CharField(max_length=32)
    c_price = models.CharField(max_length=12)
    c_num = models.IntegerField()
    c_photo = models.ImageField(upload_to='images')
    c_price_sum = models.CharField(max_length=32)
    c_add_time = models.DateTimeField()
    c_inventory = models.IntegerField()#库存


# #订单
# class order_for_goods(models.Model):
#     """
#     用户id
#     订单编号
#     订单包含的商品id
#     订单总价
#     支付状态
#     收获人信息
#     支付方式
#     订单时间创建时间
#     订单完成时间
#     """
#     u_id = models.ForeignKey('User', on_delete=models.CASCADE)
#     order_reference = models.CharField(32)

#
# #评价
# class Assessment(models.Model):
#     """
#   评价id
# 	用户id
# 	订单编号
# 	评价状况
# 	评价
# 	评价等级
#     """
#     pass           




# Create your models here.
