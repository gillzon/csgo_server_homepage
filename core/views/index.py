import os
from django.shortcuts import render, redirect
from core.models.rankme import Rankme
from core.models.user import CustomUser
# Create your views here.
# Create your views here.
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from core.forms.signup import SignUpForm as UserCreationForm
from django.contrib.auth import authenticate, login


@login_required
def home(request):
    players = Rankme.objects.all().order_by('-score')
    page_num = request.GET.get('page', 1)

    paginator = Paginator(players, 15)
    page_obj = paginator.page(page_num)

    ctx = {'obj': page_obj}
    return render(request, 'home/index.html', context=ctx)


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('core:home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})


def player_detailed_view(request, id):
    player = Rankme.objects.get(id=id)
    ctx = {'obj': player}
    print(dir(player))
    return render(request, 'player/details.html', context=ctx)


def server_info(request):
    server_ip = os.environ['SERVER_IP']
    ctx = {'SERVER_IP': server_ip}
    return render(request, 'server/info.html', context=ctx)


def user_profile(request):
    user = CustomUser.objects.get(id=request.user.id)
    print(user)
    ctx = {'obj': user}
    return render(request, 'player/profile.html', context=ctx)
