# coding=utf-8
from django.shortcuts import render
from models import *
from django.core.paginator import Paginator


# Create your views here.

def index(request):
    glist = []
    tlist = TypeInfo.objects.all()
    for i in tlist:
        nlist = i.goodsinfo_set.order_by('-id')[0:3]
        clist = i.goodsinfo_set.order_by('-gclick')[0:4]
        glist.append({'type': i, 'nlist': nlist, 'clist': clist})
    context = {'title': '首页', 'glist': glist, 'hshow': '1'}

    return render(request, 'commodity/index.html', context)


def list(request, tid, index, pid):
    type = TypeInfo.objects.get(pk=int(tid))
    nlist = type.goodsinfo_set.order_by('-id')[0:2]

    desc = '1'
    sort = '-id'
    if pid == '2':
        desc = request.GET.get('desc', '1')
        if desc == '1':
            sort = '-gprice'
            # desc = '0'
        else:
            sort = 'gprice'
            # desc = '1'
    if pid == '3':
        sort = '-gclick'

    glist = type.goodsinfo_set.order_by(sort)
    paginator = Paginator(glist, 5)
    index1 = int(index)
    if index1 < 1:
        index1 = 1
    elif index1 > paginator.num_pages:
        index1 = paginator.num_pages
    page = paginator.page(index1)

    context = {'title': '商品列表', 'hshow': '1', 'type': type, 'nlist': nlist, 'page': page, 'pid': pid, 'desc': desc}
    return render(request, 'commodity/list.html', context)


def detail(request, id):
    goods = GoodsInfo.objects.get(pk=id)
    goods.gclick += 1
    goods.save()
    nlist = goods.gtype.goodsinfo_set.order_by('-id')[0:2]
    context = {'title': '商品详情', 'hshow': '1', 'goods': goods, 'nlist': nlist}
    # 获取response对象
    response = render(request, 'commodity/detail.html', context)
    # 获取cookies的键，（若该键不存在则默认值设为1），将其值拆分为数组，以逗号分隔
    record = request.COOKIES.get('record', '').split(',')
    print record
    if id in record:
        record.remove(id)
    record.insert(0, id)
    if len(record) > 6:
        record.pop()
        # 存储cookie，使用都好拼接成字符串，过期时间为7天
    response.set_cookie('record', ','.join(record), max_age=60 * 60 * 24 * 7)
    return response
