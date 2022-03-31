from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import prove
from .models import grate
from .models import hmm
# Create your views here.

def hello(request):
    return render(request, 'index.html')

def work(request):
    return render(request, 'mission.html')

def join(request):
    return render(request, 'involve.html')

def don(request):
    if request.method == 'POST':
        full_name = request.POST['name']
        email = request.POST['email']
        occupation = request.POST['occupation']
        address = request.POST['address']
        state = request.POST['state']
        country = request.POST['country']
        opt = request.POST['optional']
        prof = request.POST['proof']

        data = prove(name=full_name, email=email, occupation=occupation, address=address, state=state, country=country, option=opt, sub=prof)
        data.save()
    
    wis = grate.objects.all()
    return render(request, 'donate.html', {"wis":wis})


def myhome(request):
    return render(request, 'home.html')

def myblog(request):
    
    return render(request, 'blog.html')

def mymedia(request):
    fam = hmm.objects.all()
    return render(request, 'media.html', {"fam":fam})

# def love(request):
    
