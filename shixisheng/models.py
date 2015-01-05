#coding:utf-8
from django.db import models

class Image(models.Model):
	img = models.ImageField(upload_to = './img')#找这个图片



class student(models.Model):
	name	= models.CharField(max_length=30)
	address = models.CharField(max_length=50)
	count	= models.IntegerField(default=0)	#访问量
	date	= models.DateField(auto_now=True)	#时间
	content = models.TextField()