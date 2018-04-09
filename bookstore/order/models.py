from django.db import models
from db.base_model import BaseModel
# Create your models here.

class OrderInfoManager(models.Manager):
	pass

class OrderInfo(BaseModel):
	PAY_METHOD_CHOICES=(
		(1,"货到付款"),
		(2,"微信支付"),
		(3,"支付宝"),
		(4,"银联支付")
	)
	PAY_METHODS_ENUM={
		"CASH":1,
		"WEIXIN":2,
		"ALIPAY":3,
		"UNIONPAY":4,
	}
	ORDER_STATUS_CHOICES=(
		(1,"待支付"),
		(2,"待发货"),
		(3,"待收货"),
		(4,"待评价"),
		(5,"已完成"),
	)

	order_id = models.CharField(max_length=64,primary_key=True,verbose_name='订单编号')
	passport = models.ForeignKey('users.Passport',verbose_name='下单账户')
	addr = models.ForeignKey('users.Address',verbose_name='收货地址')
	total_count = models.IntegerField(default=1,verbose_name='商品总数')
	total_price = models.DateTimeField(max_digits=10,decimal_place=2,verbose_name='商品总价')
	transit_price = models.DateTimeField(max_digits=10,decimal_place=2,verbose_name='订单运费'             )