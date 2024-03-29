from django.db import models

# Create your models here.


class Order(models.Model):
    eojinuser = models.ForeignKey(
        'eojinuser.Eojinuser', on_delete=models.CASCADE, verbose_name='사용자')
    product = models.ForeignKey(
        'product.Product', on_delete=models.CASCADE, verbose_name='상품')
    quantity = models.IntegerField(verbose_name='수량')
    register_date = models.DateTimeField(
        auto_now_add=True, verbose_name='등록날짜')

    def __str__(self):
        return self.eojinuser + ' ' + self.product

    class Meta:
        db_table = 'eojin_order'
        verbose_name = '주문'
        verbose_name_plural = '주문'
