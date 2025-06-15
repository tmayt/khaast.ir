import re
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, get_user_model

User = get_user_model()

PHONE_REGEX = r'^09\d{9}$'  # شماره موبایل باید شبیه 09123456789 باشد

def login(request):
    error = None
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '').strip()

        if not re.match(PHONE_REGEX, username):
            error = "شماره موبایل معتبر نیست."
        elif not password:
            error = "رمز عبور الزامی است."
        else:
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('home')  # نام آدرس صفحه خانه خود را اینجا قرار دهید
            else:
                error = "شماره موبایل یا رمز عبور اشتباه است."

    return render(request, 'login.html', {'error': error})


def register(request):
    error = None
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '').strip()
        repassword = request.POST.get('repassword', '').strip()
        fname = request.POST.get('fname', '').strip()
        lname = request.POST.get('lname', '').strip()

        if not re.match(PHONE_REGEX, username):
            error = "شماره موبایل معتبر نیست."
        elif len(password) < 6:
            error = "رمز عبور باید حداقل ۶ کاراکتر باشد."
        elif password != repassword:
            error = "رمزهای عبور مطابقت ندارند."
        elif User.objects.filter(username=username).exists():
            error = "کاربری با این شماره موبایل قبلا ثبت شده است."
        else:
            user = User.objects.create_user(
                username=username,
                password=password,
                first_name=fname,
                last_name=lname,
            )
            auth_login(request, user)
            return redirect('home')

    return render(request, 'register.html', {'error': error})
