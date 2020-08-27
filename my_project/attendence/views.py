from django.core.paginator import Paginator
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
import time
# Create your views here.
from attendence.models import Attendence
from user.models import User


def view_show(request):
    lists = Attendence.objects.all()
    paginator = Paginator(lists, 10)
    cur_page = request.GET.get('page', 1)  # 得到默认的当前页
    page = paginator.page(cur_page)
    return render(request,'attendence/view_show.html',locals())

def add(request):
    if request.method == 'GET':
        return render(request, 'attendence/add_attendence.html')
    if request.method == 'POST':
        username = request.POST.get('username')
        try:
            student = User.objects.get(username=username) #获取主表的数据
        except Exception as e:
            return HttpResponse('此学生不存在')
        sign_hour = time.localtime().tm_hour
        sign_min = time.localtime().tm_min
        if sign_hour<=8 and sign_min < 30:
            is_on_time = '正常'
        else:
            is_on_time = '迟到'
        Attendence.objects.create(student=student,is_onTime = is_on_time)
        return HttpResponseRedirect('view_show')

def search(request):
    if request.method == 'GET':
        return render(request, 'attendence/results.html')
    if request.method == 'POST':
        username = request.POST.get('username')
        error_msg = ''
        if not username:
            error_msg = '请输入关键词'
            return HttpResponse(error_msg)
        try:
            student = User.objects.get(username=username)  # 获取主表的数据
        except Exception as e:
            return HttpResponse('此学生不存在')
        lists=Attendence.objects.filter(student=student)
        # paginator = Paginator(lists, 5)
        # cur_page = request.GET.get('page', 1)  # 得到默认的当前页
        # page = paginator.page(cur_page)
        return render(request, 'attendence/results.html',locals())
