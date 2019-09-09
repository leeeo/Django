from django.db import models

# Create your models here.


class Eojinuser(models.Model):
    email = models.EmailField(verbose_name='이메일')
    password = models.CharField(max_length=64, verbose_name='비밀번호')
    register_date = models.DateTimeField(
        auto_now_add=True, verbose_name='등록날짜')

    class Meta:
        db_table = 'eojin_user'
        verbose_name = '사용자'
        verbose_name_plural = '사용자'
