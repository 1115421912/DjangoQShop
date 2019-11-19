import time
from django.shortcuts import render
from django.shortcuts import HttpResponseRedirect
from Buyer.models import User, Goods, ShopType, ShoppingCart, Retail

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

def loginValid(fun):
    def inner(request, *args, **kwargs):
        cookie_email = request.COOKIES.get('email')
        session_email = request.session.get('email')
        if cookie_email and session_email and cookie_email == session_email:
            return fun(request, *args, **kwargs)
        else:
            return HttpResponseRedirect('/Buyer/login')
    return inner

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
    username = UserName(request)

    goods_type = request.GET.get('type')
    keywords = request.GET.get('keywords')
    if goods_type == 't':
        title = '查看更多'
        goods_list = Goods.objects.filter(t_id=int(keywords)).all()
    elif goods_type == 'k':
        title = '商品搜索'
        goods_list = Goods.objects.filter(g_name__contains=keywords)
    return render(request, 'buyer/search.html', locals())

@loginValid
def success(request):
    email = request.COOKIES.get('email')
    username = UserName(request)

    success_type = request.GET.get('type')
    good_id = request.GET.get('good_id')
    good_num = request.GET.get('good_num')
    if success_type == 'a':
        try:
            good = Goods.objects.filter(id=int(good_id)).first()
            user = User.objects.filter(email=email).first()
            cart = ShoppingCart()
            add_good = ShoppingCart.objects.filter(g_id=good_id).first()
            if add_good:
                add_good.c_num += int(good_num)

                price_sum = int(good_num) * float(good.g_price)
                price_sum = round(price_sum, 2)
                # print('1:', price_sum)
                add_good.c_price_sum = price_sum + float(add_good.c_price_sum)

                add_good.save()
            else:
                r_id = good.r_id
                cart.r_id = r_id

                cart.g_id = good
                cart.u_id = user
                cart.c_num = int(good_num)
                cart.c_name = good.g_name
                cart.c_price = good.g_price
                cart.c_photo = good.g_photo
                cart.c_inventory = good.g_inventory
                cart.c_add_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

                price_sum = float(good.g_price) * int(good_num)
                price_sum = round(price_sum, 2)#保留两位小数，并四舍五入
                # print('2:', price_sum)
                cart.c_price_sum = price_sum

                cart.save()

            title = '添加购物车成功'
        except:
            title = '添加购物车失败'

    elif success_type == 'f':
        try:

            title = '付款成功'
        except:
            title = '付款失败'

    return render(request, 'buyer/success.html', locals())

@loginValid
def shopping_cart(request):
    username = UserName(request)
    email = request.COOKIES.get('email')
    user = User.objects.filter(email=email).first()
    goods = ShoppingCart.objects.filter(u_id=user).all()

    #对店家进行分类
    retail = []
    for i in goods:
        retail.append(i.r_id)
    retail = list(set(retail))#列表去重

    #让店家与其商品以键值对存储
    c = {}
    for n in retail:
        l = []
        for m in goods:
            if m.r_id == n:
                l.append(m)
        c[n.r_name] = l

    return render(request, 'buyer/shopcart.html', locals())

#订单编号：str(time.time() * 1000000)[:-2]
# Create your views here.
