#coding:utf-8
from django.http import HttpResponse
from django.shortcuts import render_to_response,redirect
import datetime
from django.template.response import TemplateResponse as TR
from shixisheng.models import student,Image

def home(request):
	d = {"ab":'Eecd',"date":str(datetime.datetime.now())}
	all = student.objects.all()
	#all = student.objects.filter(那么= “jike”)所有记录里取一条，条件过滤。
	d['all'] = all
	all_img = Image.objects.all()
	d['all_img'] = all_img
	return TR(request,"index.html",d)
	

def hell(request,abcd):
	#return HttpResponse("YUANJINYU" + abcd)
	d = {"ab":'Eecd',"date":str(datetime.datetime.now())}
	all = student.objects.all()
	#all = student.objects.filter(那么= “jike”)所有记录里取一条，条件过滤。
	d['all'] = all
	all_img = Image.objects.all()
	d['all_img'] = all_img
	return TR(request,"hello.html",d)
def new(request):
	print request.POST
	s = student()
	s.name    = request.POST['name']
	s.address = request.POST['address']
	s.content = request.POST['content']
	s.count   = 0
	s.save()
	return redirect("/hell/fdsarrerq")
def delete(request,id):
	s=student.objects.get(id=int(id))
	s.delete()
	return redirect("/hell/fdsarrerq")

def edit_view(request,id):
	s=student.objects.get(id=int(id))
	time = datetime.datetime.now()
	d = {"s":s,"t":time}
	return TR(request,"edit.html",d)



def edit(request,id):
	s = student.objects.get(id=int(id))
	s.name = request.POST['name']
	s.address = request.POST['address']
	s.save()
	return redirect("/hell/fdas")