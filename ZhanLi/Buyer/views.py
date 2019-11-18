from django.shortcuts import render
from django.shortcuts import HttpResponseRedirect
from Buyer.models import User, Goods, ShopType

def login(request):
    hint = ''
    if request.method == 'POST':
        email = request.POST.get('email')
        pw = request.POST.get('pw')
        if email:
            user = User.objects.filter(email=email).first()
            if user:
                d_password = user.password
                if pw == d_password:
                    response = HttpResponseRedirect('/')
                    response.set_cookie('email', user.email)
                    response.set_cookie('user_id', user.id)
                    request.session['email'] = user.email
                    return response
                else:
                    hint = '密码不正确'
            else:
                hint = '用户名不存在'
        else:
            hint = '邮箱不能为空'
    return render(request, 'buyer/login.html', locals())

def register(request):
    hint = ''
    if request.method == 'POST':
        email = request.POST.get('email')
        pw = request.POST.get('pw')
        pwr = request.POST.get('pwr')
        if email:
            user = User.objects.filter(email=email).first()
            if not user:
                if pw == pwr:
                    u = User()
                    u.email = email
                    u.password = pw
                    u.save()
                    hint = '注册成功，请登录'
                else:
                    hint = '两次输入密码不一致'
            else:
                hint = '邮箱已被注册'
        else:
            hint = '邮箱不能为空'
    return render(request, 'buyer/register.html', locals())

def logo_out(request):
    url = request.META.get('HTTP_REFERER', '/Buyer/index/')
    response = HttpResponseRedirect(url)
    keys = request.COOKIES.keys()
    for key in keys:
        response.delete_cookie(key)
    del request.session['email']
    return response

def UserName(request):
    email = request.COOKIES.get('email')
    if email:
        u = User.objects.filter(email=email).first()
        if u.username:
            username = u.username
        else:
            username = email
    else:
        username = False
    return username

def index(request):
    username = UserName(request)

    shop_type = ShopType.objects.all()
    result = []
    for ty in shop_type:
        goods = ty.goods_set.order_by('g_hits')
        if len(goods) >= 8:
            goods = goods[:8]
            result.append({'type': ty, 'goods_list': goods})
        else:
            result.append({'type': ty, 'goods_list': goods})

    return render(request, 'buyer/index.html',locals())

def base(request):
    return render(request, 'buyer/base.html')

def goods_info(request,id):
    username = UserName(request)
    good = Goods.objects.get(id=int(id))

    info = good.g_introduction
    info = info.split(' ')
    return render(request, 'buyer/goods_info.html', locals())

def search(request):
    goods_type = request.GET.get('type')
    keywords = request.GET.get('keywords')
    if goods_type == 't':
        title = '查看更多'
        goods_list = Goods.objects.filter(t_id=int(keywords)).all()
    elif goods_type == 'k':
        title = '商品搜索'
        goods_list = Goods.objects.filter(g_name__contains=keywords)
    return render(request, 'buyer/search.html', locals())
# Create your views here.
