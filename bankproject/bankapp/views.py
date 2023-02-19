from django.shortcuts import render, get_object_or_404

# Create your views here.
from .models import District, Branch


def demo(request, c_slug=None):
    district=District.objects.all()
    branch=Branch.objects.all()
    return render(request, 'index.html', {'dist': district, 'branch': branch})

