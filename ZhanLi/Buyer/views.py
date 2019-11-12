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

def index(request):

    shop_type = ShopType.objects.all()
    # print(shop_type.t_classify)
    cake = Goods.objects.filter(t_id=1)
    biscuit = Goods.objects.filter(t_id='2')
    # cooked_food = Goods.objects.filter(t_id='3')
    # dried_tofu = Goods.objects.filter(t_id='4')
    # nut = Goods.objects.filter(t_id='5')
    # preserved_fruit = Goods.objects.filter(t_id='6')
    # chocolate = Goods.objects.filter(t_id='7')
    # seafood = Goods.objects.filter(t_id='8')
    # tea = Goods.objects.filter(t_id='9')
    # liquor = Goods.objects.filter(t_id='10')
    return render(request, 'buyer/index.html',locals())

def base(request):
    return render(request, 'buyer/base.html')
# Create your views here.
