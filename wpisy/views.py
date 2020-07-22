from django.shortcuts import render
from django.utils import timezone
from django.http import HttpResponse
from .models import Wpis
from .forms import PostForm
from django.forms import forms
from django.shortcuts import redirect
from django.db.models import Max

def Dom(request, *args, **kwargs):
        posts = Wpis.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
        #wpis.objects.all()[0].punkty
        #w nawiasie kwadratowym działają numery do 2, a nie do 39, jak się nazywają w /admin
        najlepszy_wynik = Wpis.objects.aggregate(Max('punkty'))['punkty__max']
        if request.method == "POST":
            form = PostForm(request.POST)
            if form.is_valid():
                post = form.save(commit=False)
                post.save()
                return redirect('Dom')
        else:
            form = PostForm()
        return render(request, 'dane.html', {'form': form, 'posts': posts, 'najlepszy_wynik': najlepszy_wynik,})

def Gracjan(request):
    posts = Wpis.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    postunie = Wpis.objects.filter(strzelec="Gracjan")
    wszys_wyn = 0
    return render(request, 'dane2.html', {'posts': posts, 'postunie': postunie, 'wszys_wyn': wszys_wyn})

def Konrad(request):
    posts = Wpis.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    postunie = Wpis.objects.filter(strzelec="Konrad")
    wszys_wyn = 0
    return render(request, 'dane4.html', {'posts': posts, 'postunie': postunie, 'wszys_wyn': wszys_wyn})

def Kura(request):
    posts = Wpis.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    postunie = Wpis.objects.filter(strzelec="Bestia")
    wszys_wyn = 0
    return render(request, 'dane5.html', {'posts': posts, 'postunie': postunie, 'wszys_wyn': wszys_wyn})

def Hampel(request):
    posts = Wpis.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    postunie = Wpis.objects.filter(strzelec="Hympel")
    wszys_wyn = 0
    return render(request, 'dane3.html', {'posts': posts, 'postunie': postunie, 'wszys_wyn': wszys_wyn})

#SĄ PROBLEMY Z DATĄ GDY UŻYWAM FORMULARZA, Z PANELU ADMINA ZAPISUJE JĄ NORMALNIE

# def post_edit(request):
#     post = get_object_or_404(Post)
#     if request.method == "POST":
#         form = PostForm(request.POST, instance=post)
#         if form.is_valid():
#             post = form.save(commit=False)
#             post.author = request.user
#             post.published_date = timezone.now()
#             post.save()
#             return redirect('Dom')
#     else:
#         form = PostForm(instance=post)
#     return render(request, 'post_edit.html', {'form': form})

#Nie jest edit potrzebny, w post_new linijke z render zedytuj, trzeba jakoś przenieść Wpis.objects.filter(...)
#https://docs.djangoproject.com/pl/2.2/topics/http/shortcuts/
#Zmieniłeś też podpis na "dane.html", winno być "post_edit.html"
#https://tutorial.djangogirls.org/pl/django_urls/