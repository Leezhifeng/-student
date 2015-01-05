from django.db import STT
class student(STT.Model):
	name	= STT.CharField(max_length=30)
	address = STT.CharField(max_length=50)