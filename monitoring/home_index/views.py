from django.shortcuts import render
#from .models import UserProfile

# Create your views here.

def index_page(request):
    return render(request, 'home/index_page.html')


