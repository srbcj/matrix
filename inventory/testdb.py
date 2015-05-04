#coding:utf-8

from django.http import HttpResponse
from inventory.models import Inventory

#
def appenddb(request):
    test1 = Inventory(name='www.amazon.com')
    test1.save()
    return HttpResponse("<p>The record be appended!</p>")


def visitdb(request):
    # 初始化
    response = ""
    response1 = ""

    # 通过objects这个模型管理器的all()获得所有数据行，相当于SQL中的SELECT * FROM
    list = Inventory.objects.all()

    # filter相当于SQL中的WHERE，可设置条件过滤结果
    # response2 = Inventory.objects.filter(id=1)

    # # 获取单个对象
    # response3 = Inventory.objects.get(id=1)

    # # 限制返回的数据 相当于 SQL 中的 OFFSET 0 LIMIT 2;
    # Inventory.objects.order_by('name')[0:2]

    #数据排序
    Inventory.objects.order_by("id")

    # 上面的方法可以连锁使用
    Inventory.objects.filter(name="w3cschool.cc").order_by("id")

    # 输出所有数据
    for var in list:
        response1 += var.name + " "
    response = response1
    return HttpResponse("<p>" + response + "</p>")


def updatedb(request):
    # 修改其中一个id=1的name字段，再save，相当于SQL中的UPDATE
    test1 = Inventory.objects.get(id=1)
    test1.name = 'w3cschool'
    test1.save()

    # 另外一种方式
    #Inventory.objects.filter(id=1).update(name='w3cschool菜鸟教程')

    # 修改所有的列
    # Inventory.objects.all().update(name='w3cschool菜鸟教程')

    return HttpResponse("<p>修改成功</p>")


def deldb(request):
    # 删除id=1的数据
    test1 = Inventory.objects.get(id=1)
    test1.delete()

    # 另外一种方式
    # Inventory.objects.filter(id=1).delete()

    # 删除所有数据
    # Inventory.objects.all().delete()

    return HttpResponse("<p>删除成功</p>")
