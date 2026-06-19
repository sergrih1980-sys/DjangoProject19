from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .forms import RegistrationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .forms import LoginForm


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = True  # Активируем сразу
            user.save()

            # Отправка приветственного письма
            send_mail(
                'Добро пожаловать!',
                f'Здравствуйте, {user.email}! Спасибо за регистрацию.',
                settings.DEFAULT_FROM_EMAIL,
                [user.email],
                fail_silently=False,
            )

            messages.success(request, 'Регистрация успешна! Проверьте почту.')
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'users/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, username=email, password=password)

            if user is not None:
                login(request, user)
                messages.success(request, f'Добро пожаловать, {user.email}!')
                return redirect('home')  # или куда нужно
            else:
                messages.error(request, 'Неверные учётные данные')
    else:
        form = LoginForm()
    return render(request, 'users/login.html', {'form': form})

@login_required
def home(request):
    return render(request, 'users/home.html')

