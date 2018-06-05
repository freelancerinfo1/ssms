""" Views for the base application """

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from ssms.models import Banner,Teachers
def home(request):
    """ Default view for the root """
    banners = Banner.objects.filter()
    home_teachers = Teachers.objects.filter(home_page=True,is_approved=True).order_by('id')[:4]
    return render(request, 'base/home.html',{"banners":banners,"home_teachers":home_teachers})
