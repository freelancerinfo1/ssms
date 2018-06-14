""" Views for the base application """

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from ssms.models import Banner,Teachers, ParentFeedback, NewsAndEvents
def home(request):
    """ Default view for the root """
    banners = Banner.objects.filter()
    home_teachers = Teachers.objects.filter(home_page=True,is_approved=True).order_by('id')[:4]
    parent_feedbacks = ParentFeedback.objects.filter()
    news_and_events = NewsAndEvents.objects.filter().order_by('-id')[:4]
    return render(request, 'base/home.html',{"banners":banners,"home_teachers":home_teachers,"parent_feedbacks":parent_feedbacks,"news_and_events":news_and_events})
