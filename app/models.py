# -*- encoding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Trading(models.Model):
    GU_CODE = models.IntegerField(verbose_name='지역코드')
    DONG_NAME = models.CharField(max_length=256, verbose_name='법정동')
    TRADE_DATE = models.CharField(max_length=32, verbose_name='거래일')
    APT_NAME = models.CharField(max_length=256, verbose_name='아파트')
    JI_NUM = models.CharField(max_length=64, verbose_name='지번') 
    AREA_SIZE = models.FloatField(verbose_name='전용면적') 
    FLOOR = models.IntegerField(verbose_name='층')
    BUILT_YEAR = models.IntegerField(verbose_name='건축년도')
    TRADE_PRICE = models.IntegerField(verbose_name='거래금액')
    TRADE_MONTH = models.IntegerField(verbose_name='거래월')


