from django.shortcuts import render
from django.shortcuts import HttpResponseRedirect
# from Buyer.models import User

def login(request):
    hint = ''
    if request.method == 'POST':
        email = request.POST.get('email')
        pw = request.POST.get('pw')
        # if email:
        #     user = User.objects.filter(email=email).first()
        #     if user:
        #         d_password = user.password
        #         if pw == d_password:
        #             response = HttpResponseRedirect('/')
        #             response.set_cookie('email', user.email)
        #             response.set_cookie('user_id', user.id)
        #             request.session['email'] = user.email
        #             return response
        #         else:
        #             hint = '密码不正确'
        #     else:
        #         hint = '用户名不存在'
        # else:
        #     hint = '邮箱不能为空'
    return render(request, 'buyer/login.html', locals())

def register(request):
    hint = ''
    if request.method == 'POST':
        email = request.POST.get('email')
        pw = request.POST.get('pw')
        pwr = request.POST.get('pwr')
        # if email:
        #     user = User.objects.filter(email=email).first()
        #     if not user:
        #         if pw == pwr:
        #             u = User()
        #             u.email = email
        #             u.password = pw
        #             u.save()
        #             hint = '注册成功，请登录'
        #         else:
        #             hint = '两次输入密码不一致'
        #     else:
        #         hint = '邮箱已被注册'
        # else:
        #     hint = '邮箱不能为空'
    return render(request, 'buyer/register.html', locals())

def index(request):

    # snacks = Shop.objects.filter(c_classify='0')
    # snacks = snacks[:8]
    # raw_meat = Shop.objects.filter(c_classify='1')
    # cooked_food = Shop.objects.filter(c_classify='2')
    # Nuts = Shop.objects.filter(c_classify='3')
    # chocolate = Shop.objects.filter(c_classify='4')
    # seafood = Shop.objects.filter(c_classify='5')
    # liquor = Shop.objects.filter(c_classify='6')
    # fruits = Shop.objects.filter(c_classify='7')
    # tea = Shop.objects.filter(c_classify='8')
    # tableware = Shop.objects.filter(c_classify='9')
    return render(request, 'buyer/index.html',locals())

def base(request):
    return render(request, 'buyer/base.html')
# Create your views here.
